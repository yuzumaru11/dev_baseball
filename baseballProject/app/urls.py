from django.urls import path
from .views import IndexView
from .views import TeamsView
from .views import PlayerView
from .views import LibraryView
from .views import NewsView

urlpatterns = [
    path('', IndexView.as_view()),
    path('teams/', TeamsView.as_view()),
    path('player/', PlayerView.as_view()),
    path('library/', LibraryView.as_view()),
    path('news/', NewsView.as_view()),
]
