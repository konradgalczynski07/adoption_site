from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


def contact(request):
    if request.method == 'POST':
        pet_id = request.POST['pet_id']
        pet = request.POST['pet']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(pet=pet, pet_id=pet_id, name=name,
                          email=email, phone=phone, message=message)

        contact.save()

        # Send email
        # send_mail(
        #   'Inquiry of pet',
        #   'There has been an inquiry for ' + pet + '. Sign into the admin panel for more info',
        #   'mail@gmail.com',
        #   [volunere_email, 'mail@gmail.com'],
        #   fail_silently=False
        # )

        return redirect('/pets/'+pet_id)
