from django.http import Http404
from django.views.generic import ListView, DetailView

from cart.models import Cart

from django.shortcuts import render, get_object_or_404
# # Create your views here.
from .models import Product
# views to handle featured products
class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    queryset      = Product.objects.all().featured() #line 34
    template_name = "products/featured-detail.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()

   

   
# view ends here

 
# class based function
class ProductListView(ListView):
    # queryset      = Product.objects.all()
    template_name = "products/list.html"

# this gets the context for any query set or any view that is being done, it happens by default just like the code in line 17, this helps to remove reoeatedness
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

# function based view
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
        # 'qs': queryset
    }

    return render(request, "products/list.html", context)

# product detailed view
class ProductDetailSlugView(DetailView):
    queryset      = Product.objects.all() #line 34
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        # request = self.request
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = get_object_or_404(Product, slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("uhhhmmmm....")
        return instance


class ProductDetailView(DetailView):
    queryset      = Product.objects.all() #line 34
    template_name = "products/detail.html"

# this gets the context for any query set or any view that is being done, it happens by default just like the code in line 17, this helps to remove reoeatedness
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
# # another way apart from the object to use it delete line 34
#     def get_queryset(self, *args, **kwargs):
#         request = self.request
#         pk = self.kwargs.get('pk')
#         return Product.objects.filter(pk=pk)
    
    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get(pk=pk)
        if instance is None:
            raise Http404('product doesnt exist') 
        return instance


# function based view
def product_detail_view(request, pk=None, *args, **kwargs):
    # instance = Product.objects.get(pk=pk)
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('no product fits your search')
    #     raise Http404('product doesnt exist')
    # except:
    #     print('huh?')
    instance = Product.objects.get(pk=pk)
    if instance is None:
        raise Http404('product doesnt exist')
    # print(instance)
    # qs = Product.objects.filter(id=pk)
    # # print(qs)
    # if qs.exists() and qs.count() == 1: #counts the products in the queryset
    #     instance = qs.first()
    # else:
    #     raise Http404('product doesnt exist')

    context = {
        'object': instance
        # 'qs': queryset
    }

    return render(request, "products/detail.html", context)




















































# from django.http import Http404
# from django.views.generic import ListView, DetailView

# from django.shortcuts import render, get_object_or_404
# # Create your views here.
# from .models import Product


# # # a function to control featured product

# # class ProductFeaturedListView(ListView):
# #     template_name = "products/list.html"
   
# #     def get_queryset(self, *args, **kwargs):
# #         request = self.request
# #         return Product.objects.featured()

# # class ProductFeaturedDetailView(DetailView):
# #     # queryset      = Product.objects.all()
# #     template_name = "products/featured-detail.html"
   
# #     def get_queryset(self, *args, **kwargs):
# #         request = self.request
# #         return Product.objects.featured()
       


# # class based view
# class ProductListView(ListView):
#     queryset      = Product.objects.all()
#     template_name = "products/list.html"
   
#     def get_context_data(self, *args, **kwargs):
#         context = super(ProductListView, self).get_context_data(*args, **kwargs)
#         print(context)
#         return context

#     # def get_queryset(self, *args, **kwargs):
#     #     request = self.request
#     #     return Product.objects.all()

    

# # function based view
# def product_list_view(request):
#     queryset = Product.objects.all()
#     context = {
#         'object_list': queryset
#         # 'qs': queryset
#     }

#     return render(request, "products/list.html", context)

# # detailed view this allows for a product to be searched by name
# # class ProductDetailSlugView(DetailView):
# #     queryset = Product.objects.all() 
# #     template_name = "products/detail.html"
# # ends here

# # the function below shows the products with their details
# class ProductDetailView(DetailView):
#     # queryset = Product.objects.all() #line 32
#     template_name = "products/detail.html"

#     def get_context_data(self, *args, **kwargs):
#         context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
#         print(context)
#         return context

#     # def get_object(self, *args, **kwargs):
#     #     request = self.request
#     #     pk = self.kwargs.get('pk')
#     #     instance = Product.objects.get_by_id(pk)
#     #     raise Http404('product doesnt exist')
#     #     return(instance)

       
#     def get_queryset(self, *args, **kwargs):
#         #  another method for look up,to use it delete line 32
#         request = self.request
#         pk = self.kwargs.get('pk')
#         return Product.objects.filter(pk=pk)
# # function based view
# def product_detail_view(request, pk=None,*args, **kwargs):
#     # print(args)
#     # print(kwargs)
#     # queryset
#     # instance = Product.objects.get(pk=pk, featured=True) #id
#     # instance = Product.objects.get(pk=pk) #id
#     # instance = get_object_or_404(Product, pk=pk)
#     # try:
#     #     instance = Product.objects.get(id=pk)
#     # except Product.DoesNotExist:
#     #     print('no product fits your search')
#     #     raise Http404('product doesnt exist')
#     # except:
#     #     print('huh?')
#     instance  = Product.objects.get_by_id(pk)
#     # print(instance)
#     if instance == None:
#         raise Http404('product doesnt exist')
#     qs = Product.objects.filter(id=pk)
#     # print(qs)
#     if qs.exists() and qs.count() == 1:
#         instance = qs.first()
#     else:
#         raise Http404('product doesnt exist')

#     context = {
#         'object': instance
#     }








#     return render(request, "products/detail.html", context)
