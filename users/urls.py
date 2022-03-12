from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_up/<str:ref_code>', views.sign_up, name='sign_up'),
    path('s_product/<int:id>/', views.single_product, name='single_product'),
    path('otp_login', views.otp_login, name='otp_login'),
    path('otp_check', views.otp_check, name='otp_check'),
    path('e_login', views.email_login, name='email_login'),
    path('logout', views.logoutView, name='logout'),
    path('blocked', views.block, name='block'),
    path('cart', views.add_to_cart, name='add_to_cart'),
    path('remove', views.remove, name='remove'),
    path('checkout', views.checkout, name='checkout'),
    path('proceed', views.proceed, name='proceed'),
    path('add_address', views.add_address, name='add_address'),
    # path('user_orders', views.user_orders, name='user_orders'),
    path('cancel/<int:id>', views.cancel, name='cancel'),
    path('profile', views.profile, name='profile'),
    path('order_return/<int:id>', views.order_return, name='order_return'),
    # path('cart', views.view_cart, name='cart'),
    path('rpay', views.rpay, name='rpay'),
    path('otp_l', views.otp_l, name='otp_l'),
    path('coupen', views.coupen, name='coupen'),
    path('filter', views.filter_shop_products, name='filter'),
    # path('remove_coupen', views.removeCoupen, name='remove_coupen'),
    path('buyNow/<str:id>/', views.buyNow, name='buyNow'),
    path('texting', views.texting, name='texting'),
]