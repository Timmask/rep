from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.void,name='about'),
    path('bike1/',views.bike1,name='bike1'),
    path('bike2/',views.bike2,name='bike2'),
    path('bike3/',views.bike3,name='bike3'),
    path('bike4/',views.bike4,name='bike4'),
    path('part1/',views.part1,name='part1'),
    path('bike/<int:pk>/', views.bike_detail, name='bike_detail'),
    path('part/<int:pk>/', views.part_detail, name='part_detail'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.register,name='register'),
    path('part/', views.part,name='part'),
    path('search/', views.Search.as_view(), name='search'),
    path('sort/',views.Sort.as_view(),name='sort'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)