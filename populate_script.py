import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from games_database_api.models import Genre,Developer,Franchise,Game,GameGenre,Publisher,ProgrammingLanguage,GameEngine,GameProgrammingLanguage

fake = Faker('pt_BR')


def create_genres():
    genre = Genre(name="survival horror")
    genre.save()
    genre = Genre(name="action")
    genre.save()
    genre = Genre(name="action/adventure")
    genre.save()
    genre = Genre(name="fps")
    genre.save()
    genre = Genre(name="hack and slash")
    genre.save()
    genre = Genre(name="metroidvania")
    genre.save()
    genre = Genre(name="souls like")
    genre.save()
    genre = Genre(name="jrpg")
    genre.save()
    genre = Genre(name="rpg")
    genre.save()
    genre = Genre(name="point and click")
    genre.save()
    genre = Genre(name="fighting")
    genre.save()
    genre = Genre(name="sandbox")
    genre.save()
    genre = Genre(name="platform")
    genre.save()


def create_developers():
    developer = Developer(name="from software")
    developer.save()
    developer = Developer(name="capcom")
    developer.save()
    developer = Developer(name="konami")
    developer.save()
    developer = Developer(name="square enix")
    developer.save()
    developer = Developer(name="eidos")
    developer.save()
    developer = Developer(name="io interactive")
    developer.save()
    developer = Developer(name="rockstar")
    developer.save()
    developer = Developer(name="koei tecmo")
    developer.save()
    developer = Developer(name="netherealm")
    developer.save()
    developer = Developer(name="devolver digital")
    developer.save()
    developer = Developer(name="remedy entertainment")
    developer.save()
    developer = Developer(name="nintendo")
    developer.save()
    developer = Developer(name="team cherry")
    developer.save()
    developer = Developer(name="id software")
    developer.save()
    developer = Developer(name="ubisoft")
    developer.save()
    developer = Developer(name="infinity ward")
    developer.save()


def create_publishers():
    publisher = Publisher(name="bandai namco")
    publisher.save()
    publisher = Publisher(name="activision")
    publisher.save()
    publisher = Publisher(name="e&a")
    publisher.save()
    publisher = Publisher(name="capcom")
    publisher.save()
    publisher = Publisher(name="konami")
    publisher.save()
    publisher = Publisher(name="taketwo")
    publisher.save()
    publisher = Publisher(name="warner bros")
    publisher.save()
    publisher = Publisher(name="koei tecmo")
    publisher.save()
    publisher = Publisher(name="square enix")
    publisher.save()
    publisher = Publisher(name="devolver digital")
    publisher.save()
    publisher = Publisher(name="xbox game studios")
    publisher.save()
    publisher = Publisher(name="playstation studios")
    publisher.save()
    publisher = Publisher(name="nintendo")
    publisher.save()
    publisher = Publisher(name="team cherry")
    publisher.save()
    publisher = Publisher(name="bethesda softworks")
    publisher.save()
    publisher = Publisher(name="ubisoft")
    publisher.save()


def create_franchises():
    franchises = Franchise(name="resident evil")
    franchises.save()
    franchises = Franchise(name="silent hill")
    franchises.save()
    franchises = Franchise(name="call of duty")
    franchises.save()
    franchises = Franchise(name="battlefield")
    franchises.save()
    franchises = Franchise(name="dark souls")
    franchises.save()
    franchises = Franchise(name="the witcher")
    franchises.save()
    franchises = Franchise(name="final fantasy")
    franchises.save()
    franchises = Franchise(name="persona")
    franchises.save()
    franchises = Franchise(name="mortal kombat")
    franchises.save()
    franchises = Franchise(name="tomb raider")
    franchises.save()
    franchises = Franchise(name="grand theft auto")
    franchises.save()
    franchises = Franchise(name="allan wake")
    franchises.save()
    franchises = Franchise(name="mario bros.")
    franchises.save()
    franchises = Franchise(name="the legend of zelda")
    franchises.save()
    franchises = Franchise(name="hollow knight")
    franchises.save()
    franchises = Franchise(name="doom")
    franchises.save()
    franchises = Franchise(name="assassin's creed")
    franchises.save()
    franchises = Franchise(name="far cry")
    franchises.save()


def create_gamegenre():
    gamegenre = GameGenre(game=Game.objects.get(
        name="resident evil 4"), genre=Genre.objects.get(name='survival horror'))
    gamegenre.save()
    gamegenre = GameGenre(game=Game.objects.get(
        name="resident evil 4"), genre=Genre.objects.get(name='action/adventure'))
    gamegenre.save()
    gamegenre = GameGenre(game=Game.objects.get(
        name="resident evil 4 remake"), genre=Genre.objects.get(name='survival horror'))
    gamegenre.save()
    gamegenre = GameGenre(game=Game.objects.get(
        name="resident evil 4 remake"), genre=Genre.objects.get(name='action/adventure'))
    gamegenre.save()
    gamegenre = GameGenre(game=Game.objects.get(
        name="call of duty modern warfare 3 (2023)"), genre=Genre.objects.get(name='fps'))
    gamegenre.save()
    gamegenre = GameGenre(game=Game.objects.get(
        name="mortal kombat 1 (2023)"), genre=Genre.objects.get(name='fighting'))
    gamegenre.save()
    gamegenre = GameGenre(game=Game.objects.get(
        name="grand theft auto v"), genre=Genre.objects.get(name='fighting'))
    gamegenre.save()
    gamegenre = GameGenre(game=Game.objects.get(
        name="allan wake"), genre=Genre.objects.get(name='survival horror'))
    gamegenre.save()
    gamegenre = GameGenre(game=Game.objects.get(
        name="super mario bros. wonder"), genre=Genre.objects.get(name='platform'))
    gamegenre.save()
    gamegenre = GameGenre(game=Game.objects.get(
        name="the legend of zelda breath of the wild"), genre=Genre.objects.get(name='sandbox'))
    gamegenre.save()
    gamegenre = GameGenre(game=Game.objects.get(
        name="hollow knight"), genre=Genre.objects.get(name='metroidvania'))
    gamegenre.save()
    gamegenre = GameGenre(game=Game.objects.get(
        name="doom (2016)"), genre=Genre.objects.get(name='fps'))
    gamegenre.save()
    gamegenre = GameGenre(game=Game.objects.get(
        name="assassin's creed 1"), genre=Genre.objects.get(name='sandbox'))
    gamegenre.save()
    gamegenre = GameGenre(game=Game.objects.get(
        name="assassin's creed 1"), genre=Genre.objects.get(name='action/adventure'))
    gamegenre.save()
    gamegenre = GameGenre(game=Game.objects.get(
        name="far cry 5"), genre=Genre.objects.get(name='fps'))
    gamegenre.save()
    gamegenre = GameGenre(game=Game.objects.get(
        name="far cry 5"), genre=Genre.objects.get(name='sandbox'))
    gamegenre.save()


def create_programming_language():
    programmingLanguage = ProgrammingLanguage(name="c#")
    programmingLanguage.save()
    programmingLanguage = ProgrammingLanguage(name="c++")
    programmingLanguage.save()
    programmingLanguage = ProgrammingLanguage(name="c")
    programmingLanguage.save()
    programmingLanguage = ProgrammingLanguage(name="java")
    programmingLanguage.save()
    programmingLanguage = ProgrammingLanguage(name="python")
    programmingLanguage.save()


def create_game_engine():
    gameEngine = GameEngine(name="re engine")
    gameEngine.save()
    gameEngine = GameEngine(name="unreal engine 4")
    gameEngine.save()
    gameEngine = GameEngine(name="unity")
    gameEngine.save()
    gameEngine = GameEngine(name="iw")
    gameEngine.save()
    gameEngine = GameEngine(name="rockstar advanced game engine (rage)")
    gameEngine.save()
    gameEngine = GameEngine(name="northlight engine")
    gameEngine.save()
    gameEngine = GameEngine(name="modulesystem engine")
    gameEngine.save()
    gameEngine = GameEngine(name="havok physics engine")
    gameEngine.save()
    gameEngine = GameEngine(name="doomsday engine")
    gameEngine.save()
    gameEngine = GameEngine(name="ubisoft anvil")
    gameEngine.save()
    gameEngine = GameEngine(name="dunia engine")
    gameEngine.save()


def create_games():
    game = Game(name="resident evil 4", franchise=Franchise.objects.get(name="resident evil"), developer=Developer.objects.get(
        name="capcom"), publisher=Publisher.objects.get(name="capcom"), release_date='2005-01-11', gameEngine=GameEngine.objects.get(name="re engine"))
    game.save()
    game = Game(name="resident evil 4 remake", franchise=Franchise.objects.get(name="resident evil"), developer=Developer.objects.get(
        name="capcom"), publisher=Publisher.objects.get(name="capcom"), release_date='2023-03-24', gameEngine=GameEngine.objects.get(name="re engine"))
    game.save()
    game = Game(name="call of duty modern warfare 3 (2023)", franchise=Franchise.objects.get(name="call of duty"), developer=Developer.objects.get(
        name="infinity ward"), publisher=Publisher.objects.get(name="activision"), release_date='2023-11-10', gameEngine=GameEngine.objects.get(name="iw"))
    game.save()
    game = Game(name="mortal kombat 1 (2023)", franchise=Franchise.objects.get(name="mortal kombat"), developer=Developer.objects.get(name="netherealm"),
                publisher=Publisher.objects.get(name="warner bros"), release_date='2023-09-14', gameEngine=GameEngine.objects.get(name="unreal engine 4"))
    game.save()
    game = Game(name="grand theft auto v", franchise=Franchise.objects.get(name="grand theft auto"), developer=Developer.objects.get(
        name="rockstar"), publisher=Publisher.objects.get(name="taketwo"), release_date='2023-09-14', gameEngine=GameEngine.objects.get(name="rockstar advanced game engine (rage)"))
    game.save()
    game = Game(name="allan wake", franchise=Franchise.objects.get(name="allan wake"), developer=Developer.objects.get(
        name="remedy entertainment"), publisher=Publisher.objects.get(name="xbox game studios"), release_date='2010-05-14', gameEngine=GameEngine.objects.get(name="northlight engine"))
    game.save()
    game = Game(name="super mario bros. wonder", franchise=Franchise.objects.get(name="mario bros."), developer=Developer.objects.get(
        name="nintendo"), publisher=Publisher.objects.get(name="nintendo"), release_date='2023-10-20', gameEngine=GameEngine.objects.get(name="modulesystem engine"))
    game.save()
    game = Game(name="the legend of zelda breath of the wild", franchise=Franchise.objects.get(name="the legend of zelda"), developer=Developer.objects.get(
        name="nintendo"), publisher=Publisher.objects.get(name="nintendo"), release_date='2017-03-03', gameEngine=GameEngine.objects.get(name="havok physics engine"))
    game.save()
    game = Game(name="hollow knight", franchise=Franchise.objects.get(name="hollow knight"), developer=Developer.objects.get(
        name="team cherry"), publisher=Publisher.objects.get(name="team cherry"), release_date='2017-02-24', gameEngine=GameEngine.objects.get(name="havok physics engine"))
    game.save()
    game = Game(name="doom (2016)", franchise=Franchise.objects.get(name="doom"), developer=Developer.objects.get(
        name="id software"), publisher=Publisher.objects.get(name="bethesda softworks"), release_date='2016-05-13', gameEngine=GameEngine.objects.get(name="doomsday engine"))
    game.save()
    game = Game(name="assassin's creed 1", franchise=Franchise.objects.get(name="assassin's creed"), developer=Developer.objects.get(
        name="ubisoft"), publisher=Publisher.objects.get(name="ubisoft"), release_date='2007-11-13', gameEngine=GameEngine.objects.get(name="ubisoft anvil"))
    game.save()
    game = Game(name="far cry 5", franchise=Franchise.objects.get(name="far cry"), developer=Developer.objects.get(
        name="ubisoft"), publisher=Publisher.objects.get(name="ubisoft"), release_date='2018-03-27', gameEngine=GameEngine.objects.get(name="dunia engine"))
    game.save()


def create_game_programming_language():
    gameProgrammingLanguage = GameProgrammingLanguage(game=Game.objects.get(
        name="call of duty modern warfare 3 (2023)"), programmingLanguage=ProgrammingLanguage.objects.get(name="c++"))
    gameProgrammingLanguage.save()
    gameProgrammingLanguage = GameProgrammingLanguage(game=Game.objects.get(
        name="call of duty modern warfare 3 (2023)"), programmingLanguage=ProgrammingLanguage.objects.get(name="python"))
    gameProgrammingLanguage.save()
    gameProgrammingLanguage = GameProgrammingLanguage(game=Game.objects.get(
        name="call of duty modern warfare 3 (2023)"), programmingLanguage=ProgrammingLanguage.objects.get(name="c"))
    gameProgrammingLanguage.save()
    gameProgrammingLanguage = GameProgrammingLanguage(game=Game.objects.get(
        name="resident evil 4 remake"), programmingLanguage=ProgrammingLanguage.objects.get(name="c#"))
    gameProgrammingLanguage.save()
    gameProgrammingLanguage = GameProgrammingLanguage(game=Game.objects.get(
        name="resident evil 4 remake"), programmingLanguage=ProgrammingLanguage.objects.get(name="c++"))
    gameProgrammingLanguage.save()
    gameProgrammingLanguage = GameProgrammingLanguage(game=Game.objects.get(
        name="grand theft auto v"), programmingLanguage=ProgrammingLanguage.objects.get(name="c++"))
    gameProgrammingLanguage.save()
    gameProgrammingLanguage = GameProgrammingLanguage(game=Game.objects.get(
        name="super mario bros. wonder"), programmingLanguage=ProgrammingLanguage.objects.get(name="c++"))
    gameProgrammingLanguage.save()
    gameProgrammingLanguage = GameProgrammingLanguage(game=Game.objects.get(
        name="the legend of zelda breath of the wild"), programmingLanguage=ProgrammingLanguage.objects.get(name="c++"))
    gameProgrammingLanguage.save()
    gameProgrammingLanguage = GameProgrammingLanguage(game=Game.objects.get(
        name="hollow knight"), programmingLanguage=ProgrammingLanguage.objects.get(name="c#"))
    gameProgrammingLanguage.save()
    gameProgrammingLanguage = GameProgrammingLanguage(game=Game.objects.get(
        name="assassin's creed 1"), programmingLanguage=ProgrammingLanguage.objects.get(name="c++"))
    gameProgrammingLanguage.save()
    gameProgrammingLanguage = GameProgrammingLanguage(game=Game.objects.get(
        name="far cry 5"), programmingLanguage=ProgrammingLanguage.objects.get(name="c++"))
    gameProgrammingLanguage.save()


create_developers()
create_franchises()
create_genres()
create_publishers()
create_programming_language()
create_game_engine()
create_games()
create_gamegenre()
create_game_programming_language()

