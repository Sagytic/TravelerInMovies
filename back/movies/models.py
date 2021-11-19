from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Genre(models.Model):
    tmdb_genre_id = models.IntegerField()
    name = models.CharField(max_length=50)


class Movie(models.Model):
    # 장르와 N:M 관계
    genres = models.ManyToManyField(Genre, related_name='movies')

    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    popularity = models.FloatField()
    vote_count = models.BigIntegerField()
    vote_avg   = models.FloatField()
    user_vote_count = models.BigIntegerField(default=0)
    user_vote_avg = models.FloatField(default=0)
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Director(models.Model):
    id = models.BigIntegerField(primary_key=True)
    movies = models.ManyToManyField(Movie, related_name='directors')
    name = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Actor(models.Model):
    id = models.BigIntegerField(primary_key=True)
    movies = models.ManyToManyField(Movie, related_name='actors')
    name = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movies')

    like_users = models.ManyToManyField(User, related_name='like_reviews')

    title = models.CharField(max_length=100)
    rank = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content


class VoteRate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movie_rate')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='user_rate')
    rate = models.FloatField()




