from django.urls import path
from .views import artwork_list, artwork_detail


app_name = 'palette'

urlpatterns = [
    path('', artwork_list, name='artwork-list'),
    path('<slug:genre_slug>/', artwork_list, name='artwork-list-genre'),
    path('<int:id>/<slug:slug>/', artwork_detail, name='artwork-detail'),
]
