from django.urls import re_path
from todo import views 
 
urlpatterns = [ 
    re_path(r'^$', views.handle_todo_list),
    re_path(r'^(?P<pk>[0-9]+)$', views.handle_todo_item),
]