import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MOVIE_DB.settings')
import django
django.setup()
import requests
from movies.models import Movie, Genre, Actor, Director

# 국가별 영화 목록 가져오기
# movie_data = {
#     '브라질': ['hulk','jungle cruise', 'The Mission', 'Mechanic: Resurrection', 'Out of the Shadows', 'The Lost City of Z', 'Rio', 'Rio 2', 'Woman on Top', 'The Rundown', 'Bacurau'],
#     '콜롬비아': ['Proof Of Life', 'Lord Of War', 'Romancing the Stone', 'Colombiana', 'Miami Vice', 'Mr. & Mrs. Smith', 'El abrazo de la serpiente', 'American Made', 'Triple X', 'Triple Frontier'],
#     '멕시코': ['No Country for Old Men','Life of Pi', 'Fast & Furious', 'Sicario', 'Once Upon a Time in Mexico', 'Kill Bill: Volume 1', 'From Dusk Till Dawn', 'Godzilla: King of the Monsters', 'The Perfect Game', 'Coco'],
#     '라스베이거스': ['Now You See Me', 'The Hangover', 'Step Up All In', 'The Big Short', 'Godzilla'],
#     '워싱턴': ['The Bourne Legacy','Suicide Squad', 'The Silence of the Lambs', 'Mission: Impossible – Rogue Nation'],
#     '시카고': ['Chicago', 'When Harry Met Sally'],
#     '캐나다': ['3 Needles', 'The Time Travelers Wife', 'Catch Me If you can', 'Mean Girls', 'Brokeback Mountain', 'Cool Running', 'superman  III', 'The Twilight Saga: New Moon', 'X-Men: Last Stand', 'One Week'],
#     '칠레': ['Pacto de fuga', 'Colonia', 'The 33', 'The Motorcycle Diaries', 'El Club', 'Aftershock', 'Its Raining on Santiago', 'violeta went to heaven', 'Mi Mejor Enemigo'],
#     '일본': ['Wife of a Spy', 'The Town Where Only I Am Missing', 'Asako', 'Our Little Sister', 'Lost In Translation', 'Love Letter', 'The Sea of Trees', 'Good&Bye', 'Anarchist from Colony', 'Memoirs of a Geisha'],
#     '홍콩': ['Skyscraper', '엽문 더 파이널', '도둑들', '保持通話', 'Godzilla vs. Kong', 'Push', 'Lust, Caution', 'Shock Wave 2', 'BB project', 'Blackhat'],
#     '중국': ['The Wandering Earth', 'The Eight Hundred', 'Lost in Beijing', '007 Skyfall', 'The Captain', 'Finding Mr Right', 'Still Life', 'To The Fore', 'The Game Changer', 'The Game Changer'],
#     '인도': ['3 Idiots', '당갈', 'Life of PI', 'Secret Superstar', 'Hotel Mumbai', '피케이', 'Yeh Ballet', 'Rocky Handsome', 'Slumdog Millionaire'],
#     '호주': ['Australia', 'Finding Nemo','matrix', 'Mission: Impossible II', 'kangaroo Jack', 'A Single rider', 'The Nightingale', 'Opal Dream'],
#     '뉴질랜드': ['The chronicles of Narnia : prince Caspian', 'X-Men Origins: Wolverin', 'Vertical Limit', 'The Worlds Fastest Indian', 'The Piano', 'Avatar', 'The Light Between Oceans', 'Once Were Warriors', 'Shadow in the Cloud', 'Born to Dance'],
#     '영국': ['Cruella', 'TENET', 'Kingsman: The Secret Service', 'Kingsman: The Golden Circle', 'A Clockwork Orange', 'About Time', 'Monty Python and the Holy Grail', 'The Lord of the Rings: The Fellowship of the Ring', 'The Lord of the Rings: The Two Towers', 'The Lord of the Rings: The Return of the King', 'Harry Potter and the Sorcerers Stone', 'Harry Potter and the Chamber of Secrets', 'Harry Potter and the Goblet of Fire', 'Harry Potter and the Order of the Phoenix', 'Harry Potter and the Half-Blood Prince', 'Harry Potter and the Deathly Hallows Part 1', 'Harry Potter And The Deathly Hallows: Part 2'],
#     '프랑스': ['Les Misérables', 'Midnight in Paris', 'Intouchables', 'Attila Marcel', 'Young & Beautiful', 'Young Ahmed', 'The Dreamers', 'Inglourious Basterds', 'Saving Private Ryan', 'Farinelli'],
#     '이탈리아': ['인생은 아름다워', 'Roman Holiday', 'The Best Offer', 'Cinema Paradiso', '그레이트 뷰티', 'Made In Italy', 'Ladri di biciclette', 'The Bourne Identity', 'The Bourne Supremacy', 'A Farewell to Arms'],
#     '남아프리카공화국': ['DISTRICT 9', '10,000 BC', 'Black Panther', 'Invictus', 'Mandela: Long Walk to Freedom', 'CHAPPiE'],
#     '소말리아': ['Black Hawk Down','Escape From Mogadishu', 'Captain Phillips', '438 Days'],
#     '모로코': ['Mission: Impossible – Rogue Nation','The Bourne Ultimatum', 'Allied', 'Escape Plan', 'John Wick Chapter 3 – Parabellum'],
# }

movie_data = {
    '브라질': ['hulk','jungle cruise', 'The Mission', 'Mechanic: Resurrection', 'Out of the Shadows', 'The Lost City of Z', 'Rio', 'Rio 2', 'Woman on Top', 'The Rundown', 'Bacurau'],
}


api_key = '4b04a84decc47f820d768b6bc7d5b378'

genre_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=ko-KR'
# 장르 아이디 및 이름 가져와서 DB에 적재
def get_genre(genre_url):
    genres = requests.get(genre_url).json().get('genres')
    for genre in genres:
        genre_instance = Genre(tmdb_genre_id=genre['id'], name=genre['name'])
        genre_instance.save()

def get_movie(movie_data):
    for nation in movie_data:
        for title in movie_data[nation]:
            url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=ko-KR&query={title}&page=1&include_adult=true'
            url_en = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=en-US&query={title}&page=1&include_adult=true'
            movie = requests.get(url).json().get('results')[0]

            movieId = movie['id']
            title = movie['title']
            poster_path = 'https://image.tmdb.org/t/p/w500'+movie['poster_path']
            popularity = movie['popularity']
            vote_count = movie['vote_count']
            vote_avg = movie['vote_average']
            genre_ids = movie['genre_ids']
            overview = movie['overview']
            country_name = nation

            if not overview:
                movie = requests.get(url_en).json().get('results')[0]
                overview = movie['overview']

            print(title, '-----')
            # Movie에 데이터 추가
            movie_instance = Movie(title=title, overview=overview, poster_path=poster_path, popularity=popularity, vote_count= vote_count, vote_avg = vote_avg, country_name=country_name)
            movie_instance.save()

            # 장르와 N:M 관계 추가
            for genre_id in genre_ids:
                genre = Genre.objects.get(tmdb_genre_id=genre_id)
                movie_instance.genres.add(genre)


            # 배우 추가
            img_path = 'https://image.tmdb.org/t/p/original'
            url_credits = f'https://api.themoviedb.org/3/movie/{movieId}/credits?api_key={api_key}&language=ko-KR'
            credits = requests.get(url_credits).json()
            for actor in credits['cast'][:5]:
                if actor['profile_path']:
                    profile_path = img_path + actor['profile_path']
                else:
                    profile_path = 'None'
                actor_instance = Actor(id=actor['id'], name=actor['original_name'], profile_path=profile_path)
                try: actor_instance.save()
                except: pass
                # 배우 : 영화 N:M 관계 추가
                actor_instance.movies.add(movie_instance)
            
            # 감독 추가
            for crew in  credits['crew']:
                if crew['job'] == 'Director':
                    if crew['profile_path']:
                        profile_path = img_path + actor['profile_path']
                    else:
                        profile_path = 'None'
                    director_instance = Director(id=crew['id'], name=crew['original_name'], profile_path=profile_path)
                    try: director_instance.save()
                    except: pass
                    # 감독 : 영화 N:M 관계 추가
                    director_instance.movies.add(movie_instance)
                    break


get_genre(genre_url)
get_movie(movie_data)

# print(Genre.objects.get(id=4).movies.all().count())
# print(Movie.objects.get(id=4).genres)