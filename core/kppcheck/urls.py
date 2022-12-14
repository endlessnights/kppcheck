from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.showmap, name='showmap'),
    # path('<int:pk>/', views.showkpp, name='showkpp'),
    path('kpp/<int:pk>/', views.showkpp, name='showkpp'),
    path('ads/', views.adsinfo, name='adsinfo')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)