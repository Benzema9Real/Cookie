from . import views
from django.urls import path

urlpatterns = [path('', views.index),
               path('message/', views.my_view, name="chat"),
               path('setcookie/', views.setcookie, name="setcookie"),
               path('showcookie/', views.showcookie, name="showcookie"),
               path('set_cookie/', views.set_cookie, name="set_cookie"),
               path('show_counter/', views.show_counter, name="show_counter"),
                path('deletecookie/', views.deletecookie, name="deletecookie"),
               ]
