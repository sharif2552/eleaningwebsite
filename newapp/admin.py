from django.contrib import admin
from .models import Question, test , Category, Article


# Register your models here.
admin.site.register(Question)
admin.site.register(test)
admin.site.register(Category)
admin.site.register(Article)
