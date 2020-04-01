from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail


def contact(request):
    # get form values
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        advisor_email = request.POST['advisor_email']

        # Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'You have already made a request for this listing.')
                return redirect('/listings/' + listing_id)

        contact = Contact(
            listing=listing,
            listing_id=listing_id,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id
        )

        contact.save()

        # Send email notification
        send_mail(
            # subject
            'Your Carss Test Drive Request',
            # message
            'Hi ' + name + ', we have received your test drive request for ' + \
            listing + '. A sales advisor will get back to you soon.',
            # from email
            'wandev.projects@gmail.com',
            # recipient_list
            ['wandev.projects@gmail.com', email],
            # error check
            fail_silently=True
        )

        messages.success(
            request, 'Your request has been submitted, a request confirmation is sent to your email. We will get back to you soon.')

        return redirect('/listings/' + listing_id)
