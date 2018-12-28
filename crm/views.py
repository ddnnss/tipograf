from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from client.models import Client
from order.models import Order
from customuser.models import User
from order.forms import NewOrderForm

@login_required
def index(request):
    if request.POST:
        form = NewOrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # do something.
        else:
            new_order_form = NewOrderForm()

        return HttpResponseRedirect('/crm/')


    all_orders = Order.objects.all()
    new_order_form = NewOrderForm()

    return render(request, 'crm/index.html', locals())

