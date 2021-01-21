"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
        'title': 'Register Page',
        'year': datetime.now().year,
        }
    return render(request, 'app/register.html', context)


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def myview(request):
    assert isinstance(request, HttpRequest)
    template = 'app/my.html'
    context = {
                'title':'MyView',
                'message':'MyTestView',
                'year':datetime.now().year,
        }

    return render(request, template, context)

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    context = {
                'title':'Contact',
                'message':'Your contact page.',
                'year':datetime.now().year,
              }
    return render(
        request,
        'app/contact.html',
        context
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
