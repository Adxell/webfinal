from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/account/login/')
def index(request):
    return render(request, 'home.html')


def adminS(request):
    return render(request, 'admin.html')

def login(request):
    return render(request, 'registration/login.html')