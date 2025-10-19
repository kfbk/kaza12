from django.shortcuts import render
from django.views.generic import TemplateView, View,ListView
from app.models import Cooking
from .models import Post

# class IndexView(TemplateView):
#     template_name = "app/index.html"
# class IndexView(ListView):
class IndexView(View):
    model = Post
    ordering = '-id'
    context_object_name = 'posts'   # HTMLに渡す
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.all()
        return render(request, 'app/index.html', {
            'post_data': post_data,
        })

class CookingView(View):
    def get(self, request, *args, **kwargs):
        cooking_data = Cooking.objects.all()

        return render(request, 'app/cooking.html', {
            'cooking_data': cooking_data,
        })

class ShopView(TemplateView):
    template_name = "app/shop.html"
