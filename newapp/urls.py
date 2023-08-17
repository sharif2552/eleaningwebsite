from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name  = 'newapp'


urlpatterns = [
    path('home/',views.home , name='home'),
    path('givetest/<int:category_id>',views.givetest ,name = 'givetest'),
    path('add_category/', views.add_category , name = 'add_category'),
    path('add_test/', views.add_test , name= 'add_test'),

    path('add_question/', views.add_question, name='add_question'),
    path('add_question/<int:categories>/', views.add_question, name='add_question'),
    path('test_category_filter/', views.test_category_filter, name='test_category_filter'),
    path('add_article/', views.add_article, name='add_article'),
    path('forum/', views.forum, name='forum'),
    path('all_article/', views.all_article, name='all_article'),

    path('forum/', views.forum, name='forum'),





    

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)