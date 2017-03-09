import random
from django.shortcuts import render
from .models import NavServer, Container


def rand_n_digits(num_digits):
    """ Generates a random integer with n digits """
    range_start = 10**(num_digits-1)
    range_end = (10**num_digits) - 1
    return random.randint(range_start, range_end)


# Create your views here.
def container_select(request):
    """ Select a container """

    if request.method == 'POST':
        form = ContainerForm(request.POST)
        if form.is_valid():
            cont = form.save(commit=False)

            cont.rand_int = rand_n_digits(9)
            cont.save()
    return render(request, 'dockernav/container_select.html', {})
