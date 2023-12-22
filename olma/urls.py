from django.urls import path
from .views import HomeView, ShopView, AboutView, GalleryView, ContactusView, ShopdetailView, CartView, CheckoutView, MyaccountView, WishlistView

app_name = 'olma'

urlpatterns = [
    path('', HomeView.as_view(), name="home_page"),
    path('shop/', ShopView.as_view(), name="shop_page"),
    path('about/', AboutView.as_view(), name="about_page"),
    path('gallery/', GalleryView.as_view(), name='gallery_page'),
    path('contact-us/', ContactusView.as_view(), name='contact_page'),
    path('shop-detail/', ShopdetailView.as_view(), name='shopdetail_page'),
    path('cart/', CartView.as_view(), name='cart_page'),
    path('checkout/', CheckoutView.as_view(), name='checkout_page'),
    path('my-account/', MyaccountView.as_view(), name='myaccount_page'),
    path('wishlist/', WishlistView.as_view(), name='wishlist_page'),
]