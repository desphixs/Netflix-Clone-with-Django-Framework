from django.urls import path
from .views import Home, ProfileList, ProfileCreate, Watch, ShowMovieDetail, ShowMovie

app_name='netflixapp'

urlpatterns = [
    path('', Home.as_view(), name="Home"),
    path('profiles', ProfileList.as_view(), name="profile-lists"),
    path('profiles/create/', ProfileCreate.as_view(), name="profile-create"),
    path('watch/<str:profile_id>/', Watch.as_view(), name="watch"),
    path('movie/detail/<str:movie_id>/', ShowMovieDetail.as_view(), name="show_det"),
    path('movie/play/<str:movie_id>/', ShowMovie.as_view(), name="play"),
    
    
]

