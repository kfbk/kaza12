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
        # post_data = Post.objects.all()
        post_data = Post.objects.order_by('-id')[:5]
        return render(request, 'app/index.html', {
            'post_data': post_data,
        })

class CookingView(View):
    def get(self, request, *args, **kwargs):
        cooking_data = Cooking.objects.all()
        agemono_data = Cooking.objects.filter(category__name='揚げ物')
        sasimi_data = Cooking.objects.filter(category__name='刺身')
        tumami_data = Cooking.objects.filter(category__name='おつまみ')
        yakimono_data = Cooking.objects.filter(category__name='焼き物')
        nikomi_data = Cooking.objects.filter(category__name='煮込み・ご飯もの')
        seisyu_data = Cooking.objects.filter(category__name='清酒')
        beer_data = Cooking.objects.filter(category__name='ビール')
        syoutyu_data = Cooking.objects.filter(category__name='焼酎')
        bottle_data = Cooking.objects.filter(category__name='ボトル')
        drink_data = Cooking.objects.filter(category__name='お飲み物')
        # print(f'agemono_data={agemono_data}')
        return render(request, 'app/cooking.html', {
            'cooking_data': cooking_data,
            'agemono_data': agemono_data,
            'sasimi_data': sasimi_data,
            'tumami_data': tumami_data,
            'yakimono_data': yakimono_data,
            'nikomi_data': nikomi_data,
            'seisyu_data': seisyu_data,
            'beer_data': beer_data,
            'syoutyu_data': syoutyu_data,
            'bottle_data': bottle_data,
            'drink_data': drink_data,
        })

class ShopView(TemplateView):
    template_name = "app/shop.html"

class VideoView(TemplateView):
    template_name = "app/video.html"

def google_search_console(request):
    return render(request, 'google/google51925de0612ccd11.html')

def sitemap(request):
    return render(request, 'google/sitemap.xml')
