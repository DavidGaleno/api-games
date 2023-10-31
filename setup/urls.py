#Django Imports
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#Views
from games_database_api.views import GamesViewSet,GenreViewSet,FranchiseViewSet,DeveloperViewSet,PublisherViewSet,GameGenreViewSet,ListGameGenreViewSet,ListGameFranchiseViewSet,ListGameDeveloperViewSet,ProgrammingLanguageViewSet,GameEngineViewSet,GameProgrammingLanguageViewSet,ListGameProgrammingLanguageViewSet,ListGameGameEngineViewSet,ListGamePublisherViewSet


 

#Roteador
router = routers.DefaultRouter()

#Swagger Template
schema_view = get_schema_view(
   openapi.Info(
      title="GAMES DATABASE API",
      default_version='v1',
      description="Essa é uma API de jogos que contendo desenvolvedoras, publicadoras, gêneros e jogos. Ela já possui alguns filtros embutidos\n Nossa proposta é oferecer algo que pode ser consultado por fans e programadores para conseguirem suas respectivas informações\n A API é livre para ser modificada e usada para outros fins",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),

)


#Rotas das Entidades
router.register('games',viewset=GamesViewSet,basename='Game')
router.register('programming_language',viewset=ProgrammingLanguageViewSet,basename='ProgrammingLanguage')
router.register('game_engine',viewset=GameEngineViewSet,basename='GameEngine')
router.register('genres',viewset=GenreViewSet,basename='Genre')
router.register('game_programming_language',viewset=GameProgrammingLanguageViewSet,basename='GameProgrammingLanguage')
router.register('franchises',viewset=FranchiseViewSet,basename='Franchise')
router.register('developers',viewset=DeveloperViewSet,basename='Developer')
router.register('publishers',viewset=PublisherViewSet,basename='Publisher')
router.register('game_genres',viewset=GameGenreViewSet,basename='GameGenre')


#Filtros e perfis
urlpatterns = [
    #Rota para perfil de admin
    path('admin/', admin.site.urls),
    #Rota Swagger
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    #Rotas de cada uma das entidades
    path('',include(router.urls)),
    #Filtra jogos de um gênero específico
    path('genres/<int:pk>/games',ListGameGenreViewSet.as_view(),name='games-genre'),
    #Filtra jogos de uma franquia específica
    path('franchises/<int:pk>/games',ListGameFranchiseViewSet.as_view(),name='games-franchise'),
    #Filtra jogos de uma publicadora específica
    path('publishers/<int:pk>/games',ListGamePublisherViewSet.as_view(),name='games-franchise'),
    #Filtra jogos de uma desenvolvedora específica
    path('developers/<int:pk>/games',ListGameDeveloperViewSet.as_view(),name='games-developer'),
    #Filtra jogos de uma linguagem de programação específica
    path('programming_language/<int:pk>/games',ListGameProgrammingLanguageViewSet.as_view(),name='games-programming-language'),
    #Filtra jogos de uma engine específica
    path('game_engine/<int:pk>/games',ListGameGameEngineViewSet.as_view(),name='games-game-engine'),
]
