from django.db import models
from django.contrib.auth.models import User

class Games(models.Model):
    # fields for game title, release date, and game rating
    gametitle=models.CharField(max_length=255)
    releasedate=models.DateField()
    gamerating=models.CharField(max_length=255)

    def __str__(self):
        return self.gametitle
    
    class Meta:
        db_table='games'

class Genres(models.Model):
    # fields for genre id (foreign key), genre name (many-to-many)
    genreid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    genrename=models.TextField()
    
    def __str__(self):
        return self.genrename
    
    class Meta:
        db_table='genres'

class Reviews(models.Model):
    # fields for game reviews, date entered, user ID (foreign key), and description
    reviewtitle=models.CharField(max_length=255)
    dateentered=models.DateField()
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    reviewedescription=models.TextField()

    def __str__(self):
        return self.review
    
    class Meta:
        db_table='review'

class GameEvents(models.Model):
    # fields for game event title, location, date, time, description, user ID of member who posted it
    gameeventtitle=models.CharField(max_length=255)
    gameeventlocation=models.CharField(max_length=255)
    gameeventdate=models.DateField()
    gameeventtime=models.TimeField()
    gameeventdescription=models.TextField()
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.gameeventtitle

    class Meta:
        db_table='gameevent'

    
