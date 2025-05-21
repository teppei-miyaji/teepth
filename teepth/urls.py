from django.contrib import admin
from django.urls import path, include  # ← include を必ずインポート

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # ← core.urls をルートに含める
]
