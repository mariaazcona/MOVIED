from django.contrib import admin
from .models import Title, Award, Genre, Name, Budget, Rating

# Register your models here.
admin.site.register(Title)
admin.site.register(Award)
admin.site.register(Genre)
admin.site.register(Name)
admin.site.register(Budget)
admin.site.register(Rating)
