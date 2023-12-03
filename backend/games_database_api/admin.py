from django.contrib import admin
from games_database_api.models import Game,Genre,Franchise,Developer,Publisher,GameGenre

class Games(admin.ModelAdmin):
    list_display = ('id','name','release_date','franchise','developer','publisher')
    list_display_links = ('id','name','release_date','franchise','developer','publisher')
    search_fields = ('name','id')
    list_per_page = 20

admin.site.register(Game,Games)

class Genres(admin.ModelAdmin):
    list_display= ('id','name')
    list_display_links= ('id','name')
    search_fields= ('id','name')
    list_per_page = 20
admin.site.register(Genre,Genres)

class Franchises(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name','id')
    list_per_page = 20

admin.site.register(Franchise,Franchises)

class Developers(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name','id')
    list_per_page = 20

admin.site.register(Developer,Developers)

class Publishers(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name','id')
    list_per_page = 20

admin.site.register(Publisher,Publishers)

class GameGenres(admin.ModelAdmin):
    list_display = ('id','game','genre')
    list_display_links = ('id','game','genre')
    search_fields = ('id','game','genre')
    list_per_page = 20

admin.site.register(GameGenre,GameGenres)
