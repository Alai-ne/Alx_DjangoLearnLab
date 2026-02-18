from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin-dashboard/', views.admin_view, name='admin_view'),
    path('librarian-dashboard/', views.librarian_view, name='librarian_view'),
    path('member-dashboard/', views.member_view, name='member_view'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
]
