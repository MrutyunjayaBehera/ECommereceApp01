from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator


def index(request):
  products = Products.objects.all()

  # adding search functionality by geeting the user input value through 'name' attribute
  item_name = request.GET.get('item_name')
  if (item_name != " " and item_name is not None):
    products = Products.objects.filter(title__icontains=item_name)

  # pagination code
  paginator = Paginator(products, 4)
  page = request.GET.get('page')
  products = paginator.get_page(page)

  # contexts used to display objects on screen
  context = {'products': products}
  return render(request, 'ecommerce/index.html', context)


def detail(request, id):
  product_obj = Products.objects.get(id=id)
  context = {'product_obj': product_obj}
  return render(request, 'ecommerce/detail.html', context)
