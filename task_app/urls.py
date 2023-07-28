from django.urls import path,include
from django.http import HttpResponse
from . import views as ev

urlpatterns = [
    # path('',ev.home,name='home'),
    path('',ev.register,name='register'),
    path('my_login',ev.my_login,name='my_login'),
    path('user_logout/',ev.user_logout,name='user_logout'), 

    # - CRUD operations
    # - CREATE TASK
    path('createtask/',ev.createtask,name='createtask'),

    # - READ TASK
    path('viewtasks/',ev.viewtasks,name='viewtasks'),

    # - UPDATE TASK
    path('updatetask/<int:id>/',ev.updatetask,name='updatetask'),

    # - DELETE TASK
    path('deletetask/<int:id>/',ev.deletetask,name='deletetask'),
]