from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from web.models import Category, Product, Profile, Cart, Wishlist
from django.contrib.auth.decorators import login_required
from web.forms import CreateUserForm, ProfileForm



def index(request):
    categories_of_men = Category.objects.filter(gender='M')
    categories_of_women = Category.objects.filter(gender='W')
    product = Product.objects.order_by('-buy_count')[:4]
    new_arrival = Product.objects.order_by('-date_time')[:6]
    user_wishlist = []
    profile = None
    if request.user.is_authenticated:
        profile, created = Profile.objects.get_or_create(user=request.user)
        user_wishlist = Wishlist.objects.filter(user=request.user).values_list('product_id', flat=True)

    return render(request,"index.html",{'categories_of_men' : categories_of_men, 'categories_of_women' : categories_of_women,  'user_wishlist':user_wishlist, 'product':product, 'new_arrival':new_arrival, 'profile':profile})


def registerPage(request):
    
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
        

    return render(request, 'accounts/register.html', {'form':form})

@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('web:account')  
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'upload_photo.html', {'form': form})

def logoutPage(request):
    logout(request)
    return redirect('login')

def accountPage(request):
    if request.user.is_authenticated:
        profile, created = Profile.objects.get_or_create(user=request.user)
        return render(request, 'accounts/accounts.html', {'profile': profile})
    else:
        return redirect('login')

def categoryPage(request, category_id):
    category = Category.objects.get(id=category_id)
    product = Product.objects.filter(category=category)
    user_wishlist = []
    if request.user.is_authenticated:
        user_wishlist = Wishlist.objects.filter(user=request.user).values_list('product_id', flat=True)
    return render(request, 'category.html', {'category' : category, 'products' : product, 'user_wishlist':user_wishlist})

def productPage(request, product_id):
    product = Product.objects.get(id=product_id)
    same_category = Product.objects.filter(category=product.category )
    all_product = Product.objects.all()
    if request.user.is_authenticated:
        user_wishlist = Wishlist.objects.filter(user=request.user).values_list('product_id', flat=True)
    else:
        user_wishlist = []

    return render(request, 'product.html', {'product' : product, 'same_category' : same_category, 'all_product':all_product, 'user_wishlist':user_wishlist })

@login_required
def wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)

    if not created:
        wishlist_item.delete()  

    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def wishlistPage(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    user_wishlist = Wishlist.objects.filter(user=request.user).values_list('product_id', flat=True)


    return render(request, 'wishlist.html', {'wishlist_items':wishlist_items, 'user_wishlist': user_wishlist,})



@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    Cart.objects.get_or_create(user=request.user, product=product)
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def cartPage(request):
    cart_items = Cart.objects.filter(user=request.user)
    user_wishlist = Wishlist.objects.filter(user=request.user).values_list('product_id', flat=True)
    return render(request, 'cart.html', {'cart_items':cart_items, 'user_wishlist': user_wishlist,})