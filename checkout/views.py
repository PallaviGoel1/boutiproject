from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key' : 'pk_test_51OZVcdKjqt1ZoBTg3rmOzIfb7psOjnlRY2jiG4MGBa881RS3bdGyciwt6sl3LvfGIrev166baXuN1EhHSeIRRwVV004rjbdeYg',
        'client_secret' : 'test client secret',
    }

    return render(request, template, context)