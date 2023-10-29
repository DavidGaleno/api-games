from django.db import models



class Genre(models.Model):
    name= models.CharField(max_length=20,unique=True)
    def __str__(self) -> str:
        return self.name
    
class Franchise(models.Model):
    name= models.CharField(max_length=20,unique=True)
    def __str__(self) -> str:
        return self.name

class Developer(models.Model):
    name= models.CharField(max_length=20,unique=True)
    def __str__(self) -> str:
        return self.name

class Publisher(models.Model):
    name= models.CharField(max_length=20,unique=True)
    def __str__(self) -> str:
        return self.name
    
class Game(models.Model):
    name =  models.CharField(max_length=100,unique=True)
    release_date = models.DateField()
    franchise = models.ForeignKey(Franchise,on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    developer = models.ForeignKey(Developer,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class GameGenre(models.Model):
    game = models.ForeignKey(Game,on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    

