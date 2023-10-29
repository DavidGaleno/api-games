from rest_framework import serializers
from games_database_api.models import Game,Genre,Franchise,Developer,Publisher,GameGenre

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id','name','release_date','franchise','developer','publisher']
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
class FranchiseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Franchise
        fields='__all__'
class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model= Developer
        fields='__all__'
class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model= Publisher
        fields='__all__'
class GameGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameGenre
        fields='__all__'
class ListGameGenreSerializer(serializers.ModelSerializer):
    game = serializers.ReadOnlyField(source='game.name')
    genre = serializers.ReadOnlyField(source='genre.name')
    class Meta:
        model = GameGenre
        fields = '__all__'
class ListGameFrenchiseSerializer(serializers.ModelSerializer):
    game = serializers.ReadOnlyField(source='game.name')
    franchise = serializers.ReadOnlyField(source='franchise.name')
    class Meta:
        model = Game
        fields = '__all__'
class ListGameDeveloperSerializer(serializers.ModelSerializer):
    game = serializers.ReadOnlyField(source='game.name')
    developer = serializers.ReadOnlyField(source='developer.name')
    class Meta:
        model = Game
        fields = '__all__'
class ListGamePublisherSerializer(serializers.ModelSerializer):
    game = serializers.ReadOnlyField(source='game.name')
    publisher = serializers.ReadOnlyField(source='publisher.name')
    class Meta:
        model = Game
        fields = '__all__'

     
