from django.urls import path
from . import views
from My_ToDo_app.views import todoView, addTodo, deleteTodo


# NO LEADING SLASHES
urlpatterns = [
    # path('', views.index, name='index'),
    path('todo/', todoView),
    path('addTodo/', addTodo),
    path('deleteTodo/<int:todo_id>/', deleteTodo),
]
