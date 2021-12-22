
from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.FaqListCreateView.as_view()),
    path("rud/<int:pk>/", views.FaqRUDView.as_view())
]
