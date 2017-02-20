from django.shortcuts import render

# Create your views here.
def container_select(request):
    return render(request, 'dockernav/container_select.html', {})
