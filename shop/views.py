from django.shortcuts import render,redirect
from .models import Coffee, Order, OrderItem, Review

def home(request):
    coffees = Coffee.objects.all()
    return render(request, 'home.html', {'coffees': coffees})


def coffee_detail(request, id):
    coffee = Coffee.objects.get(id=id)
    return render(request, 'coffee_detail.html', {'coffee': coffee})

def add_to_cart(request, id):
    cart = request.session.get('cart', {})

    cart[id] = cart.get(id, 0) + 1

    request.session['cart'] = cart
    return redirect('cart')


def cart(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for coffee_id, qty in cart.items():
        coffee = Coffee.objects.get(id=coffee_id)
        subtotal = coffee.price * qty
        total += subtotal
        items.append({'coffee': coffee, 'qty': qty, 'subtotal': subtotal})

    return render(request, 'cart.html', {'items': items, 'total': total})

def checkout(request):
    if not request.user.is_authenticated:
        return redirect('/admin')  # simple login

    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart')

    total = 0
    order = Order.objects.create(user=request.user, total_price=0)

    for coffee_id, qty in cart.items():
        coffee = Coffee.objects.get(id=coffee_id)
        subtotal = coffee.price * qty
        total += subtotal
        OrderItem.objects.create(order=order, coffee=coffee, quantity=qty)

    order.total_price = total
    order.save()

    request.session['cart'] = {}  # clear cart

    return redirect('order_success')

def order_success(request):
    return render(request, 'order_success.html')

def add_review(request, coffee_id):
    if request.method == 'POST':
        Review.objects.create(
            coffee_id=coffee_id,
            user=request.user,
            rating=request.POST['rating'],
            comment=request.POST['comment']
        )
    return redirect('coffee_detail', id=coffee_id)
