from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import include
urlpatterns = [
    
    path('', views.post_list, name='post_list'),
    # path('grappelli/', include('grappelli.urls')),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('login/',views.user_login,name='login'),

    path('logout/',views.user_logout,name='logout'),
    
    path('register/',views.register,name='register'),
    path('Search/',views.Search.as_view(),name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)