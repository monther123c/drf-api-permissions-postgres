from django.urls import path

from .views import GameListView, GameDetailView,PlayerListView,PlayerDetailView

urlpatterns = [
    path('', GameListView.as_view(), name='games_list'),
    path('<int:pk>/', GameDetailView.as_view(), name='games_detail'),
    path('player/', PlayerListView.as_view(), name='player_list'),
    path('player/<int:pk>/', PlayerDetailView.as_view(), name='player_detail'),
]