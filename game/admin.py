from django.contrib import admin
from .models import Games, Genres, Review, GameEvents

admin.site.register(Games)
admin.site.register(Genres)
admin.site.register(Reviews)
admin.site.register(GameEvents)