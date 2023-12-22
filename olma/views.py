from django.shortcuts import render
from django.views.generic import TemplateView

def home_page(request):
    return render(request, 'index.html',)

class HomeView(TemplateView):
    template_name = 'index.html'
class ShopView(TemplateView):
    template_name = 'shop.html'
class AboutView(TemplateView):
    template_name = 'about.html'
class GalleryView(TemplateView):
    template_name = 'gallery.html'
class ContactusView(TemplateView):
    template_name = 'contact-us.html'
class ShopdetailView(TemplateView):
    template_name = 'shop-detail.html'
class CartView(TemplateView):
    template_name = 'cart.html'
class CheckoutView(TemplateView):
    template_name = 'checkout.html'
class MyaccountView(TemplateView):
    template_name = 'my-account.html'
class WishlistView(TemplateView):
    template_name = 'wishlist.html'









