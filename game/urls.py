from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index' ),
    path('games/', views.games, name='games'),
    path('gamegenre/', views.gamegenre, name='gamegenre'),
    path('newReview/', views.newReview, name='newreview'),
    path('gameStores/', views.gameStores, name='gameStores'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]