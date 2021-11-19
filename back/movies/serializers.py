from rest_framework import serializers
from .models import Movie, Review, Comment, Genre, Director, Actor, VoteRate

from accounts.serializers import UserProfileSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'user', 'review', 'content', 'created_at', 'updated_at',)
        read_only_fields = ('review',)


class ReviewSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)
    user = UserProfileSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('id', 'user', 'movie', 'title', 
        'rank', 'content', 'created_at', 'updated_at'
        , 'comments', 'comments_count')
        read_only_fields = ('movie',)


# 영화 리스트 Read용
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id',
            'genres',
            'title',
            'overview',
            'poster_path',
            'popularity',
            'poster_path', 
            'vote_count', 
            'vote_avg', 
            'user_vote_count', 
            'user_vote_avg',
            'country_name',
        )

# 단일 영화 Read용
class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    reviews_count = serializers.IntegerField(source='reviews.count', read_only=True)
    class Meta:
        model = Movie
        fields = (
            'id',
            'genres',
            'title',
            'overview',
            'poster_path',
            'popularity',
            'poster_path', 
            'vote_count', 
            'vote_avg', 
            'user_vote_count', 
            'user_vote_avg',
            'country_name',
            'reviews',
            'reviews_count',
            
        )


class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'

class VoteRateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VoteRate
        fields = ('id', 'user', 'movie', 'rate',)
        read_only_fields = ('user', 'movie',)






