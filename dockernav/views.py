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


@login_required
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

            # Set up for connection to navlistener
            HOST = nav_server.host
            PORT = nav_server.port
            vnc_dict = {'action': 'start',  'rand_int': vnc.rand_int,
                        'image': 'wallace123/docker-vnc',
                        'vncpass': vnc.vnc_pass}
            data = json.dumps(vnc_dict)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            try:
                sock.connect((HOST, PORT))
                sock.send(data)
                recv = sock.recv(1024)
            finally:
                sock.close()

            # Save received data to database
            recv_dict = json.loads(recv)
            vnc.category = recv_dict['category']
            vnc.loop_file = recv_dict['loop_file']
            vnc.dservice = recv_dict['dservice']
            vnc.dockerd = recv_dict['dockerd']
            vnc.device = recv_dict['device']
            vnc.port = recv_dict['port']
            vnc.docker_run = recv_dict['docker_run']
            vnc.docker_lib = recv_dict['docker_lib']
            vnc.docker_bridge = recv_dict['docker_bridge']
            vnc.mount_point = recv_dict['mount_point']
            vnc.container = recv_dict['container']
            vnc.dservice_path = recv_dict['dservice_path']
            vnc.docker = recv_dict['docker']

            vnc.save()
            return redirect('start_page')
    else:
        form = VNCForm()

    return render(request, 'dockernav/new_vnc.html', {'form': form})


@login_required
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

            # Set up for connection to navlistener
            HOST = nav_server.host
            PORT = nav_server.port
            jabber_dict = {'action': 'start',  'rand_int': jabber.rand_int,
                          'image': 'wallace123/docker-jabber',
                          'jabber_ip': jabber.jabber_ip,
                          'user1': jabber.user1, 'pass1': jabber.pass1,
                          'user2': jabber.user2, 'pass2': jabber.pass2}
            data = json.dumps(jabber_dict)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            try:
                sock.connect((HOST, PORT))
                sock.send(data)
                recv = sock.recv(1024)
            finally:
                sock.close()

            # Save received data to database
            recv_dict = json.loads(recv)
            jabber.category = recv_dict['category']
            jabber.loop_file = recv_dict['loop_file']
            jabber.dservice = recv_dict['dservice']
            jabber.dockerd = recv_dict['dockerd']
            jabber.device = recv_dict['device']
            jabber.port = recv_dict['port']
            jabber.docker_run = recv_dict['docker_run']
            jabber.docker_lib = recv_dict['docker_lib']
            jabber.docker_bridge = recv_dict['docker_bridge']
            jabber.mount_point = recv_dict['mount_point']
            jabber.container = recv_dict['container']
            jabber.dservice_path = recv_dict['dservice_path']
            jabber.docker = recv_dict['docker']

            jabber.save()
            return redirect('start_page')
    else:
        form = JabberForm()

    return render(request, 'dockernav/new_jabber.html', {'form': form})


@login_required
def container_list(request):
    """ Displays active containers """

    containers = Container.objects.filter(user=request.user)

    return render(request, 'dockernav/active_containers.html',
                  {'containers': containers})


@login_required
def container_detail(request, cont_pk, nav_pk):
    """ Displays the details about a container """

    cont = get_object_or_404(Container, pk=cont_pk)
    nav_server = get_object_or_404(NavServer, pk=nav_pk)

    return render(request, 'dockernav/details.html',
                  {'cont': cont})
