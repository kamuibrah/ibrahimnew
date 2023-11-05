from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html') 

def manage_view(request):
    return render(request, 'manage.html') 

def client_view(request):
    return render(request, 'client.html')

def driver_view(request):
    return render(request, 'driver.html')

