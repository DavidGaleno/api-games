from rest_framework import serializers
from games_database_api.models import Game,Genre,Franchise,Developer,Publisher

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id','name','genre','release_date','franchise','developer','publisher']
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
        model= Developer,
        fields='__all__'
class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model= Publisher,
        fields='__all__'
     
