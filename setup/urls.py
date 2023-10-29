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
from games_database_api.views import GamesViewSet,GenreViewSet,FranchiseViewSet,DeveloperViewSet,PublisherViewSet,GameGenreViewSet,ListGameGenreViewSet,ListGameFranchiseViewSet,ListGameDeveloperViewSet
from rest_framework import routers
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
 

#Roteador
router = routers.DefaultRouter()


schema_view = get_schema_view(
   openapi.Info(
      title="GAMES DATABASE API",
      default_version='v1',
      description="Essa é uma API de jogos que contendo desenvolvedoras, publicadoras, gêneros e jogos. Ela já possui alguns filtros embutidos\n Nossa proposta é oferecer algo que pode ser consultado por fans, programadores e acionistas para conseguirem suas respectivas informações\n A API é livre para ser modificada e usada para outros fins",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


#Rotas das Entidades. Não inclui os filtros
router.register('games',viewset=GamesViewSet,basename='Games')
router.register('genres',viewset=GenreViewSet,basename='Genres')
router.register('franchises',viewset=FranchiseViewSet,basename='Franchises')
router.register('developers',viewset=DeveloperViewSet,basename='Developers')
router.register('publishers',viewset=PublisherViewSet,basename='Publishers')
router.register('gamegenres',viewset=GameGenreViewSet,basename='GameGenres')
urlpatterns = [
    #Rota para perfil de admin
    path('admin/', admin.site.urls),
    #Rotas de cada uma das entidades
    path('',include(router.urls)),
    #Filtra jogos de um gênero específico
    path('genres/<int:pk>/games',ListGameGenreViewSet.as_view(),name='games-genre'),
    #Filtra jogos de uma franquia especíica
    path('franchises/<int:pk>/games',ListGameFranchiseViewSet.as_view(),name='games-franchise'),
    path('developers/<int:pk>/games',ListGameDeveloperViewSet.as_view(),name='games-developer'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
