import random
import json
import socket
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import NavServer, Container
from .forms import ImageForm, VNCForm, JabberForm


def rand_n_digits(num_digits):
    """ Generates a random integer with n digits """
    range_start = 10**(num_digits-1)
    range_end = (10**num_digits) - 1
    return random.randint(range_start, range_end)


# Create your views here.
def start_page(request):
    """ Display start page """

    return render(request, 'dockernav/start.html', {})


@login_required
def container_new(request):
    """ Select a container """

    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            cont = form.save(commit=False)
            cont.user = request.user
            cont.rand_int = rand_n_digits(9)

            server_list = NavServer.objects.all()
            server = server_list[random.randint(0, len(server_list)-1)]
            cont.navserver = server

            cont.save()

            if cont.image == 'vnc':
                return redirect('new_vnc', cont_pk=cont.pk, nav_pk=server.pk)
            elif cont.image == 'jabber':
                return redirect('new_jabber', cont_pk=cont.pk, nav_pk=server.pk)
    else:
        form = ImageForm()

    return render(request, 'dockernav/new_container.html', {'form': form})


def vnc_new(request, cont_pk, nav_pk):
    """ Create a new VNC image """

    vnc = get_object_or_404(Container, pk=cont_pk)
    nav_server = get_object_or_404(NavServer, pk=nav_pk)

    if request.method == 'POST':
        form = VNCForm(request.POST, instance=vnc)
        if form.is_valid():
            vnc = form.save(commit=False)
            vnc.user = request.user
            vnc.navserver = nav_server
            vnc.save()
            return redirect('start_page')
    else:
        form = VNCForm()

    return render(request, 'dockernav/new_vnc.html', {'form': form})


def jabber_new(request, cont_pk, nav_pk):
    """ Create a new Jabber image """

    jabber = get_object_or_404(Container, pk=cont_pk)
    nav_server = get_object_or_404(NavServer, pk=nav_pk)

    if request.method == 'POST':
        form = JabberForm(request.POST, instance=jabber)
        if form.is_valid():
            jabber = form.save(commit=False)
            jabber.jabber_ip = nav_server.host
            jabber.user = request.user
            jabber.navserver = nav_server
            jabber.save()
            return redirect('start_page')
    else:
        form = JabberForm()

    return render(request, 'dockernav/new_jabber.html', {'form': form})
