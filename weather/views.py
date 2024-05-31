from django.shortcuts import render

# Create your views here.

def weathpage(request):
    return render(request, 'weatherpage.html')