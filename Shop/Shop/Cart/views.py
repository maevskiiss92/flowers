from django.shortcuts import render, redirect
from django.views import View
from Main.models import Flowers
from .Cart import Cart
# Create your views here.

class CartView(View):
    def get(self, request):
        html = 'Cart.html'
        cart = Cart(request)
        context = {'cart': cart}
        return render(request, html, context)

    def post(self, request):
        data = request.POST
        cart = Cart(request)

        if 'buy' in request.POST:
            cart.buy()
            return redirect('catalog')
        else:
            flowers = data.getlist('flower')
            quantity = data.getlist('quantity')

            cart.edit(flowers, quantity)

            return redirect('cart')