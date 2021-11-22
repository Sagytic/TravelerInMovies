from django.shortcuts import get_list_or_404, get_object_or_404

from accounts import serializers
from .models import Movie, Review, Comment, Genre, Director, Actor, VoteRate
from .serializers import UserProfileSerializer, MovieListSerializer, MovieSerializer, ReviewSerializer, CommentSerializer, GenreSerializer, DirectorSerializer, ActorSerializer, VoteRateSerializer
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from django.core.paginator import Paginator
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# 유저 모델 
User = get_user_model()

'''
메인 페이지
'''
@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

'''
단일 영화 조회
'''
@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

'''
전체 리뷰 조회 및 생성
'''
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def review_list(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    # 리뷰 조회
    if request.method == 'GET':
        reviews = Review.objects.filter(movie=movie_pk).order_by('-pk')
        paginator = Paginator(reviews, 5)
        page_number = request.GET.get('page_num')
        reviews = paginator.get_page(page_number)
        serializer = ReviewSerializer(reviews, many=True)
        data = serializer.data
        data.append({'total_pages': paginator.num_pages})
        return Response(data)
    
    # 리뷰 생성
    elif request.method == 'POST':
        print(request.data)
        serializer = ReviewSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

'''
단일 리뷰 조회, 수정 및 삭제
'''
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    # 단일 리뷰 조회
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    # 현재 유저와 리뷰를 쓴 유저가 같은 경우만 수정 및 삭제
    elif request.user == review.user:
        # 리뷰 수정
        if request.method == 'PUT':
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

        # 리뷰 삭제
        elif request.method == 'DELETE':
            review.delete()
            data = {
                'delete' : f'{review_pk}번 리뷰가 삭제되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        
    return Response({ 'Unauthorized': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

'''
전체 댓글 조회 및 생성
'''
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def comment_list(request, review_pk):
    # 현재 리뷰 가져오기
    review = get_object_or_404(Review, pk=review_pk)
    
    # 해당 리뷰의 댓글 조회
    if request.method == 'GET':
        comments = Comment.objects.filter(review__pk=review_pk).order_by('-pk')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    # 해당 리뷰의 댓글 작성
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # Vue에서 axios 요청할 때 URI에 movie의 id값을 넣어서 요청해야 함
            serializer.save(user=request.user, review=review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

'''
상세 댓글 수정 및 삭제
'''
@api_view(['PUT', 'DELETE'])
@permission_classes([AllowAny])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    # 현재 유저와 댓글 작성자가 같을 때 수정 및 삭제 가능
    if request.user == comment.user:
        # 수정
        if request.method == 'PUT':
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        # 삭제
        elif request.method == 'DELETE':
            comment.delete()
            data = {
                'delete' : f'{comment_pk}번 댓글이 삭제되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        
    return Response({ 'Unauthorized': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)


# 평점 매기는거는 나중에 
def voterate(request, movie_pk):
    pass

