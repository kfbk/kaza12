from django.contrib.sitemaps import Sitemap
from django.urls import reverse

# 動的の場合（このファイルはappに移動する）
# from .models import OnCount  # サイトマップ作成に使用するモデル名
 
# class OnCountSitemap(Sitemap):
#     def items(self):
#         return OnCount.objects.all()
 
#     def location(self, item):
#         return reverse('index', args=[item.id])

# 静的の場合
class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'
    # サイトマップに含めたいオブジェクトのリストを返します。
    def items(self):
        # [ ]の左側は urls.py (setting.py側) のnamespace、右側は urls.py(アプリ側)のnameを設定する。
        # return ['kuso:app']
        return [
            {'url':'/','changefreq': 'monthly', 'priority': 0.5},
        ]
    # 各オブジェクトのURLを生成します。
    def location(self, item):
        return reverse(item)