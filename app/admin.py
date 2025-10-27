from django.contrib import admin
from .models import Cooking,Post,Category

admin.site.register(Category)
admin.site.register(Cooking)
admin.site.register(Post)
