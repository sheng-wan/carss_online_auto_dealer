from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check password
        if password == password2:
            # check if username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, ' The username is already taken.')
                return redirect('register')
            else:
                # check if email already exists
                if User.objects.filter(email=email).exists():
                    messages.error(
                        request, ' The email is already registered.')
                    return redirect('register')
                else:
                    # all checked, create user
                    user = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=password
                    )
                    user.save()
                    # login after register
                    auth.login(request, user)
                    messages.success(
                        request, ' Welcome to Carss, ' + first_name)
                    return redirect('dashboard')
        else:
            # if passwords not match, return error message
            messages.error(request, ' The passwords entered do not match.')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    # get values
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authenticate user
        user = auth.authenticate(
            username=username,
            password=password
        )

        # correct credentials
        if user is not None:
            auth.login(request, user)
            messages.success(request, ' Welcome back, ' + user.first_name)
            return redirect('dashboard')
        else:
            # incorrect credentials
            messages.error(request, ' invalid credentials.')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('index')


def dashboard(request):
    # render contacted listings
    user_contacts = Contact.objects.order_by(
        '-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }

    return render(request, 'accounts/dashboard.html', context)
