"""djangoCrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="inicio"),
    path('signup/', views.signup, name="inscribiser"),
    path('tasks/', views.tasks, name="tareas"),
    path('tasks_complete/', views.tasks_complete, name="tarea_completada"),
    path('tasks/create/', views.create_tasks, name="crear_tareas"),
    path('tasks/<int:task_id>/', views.task_detail, name="detalle"),
    path('tasks/<int:task_id>/complet', views.complete_task, name="tareas_completas"),
    path('tasks/<int:task_id>/delete', views.delete_task, name="tareas_eliminada"),
    path('logout/', views.signout, name="salir"),
    path('signin/', views.signin, name="iniciar"),
    
]
