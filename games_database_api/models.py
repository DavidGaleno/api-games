from django.db import models



class Genre(models.Model):
    name= models.CharField(max_length=15)
    def __str__(self) -> str:
        return self.name
    
class Franchise(models.Model):
    name= models.CharField(max_length=15)
    def __str__(self) -> str:
        return self.name

class Developer(models.Model):
    name= models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name

class Publisher(models.Model):
    name= models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name
    
class Game(models.Model):
    name =  models.CharField(max_length=30)
    release_date = models.DateField()
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    franchise = models.ForeignKey(Franchise,on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    developer = models.ForeignKey(Developer,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

