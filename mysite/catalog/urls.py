from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('instrument/<int:pk>/', views.instrument_detail, name='instrument_detail'),
    path('instrument/new/', views.instrument_new, name='instrument_new'),
    path('instrument/(<pk>\d+)/edit/', views.instrument_edit, name='instrument_edit'),
    path('bom/<int:pk>/', views.bom_detail, name='bom_detail'),
    path('bom/new/', views.bom_new, name='bom_new'),
    path('bom/(<pk>\d+)/edit/', views.bom_edit, name='bom_edit'),
    path('released_bom', views.released_boms, name='released_bom'),



    #create a BOM instrument list in which the model number can be cliked on to show details
    #create a way of editing BOMs by an authorized user.
    # After chosing the foreinkey the rest of the fields for instrumnet are automatically populated.

]