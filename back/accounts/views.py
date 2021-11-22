from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import UserSerializer, UserProfileSerializer, UserReviewSerializer

from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model

from movies.models import Review, Movie, Genre
from movies.serializers import MovieSerializer, GenreSerializer


User = get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny])
# 회원가입시는 인증 x 
def signup(request):
    # 사용자에게 요청으로 넘어온 패스워드 데이터 받기
    password = request.data.get('password')
    passwordConfirmation = request.data.get('passwordConfirmation')

    # 패스워드와 확인용 패스워드 일치 여부 검사
    if password != passwordConfirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    # 아이디 일치여부 검사
    if User.objects.filter(username=request.data.get('username')).exists():
        return Response({'error': '이미 존재하는 아이디입니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # 닉네임 일치여부 검사
    if User.objects.filter(nickname=request.data.get('nickname')).exists():
        return Response({'error': '이미 존재하는 별명입니다.'}, status=status.HTTP_400_BAD_REQUEST)

    # UserSerializer를 통해 사용자가 넘겨준 데이터 직렬화
    serializer = UserSerializer(data=request.data)

    # validation (password도 같이 직렬화)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        # password 해싱 -> password -> 문자열 데이터로, set_password 메서드는 User 객체 저장 x 
        user.set_password(request.data.get('password'))
        # 유저 객체 저장
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def profile(request):
    # profile 조회
    if request.method == 'GET':
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

    # profile 수정
    elif request.method == 'PUT':

        # profile 이미지 받기
        profile_image = request.data.get('profile_image')
        print(profile_image)
        # background 이미지 받기
        background_image = request.data.get('background_image')
        print(background_image)

        # 별명 수정 시 일치여부 검사
        if request.user.nickname != request.data.get('nickname') and User.objects.filter(nickname=request.data.get('nickname')).exists():
            return Response({'error': '이미 존재하는 별명입니다.'}, status=status.HTTP_400_BAD_REQUEST)

        
        serializer = UserProfileSerializer(request.user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            print('serializer is valid!')
            serializer.save(profile_image=profile_image, background_image=background_image)
            return Response(serializer.data)
        else:
            print('is not valid')
    
    # 회원탈퇴
    elif request.method == 'DELETE':
        user_pk = request.user.pk
        request.user.delete()
        return Response({ 'delete': f'{user_pk}번 회원이 탈퇴했습니다.' }, status=status.HTTP_204_NO_CONTENT)

'''
유저가 작성한 리뷰 목록 조회
'''
@api_view(['GET'])
@permission_classes([AllowAny])
def reviews(request, user_pk):
    reviews = Review.objects.filter(user__pk=user_pk).order_by('-pk')
    serializer = UserReviewSerializer(reviews, many=True)
    return Response(serializer.data)

from django.http import JsonResponse
@api_view(['GET'])
@permission_classes([AllowAny])
def reviews_genre(request, user_pk):

    # Genre to query set list
    result = Genre.objects.values()
    # queryset list to python list
    genres = [genre for genre in result]
    # 장르 개수 초기화
    genres_cnt = {}
    for genre in genres:
        genres_cnt[genre['name']] = 0

    # 리뷰 조회
    if request.method == 'GET':
        reviews = [review for review in Review.objects.filter(user__pk=user_pk).order_by('-pk').values()]
        for review in reviews:
            genres = [genre for genre in Genre.objects.filter(movies__id=review['movie_id']).values()]
            for genre in genres:
                genres_cnt[genre['name']] += 1
    
    return JsonResponse(genres_cnt)

@api_view(['GET'])
@permission_classes([AllowAny])
def reviews_country(request, user_pk):

    # Genre to query set list
    countries = ['브라질', '콜롬비아', '멕시코', '라스베이거스', '워싱턴', '시카고', '캐나다', '칠레', '일본', 
    '홍콩', '중국', '인도', '호주', '뉴질랜드', '영국', '프랑스', '이탈리아', '남아프리카공화국', '소말리아', '모로코']
    
    # 장르 개수 초기화
    countries_cnt = {}
    for country in countries:
        countries_cnt[country] = 0

    # 리뷰 조회
    if request.method == 'GET':
        reviews = [review for review in Review.objects.filter(user__pk=user_pk).order_by('-pk').values()]
        for review in reviews:
            countries = [movie['country_name'] for movie in Movie.objects.filter(id=review['movie_id']).values()]
            for country in countries:
                countries_cnt[country] += 1
    
    return JsonResponse(countries_cnt)

@api_view(['GET'])
@permission_classes([AllowAny])
def reviews_movies(request, user_pk):
    
    movieList = []
    # 리뷰에 해당하는 영화 조회
    if request.method == 'GET':
        movieIds = [review['movie_id'] for review in Review.objects.filter(user__pk=user_pk).order_by('-pk').values()]
        for movieId in movieIds:
            movie = Movie.objects.filter(id=movieId).values()[0]
            genreNames = [genre['name'] for genre in Genre.objects.filter(movies__id=movie['id']).values()]
            movieList.append({'title':movie['title'], 'poster_path':movie['poster_path'], 'country_name':movie['country_name'], 'genre_names': genreNames})

    return JsonResponse(movieList, safe=False)           


    