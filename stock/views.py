from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'fontend/index.html')
def about(request):
    return render(request, 'fontend/about.html')
def contact(request):
    return render(request, 'fontend/contact.html')