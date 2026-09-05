from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path(
        '',
        views.product_list,
        name='product_list'
    ),

    path(
        'product/<slug:slug>/',
        views.product_detail,
        name='product_detail'
    ),

    path(
        'cart/',
        views.cart_detail,
        name='cart_detail'
    ),

    path(
        'cart/add/<int:product_id>/',
        views.cart_add,
        name='cart_add'
    ),

    path(
        'cart/remove/<int:product_id>/',
        views.cart_remove,
        name='cart_remove'
    ),

    path(
        'cart/increase/<int:product_id>/',
        views.cart_increase,
        name='cart_increase'
    ),

    path(
        'cart/decrease/<int:product_id>/',
        views.cart_decrease,
        name='cart_decrease'
    ),

    path(
    'register/',
    views.register,
    name='register'
),

path(
    'login/',
    auth_views.LoginView.as_view(
        template_name='store/login.html'
    ),
    name='login'
),

path(
    'logout/',
    auth_views.LogoutView.as_view(),
    name='logout'
),
path(
    'checkout/',
    views.checkout,
    name='checkout'
),
]