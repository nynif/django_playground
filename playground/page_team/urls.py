from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'page_team'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_people>/', views.detail, name='detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)