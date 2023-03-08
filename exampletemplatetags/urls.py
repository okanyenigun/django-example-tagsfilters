from django.contrib import admin
from django.urls import path
from home.views import home_view, hello, cycle_view, product_list,tag_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('hello/<name>/', hello, name='hello'),
    path('cycle/', cycle_view, name='cycle'),
    path('product/',product_list, name="product"),
    path('tags/',tag_view, name="tags"),
]
