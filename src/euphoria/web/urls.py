from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index,registerPage,logoutPage, accountPage, categoryPage, productPage, wishlistPage, cartPage, add_to_cart, wishlist, upload_photo



app_name = "web"

urlpatterns = [
    path ('', index, name="home"),
    path('register/', registerPage, name="register"),
    path('logout/', logoutPage, name='logout'),
    path('account/', accountPage, name='account'),
    path('category/<int:category_id>/', categoryPage, name='category'),
    path('product/<int:product_id>/', productPage, name='product'),
    path('wish/<int:product_id>/', wishlist, name='wishlist'),
    path('wishlist/', wishlistPage, name='wishlistPage'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cartPage, name='cart'),
    path('upload/', upload_photo , name='upload_photo'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)