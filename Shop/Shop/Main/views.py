from django.shortcuts import render, redirect
from django.views import View
from .models import Flowers
from Cart.Cart import Cart
from .forms import SimpleForm
# Create your views here.

class CatalogView(View):

    def get(self, request):
        html = 'Catalog.html'
        flowers = Flowers.objects.all()
        form = SimpleForm()
        cart = Cart(request)

        print(request.session['cart'])
        context = {'flowers': flowers,
                   'cart': cart,
                   'form': form}
        return render(request, html, context)

    def post(self, request):
        print(request.POST)
        flower = Flowers.objects.get(name = request.POST['flower'])
        quantity = float(request.POST['quantity'])
        cart = Cart(request)
        cart.add(flower, quantity)
        print(cart)
        return redirect('catalog')

class FlowerDetailView(View):

    def get(self, request, slug):
        flower = Flowers.objects.get(slug=slug)
        context = {'flower': flower}
        html = 'Flower.html'
        return render(request, html, context)