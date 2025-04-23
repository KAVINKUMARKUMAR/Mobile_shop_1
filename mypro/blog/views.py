from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from django.views.generic import DetailView,UpdateView,DeleteView,ListView,CreateView
from .models  import Product
from .forms import AddProductForm
# Create your views here.
def baseview(request):
    template = loader.get_template('base.html')
    context = {
        
    }
    return HttpResponse(template.render(context,request))
def homeview(request):
    template = loader.get_template('home.html')
    context = {
        'products' : Product.objects.all()
    }
    return HttpResponse(template.render(context,request))


class Productdetial(DetailView):
    model = Product
    template_name = 'product_detial.html'

class AddProduct(CreateView):
    model = Product
    template_name = 'add_product.html'
    form_class = AddProductForm
    success_url = '/'
class EditProduct(UpdateView):
    model = Product
    context_object_name = 'product'
    template_name = 'edit_prod.html'
    fields = ['name','img','price','stock']
    success_url = '/'
class DeleteProduct(DeleteView):
    model = Product
    template_name = 'del_prod.html'
    success_url = '/'

    
