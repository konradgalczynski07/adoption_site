from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from pets.models import Pet
# from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        pet = request.POST['pet']
        pet_instance = Pet.objects.get(pk=pet)
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(pet=pet_instance, name=name,
                          email=email, phone=phone, message=message)

        contact.save()

        # Send email
        # send_mail(
        #   'Inquiry of Pet',
        #   'There has been an inquiry for ' + pet + '. Sign into the admin panel for more info',
        #   'mail@gmail.com',
        #   [volunere_email, 'mail@gmail.com'],
        #   fail_silently=False
        # )

        return redirect('/pets/'+pet)
