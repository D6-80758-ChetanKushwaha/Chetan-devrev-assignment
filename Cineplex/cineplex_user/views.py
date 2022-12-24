from django.shortcuts import render, redirect
from .models import Movie, Buy
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# from django.http import HttpResponse
# Create your views here.

def home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        # data = Movie.objects.filter(title__icontains=q)
        multiple_q = Q(Q(title__icontains=q) | Q(date__icontains=q))
        data = Movie.objects.filter(multiple_q)
    else:
        data = Movie.objects.all()

    context = {
        'movies': data
    }
    return render(request, 'cineplex_user/home.html',context)

def login(request):
    return render(request, 'cineplex_user/login.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username} Now you are able to log in!!")
            return redirect('user-login')

    else:    
        form = UserCreationForm()

    return render(request, 'cineplex_user/signup.html',{'form':form})

@login_required
def profile(request):
    context = {
        "buys":Buy.objects.all()
    }
    return render(request, 'cineplex_user/profile.html',context)