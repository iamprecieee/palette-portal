from django.db.models import (Model, CharField, SlugField, DateTimeField,
                              Index, ImageField, PositiveIntegerField, URLField,
                              DecimalField, TextField, BooleanField, TextChoices,
                              ForeignKey, CASCADE)
from django.db.models.manager import Manager
from django.urls import reverse


# Custom manager for retrieving only available artworks.
class AvailableManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)


class Genre(Model):
    name = CharField(max_length=250, unique=True)
    slug = SlugField(max_length=250)
    created = DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
        indexes = [
            Index(fields=['slug']),
            Index(fields=['name']),
        ]
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('palette:artwork-list-genre', args=[self.slug])
    
    
    
class Artwork(Model):
    class Edition(TextChoices):
        LIMITED = ('LT', 'limited')
        OPEN = ('OP', 'open')
        SINGULAR = ('SI', '1/1')
        
    name = CharField(max_length=250, unique=True)
    slug = SlugField(max_length=250)
    image = ImageField(upload_to='images/')
    description = TextField(max_length=255, blank=True)
    height = PositiveIntegerField(blank=True, null=True)
    width = PositiveIntegerField(blank=True, null=True)
    artist = CharField(max_length=250)
    instagram_link = URLField(max_length=255, blank=True)
    price = DecimalField(max_digits=9, decimal_places=2,
                         blank=True, null=True)
    quantity = PositiveIntegerField(default=1)
    edition = CharField(max_length=2, choices=Edition.choices, 
                     default=Edition.OPEN)
    is_available = BooleanField(default=True)
    genre = ForeignKey(Genre, related_name='artworks',
                       on_delete=CASCADE)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)
    
    objects = Manager()
    available = AvailableManager()
    
    class Meta:
        ordering = ['-created']
        indexes = [
            Index(fields=['id', 'slug']),
            Index(fields=['name']),
            Index(fields=['is_available']),
            Index(fields=['edition']),
        ]
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('palette:artwork-detail', args=[self.id, self.slug])
    