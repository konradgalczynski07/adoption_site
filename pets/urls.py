from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='pets'),
    path('<int:pet_id>', views.pet, name='pet'),
]
