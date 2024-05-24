from django.contrib import admin

from filmy.models import Movie, Director, Genre, Actor


class MovieAdmin(admin.ModelAdmin):
    pass


class DirectorAdmin(admin.ModelAdmin):
    pass


class GenreAdmin(admin.ModelAdmin):
    pass


class ActorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Actor)

# Register your models here.