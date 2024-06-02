from django.shortcuts import render
from .models import Genre, Artwork


def artwork_list(request, genre_slug=None):
    ''' 
    If `genre_slug` is not provided, return all available artworks.
    Else return related genre and available artworks.
    Finally return `genre` to double as bool-check.
    '''
    genre = None
    genres = Genre.objects.all()
    artworks = Artwork.available.all()
    
    if genre_slug:
        genre = Genre.objects.filter(slug=genre_slug).first()
        artworks = Artwork.available.filter(genre=genre)
        
    return render(request, 'palette/artwork_list.html', {
        'genre': genre,
        'genres':genres,
        'artworks':artworks
    })
    

def artwork_detail(request, id, slug):
    artwork = Artwork.available.filter(id=id, slug=slug).first()
    
    return render(request, 'palette/artwork_detail.html', {'artwork':artwork})