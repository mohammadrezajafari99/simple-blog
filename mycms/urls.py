from django.urls import path
from .views import detail,createpost,index,updatepost,deletepost,panel


urlpatterns = [
    path('', index,name='index'),
    path('panel',panel,name='panel'),
    path('article/<str:slug>',detail , name='detail'),
    path('create-post',createpost , name='create'),
    path('update-post/<str:slug>', updatepost,name='update'),
    path('delete-post/<str:slug>',deletepost,name='delete')
]
