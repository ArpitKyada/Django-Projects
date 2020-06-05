from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),

    path('show_desktop', views.show_desktop, name="show_desktop"),
    path('show_laptop', views.show_laptop, name="show_laptop"),
    path('show_mobile', views.show_mobile, name="show_mobile"),

    path('create_desktop', views.create_desktop, name="create_desktop"),
    path('create_laptop', views.create_laptop, name="create_laptop"),
    path('create_mobile', views.create_mobile, name="create_mobile"),

    path('update_desktop/<id>', views.update_desktop, name="update_desktop"),
    path('update_laptop/<id>', views.update_laptop, name="update_laptop"),
    path('update_mobile/<id>', views.update_mobile, name="update_mobile"),

    path('delete_desktop/<id>', views.delete_desktop, name="delete_desktop"),
    path('delete_laptop/<id>', views.delete_laptop, name="delete_laptop"),
    path('delete_mobile/<id>', views.delete_mobile, name="delete_mobile"),
]
