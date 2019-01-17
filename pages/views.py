from django.shortcuts import render

from volunteers.models import Volunteer
from pets.models import Pet


def index(request):
    pets = Pet.objects.order_by('-list_date').filter(is_published=True)[:4]

    context = {
        'pets': pets,
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all volunteers
    volunteers = Volunteer.objects.order_by('-hire_date')

    # Get MVP
    mvp_volunteer = Volunteer.objects.all().filter(is_mvp=True)

    context = {
        'volunteers': volunteers,
        'mvp_volunteer': mvp_volunteer
    }

    return render(request, 'pages/about.html', context)
