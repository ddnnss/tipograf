from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from client.models import Client
from customuser.models import User
from order.forms import NewOrderForm

@login_required
def index(request):
    all_clients = Client.objects.all()
    new_order_form = NewOrderForm()
    return render(request, 'crm/index.html', locals())

