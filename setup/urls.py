"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from games_database_api.views import GamesViewSet,GenreViewSet,FranchiseViewSet,DeveloperViewSet,PublisherViewSet,GameGenreViewSet,ListGameGenreViewSet,ListGameFranchiseViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('games',viewset=GamesViewSet,basename='Games')
router.register('genres',viewset=GenreViewSet,basename='Genres')
router.register('franchises',viewset=FranchiseViewSet,basename='Franchises')
router.register('developers',viewset=DeveloperViewSet,basename='Developers')
router.register('publishers',viewset=PublisherViewSet,basename='Publishers')
router.register('gamegenres',viewset=GameGenreViewSet,basename='GameGenres')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('genres/<int:pk>/games',ListGameGenreViewSet.as_view()),
    path('franchises/<int:pk>/games',ListGameFranchiseViewSet.as_view())
]
