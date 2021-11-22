from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home.html')


def adminS(request):
    return render(request, 'admin.html')

def login(request):
    return render(request, 'login.html')