from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import OrderForm, MakePaymentForm
from django.utils import timezone
from gallery.models import Photo
from .models import Order
import stripe
from django.contrib import messages

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET


def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Photo, pk=id)
                total += quantity * product.price
                Order = Order(order=order, product=product, quantity=quantity)
                Order.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )

            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('gallery'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    return render(request, "checkout/checkout.html",
                  {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})