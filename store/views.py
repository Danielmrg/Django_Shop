from django.shortcuts import render , HttpResponse , redirect , get_object_or_404 , get_list_or_404
from django.contrib.auth.models import User , Group
from django.views.generic import *
from .filters import *
from .models import *



# Create your views here.
#category__in=Category's

def home(request):
    category_s=Categorys.objects.all()
    products=Item.objects.all()
    context={
        'allcategory':category_s,
        'products':products,
    }
    return render(request, 'test/index.html',context)

def store(request):

    context={

    }
    return render(request, 'test/store.html',context)

class ItemListView(ListView):
    model = Item
    template_name = "test/teststore.html"
    context_object_name = "obj"
    queryset = Item.objects.order_by('-date_created')
    paginate = 1
    
    def get_context_data(self, **kwargs):
        context = super(ItemListView, self).get_context_data(**kwargs)
        context['test']=Categorys.objects.all()
        qs = self.model.objects.all()
        context['obj']=ProductFilter(self.request.GET, queryset=qs)
        return context

    def get_queryset(self):
        qs = self.model.objects.all()
        product_filtered_list = ProductFilter(self.request.GET, queryset=qs)
        return product_filtered_list
    


def detail(request,id,slug):

    return HttpResponse('page detail:<br> product by id:{} and<br>slug:{}'.format(id,slug))

def detail_category(request):
    return HttpResponse('page detail_category')

def cart(request):
    return HttpResponse( 'page cart')

def profile(request):
    return HttpResponse('page profile')

def settings(request):
    return HttpResponse('page settings')

def update_info_order(request):
    return HttpResponse('page update')

def delete_of_cart(request):
    return HttpResponse('page delete')

def add_to_cart(request,id,slug):
    return HttpResponse( f'page add by id:{id} & slug:{slug}')

