from django.urls import path
from .import views
urlpatterns = [path('',views.index,name='index'),
               path('counter/',views.counter,name='counter'),
               path('splitting/',views.splitting,name="splitting"),
               path('removepunc/',views.removepunc,name='removepunc'),
               path('about/',views.about,name='about'),
               path('contact/',views.contact,name='contact')]