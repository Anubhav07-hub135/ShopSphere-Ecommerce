from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .models import Product, Category, Order, OrderItem
from .cart import Cart


def product_list(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()

    query = request.GET.get('q')
    category_slug = request.GET.get('category')

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    if category_slug:
        products = products.filter(
            category__slug=category_slug
        )

    context = {
        'products': products,
        'categories': categories,
        'query': query,
        'selected_category': category_slug,
    }

    return render(
        request,
        'store/product_list.html',
        context
    )


def product_detail(request, slug):
    product = get_object_or_404(
        Product,
        slug=slug,
        available=True
    )

    recommended_products = Product.objects.filter(
        category=product.category,
        available=True
    ).exclude(
        id=product.id
    )[:4]

    context = {
        'product': product,
        'recommended_products': recommended_products,
    }

    return render(
        request,
        'store/product_detail.html',
        context
    )


def cart_detail(request):
    cart = Cart(request)

    return render(
        request,
        'store/cart_detail.html',
        {
            'cart': cart
        }
    )


def cart_add(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(
        Product,
        id=product_id,
        available=True
    )

    if product.stock > 0:
        cart.add(
            product=product,
            quantity=1
        )

    return redirect('cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(
        Product,
        id=product_id
    )

    cart.remove(product)

    return redirect('cart_detail')


def cart_increase(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(
        Product,
        id=product_id
    )

    current_quantity = cart.cart.get(
        str(product.id),
        {}
    ).get('quantity', 0)

    if current_quantity < product.stock:
        cart.add(
            product=product,
            quantity=1
        )

    return redirect('cart_detail')


def cart_decrease(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(
        Product,
        id=product_id
    )

    product_id_string = str(product.id)

    if product_id_string in cart.cart:
        current_quantity = cart.cart[
            product_id_string
        ]['quantity']

        if current_quantity > 1:
            cart.cart[
                product_id_string
            ]['quantity'] -= 1

            cart.save()

        else:
            cart.remove(product)

    return redirect('cart_detail')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('product_list')

    else:
        form = UserCreationForm()

    return render(
        request,
        'store/register.html',
        {
            'form': form
        }
    )


def checkout(request):
    cart = Cart(request)

    if len(cart) == 0:
        return redirect('cart_detail')

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        address = request.POST.get('address', '').strip()

        if name and email and phone and address:

            if request.user.is_authenticated:
                user = request.user
            else:
                user = None

            order = Order.objects.create(
                user=user,
                name=name,
                email=email,
                phone=phone,
                address=address
            )

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )

            cart.clear()

            return render(
                request,
                'store/order_success.html',
                {
                    'name': name,
                    'order': order
                }
            )

    return render(
        request,
        'store/checkout.html',
        {
            'cart': cart
        }
    )