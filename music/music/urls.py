from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index', views.index),
    path('genres/', views.genres),
    path('track/', views.track),
    path('add_genre/', views.add_genre),
    path('editgenre/<int:id_genre>', views.edit_genre),
    path('deletegenre/<int:id_genre>', views.delete_genre),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
