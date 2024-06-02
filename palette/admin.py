from django.contrib.admin import register, ModelAdmin, TabularInline
from .models import Genre, Artwork


@register(Genre)
class GenreAdmin(ModelAdmin):
    list_display = ['id', 'name', 'slug', 'created']
    list_filter = ['id', 'name', 'created']
    prepopulated_fields = {'slug':['name']}

    
@register(Artwork)
class ArtworkAdmin(ModelAdmin):
    list_display = ['id', 'name', 'slug', 'image',
                    'description', 'height', 'width', 'artist',
                     'instagram_link', 'price', 'quantity', 'edition',
                      'is_available', 'genre', 'created', 'updated']
    list_filter = ['id', 'name', 'artist', 'price',
                   'edition', 'is_available', 'genre', 'created',
                    'updated']
    prepopulated_fields = {'slug':['name']}    