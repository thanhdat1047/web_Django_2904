from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.


def register(request):
    form = CreateUserForm()
    # neu req tro toi pthuc Gui
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # form co gia tri nhap vao thoa man dk.
            form.save()
    context = {'form': form}
    return render(request, 'app/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None: 
            login(request,user)
            return redirect('home')
        else : 
            messages.info(request,'user or password not correct!')
    context = {}
    return render(request, 'app/login.html', context)
def logoutPage(request):
    logout(request)
    return redirect('login')


def home(request):
    if request.user.is_authenticated:  # user dang nhap r
        customer = request.user.customer
        order, create = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'app/home.html', context)


def cart(request):
    if request.user.is_authenticated:  # user dang nhap r
        customer = request.user.customer
        order, create = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'app/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:  # user dang nhap r
        customer = request.user.customer
        order, create = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'app/checkout.html', context)


def updateItem(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError as e:
        data = {}

    productId = data['productId']
    action = data['action']
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, create = Order.objects.get_or_create(
        customer=customer, complete=False)
    orderItem, create = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quatity += 1
    elif action == 'remove':
        orderItem.quatity -= 1
    orderItem.save()

    if orderItem.quatity <= 0:
        orderItem.delete()

    return JsonResponse('added', safe=False)
