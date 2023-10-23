from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'base.html')

def about(request):
    return render(request,'pages/about.html')

def home(request, id=None):
    # If id is provided, you can use it in your view logic
    if id == 'my_projects':
        return render(request, 'pages/home.html', {'id': id})
    return render(request, 'pages/home.html')