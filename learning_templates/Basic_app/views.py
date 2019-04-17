from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'Basic_app/index.html')

def other(request):
    return render(request,'Basic_app/other.html')

def relative_url(request):
    return render(request,'Basic_app/relative_url_templates.html')
