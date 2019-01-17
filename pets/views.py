from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .choices import gender_choices, age_choices, size_choices

from .models import Pet


def index(request):
    queryset_list = Pet.objects.order_by(
        '-list_date').filter(is_published=True)

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # Gender
    if 'gender' in request.GET:
        gender = request.GET['gender']
        if gender:
            queryset_list = queryset_list.filter(gender__iexact=gender)

    # Age
    if 'age' in request.GET:
        age = request.GET['age']
        if age:
            queryset_list = queryset_list.filter(age__lte=age)

    # Size
    if 'size' in request.GET:
        size = request.GET['size']
        if size:
            queryset_list = queryset_list.filter(size__iexact=size)

    paginator = Paginator(queryset_list, 6)
    page = request.GET.get('page')
    paged_pets = paginator.get_page(page)

    context = {
        'pets': paged_pets,
        'gender_choices': gender_choices,
        'age_choices': age_choices,
        'size_choices': size_choices,
        'values': request.GET
    }

    return render(request, 'pets/pets.html', context)


def pet(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)

    context = {
        'pet': pet
    }

    return render(request, 'pets/pet.html', context)
