from django.conf import settings
from Main.models import Flowers
from decimal import Decimal

class Cart(object):
    def __init__(self, request):
        # initializing cart
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # saving cart to session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def is_not_empty(self):
        return True if len(self.cart) > 0 else False

    def check_storage(self, flower, quantity):
        flower = Flowers.objects.get(name=flower)
        if int(quantity) >= int(flower.quantity):
            return flower.quantity
        else:
            return quantity



    def add(self, flowers, quantity=1):
        flower_name = str(flowers.name)
        quantity = self.check_storage(flower_name, quantity)
        if flower_name not in self.cart:
            self.cart[flower_name] = {'quantity': quantity,
                                      'price': float(flowers.price)}
        else:
            self.cart[flower_name]['quantity'] += int(quantity)

        self.cart[flower_name]['quantity'] = int(self.cart[flower_name]['quantity'])
        self.save()

    def edit(self, flowers, quantity):
        index = 0
        for flower in flowers:
            current_quantity = self.check_storage(flower, quantity[index])
            self.cart[flower]['quantity'] = current_quantity
            index += 1
        self.save()


    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, flowers):
        flower_name = str(flowers.name)
        if flower_name in self.cart:
            del self.cart[flower_name]
            self.save()

    def total_price(self):
        total_price = 0
        for el in self.cart:
            total_price += float(self.cart[el]['quantity']) * float(self.cart[el]['price'])
        return total_price

    def total_quantity(self):
        cart_quantity = 0
        for el in self.cart:
            cart_quantity += int(self.cart[el]['quantity'])
        return cart_quantity

    def buy(self):
        for el in self.cart:
            flower = Flowers.objects.get(name = el)
            flower.quantity -= int(self.cart[el]['quantity'])
            flower.save()
        self.cart.clear()
        self.save()

    def __iter__(self):
        flower_names = self.cart.keys()
        flowers = Flowers.objects.filter(name__in = flower_names)

        for flower in flowers:
            self.cart[str(flower.name)]['flower'] = flower

        for item in self.cart.values():
            item['total_price'] = float(item['quantity']) * float(item['price'])
            yield item