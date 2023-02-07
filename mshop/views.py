from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product
from .forms import CommentsForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ImproperlyConfigured

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from django.db.models import Q

class ProductList(ListView):
    model=Product
    template_name='mshop/shop_list.html'
    context_object_name='all_products'
    

class ProductDetail(DetailView, FormMixin):
    model=Product
    template_name='mshop/shop_detail.html'
    form_class=CommentsForm
    context_object_name='product'
    success_url= reverse_lazy('shop')


    def post(self,request,*args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.product=self.get_object()
        self.object.save()
        return super().form_valid(form)


class Register(CreateView):
    template_name='registration/register.html'
    form_class=UserCreationForm
    success_url=reverse_lazy('successreg')

    def get_success_url(self):
        if not self.success_url:
            raise ImproperlyConfigured("NO url to redirect")
        return str(self.success_url)


    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)
	    

def Success(request):
    return render(request, 'registration/success.html')


def Homepage(request):
    return render(request, 'home.html')



class SearchResultsView(ListView):
    model = Product
    template_name = "search_results.html"

    def get_queryset(self): # new
        return Product.objects.filter(
            Q(name__icontains="Boston") | Q(state__icontains="NY")
        )
        