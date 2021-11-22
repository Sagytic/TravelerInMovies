from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # 영화 목록, 세부 영화 url
    path('',views.movie_list,name='movie_list'),
    path('<int:movie_pk>', views.movie_detail, name='movie_detail'),
    
    # 리뷰 목록, 세부 리뷰 url
    path('<int:movie_pk>/reviews', views.review_list, name='review_list'),
    path('reviews/<int:review_pk>', views.review_detail, name='review_detail'),

    # 댓글 목록, 상세 댓글 url
    path('reviews/<int:review_pk>/comments/', views.comment_list, name='comment_list'),
    path('comments/<int:comment_pk>/', views.comment_detail, name='comment_detail'),

    # 배우 호출 url
    # path('<int:movie_pk>/actors', views.actors, name='actors'),
    # 장르 호출 url
    path('<int:movie_pk>/genres', views.genres, name='genres'),
    # 감독 호출 url
    path('<int:movie_pk>/director', views.director, name='director'),

    # 평점 url
    path('<int:movie_pk>/voterate', views.voterate, name='voterate'),
]
