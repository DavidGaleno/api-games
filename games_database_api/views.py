from django.http import JsonResponse
from rest_framework import viewsets,generics,filters
from games_database_api.models import Game,Genre,Franchise,Publisher,Developer
from games_database_api.serializer import GameSerializer,GenreSerializer,FranchiseSerializer,GameGenre,DeveloperSerializer,PublisherSerializer,GameGenreSerializer,ListGameGenreSerializer,ListGameFrenchiseSerializer,ListGameDeveloperSerializer,ListGamePublisherSerializer
from django_filters.rest_framework import DjangoFilterBackend


class GamesViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name','email']

class FranchiseViewSet(viewsets.ModelViewSet):
    queryset = Franchise.objects.all()
    serializer_class = FranchiseSerializer
class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
class GameGenreViewSet(viewsets.ModelViewSet):
    queryset= GameGenre.objects.all()
    serializer_class = GameGenreSerializer
class ListGameGenreViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = GameGenre.objects.filter(genre_id =self.kwargs['pk'])
        return queryset
    serializer_class = ListGameGenreSerializer
class ListGameFranchiseViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Game.objects.filter(franchise_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListGameFrenchiseSerializer
class ListGameDeveloperViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Game.objects.filter(developer_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListGameDeveloperSerializer
class ListGameDeveloperViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Game.objects.filter(publisher_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListGamePublisherSerializer