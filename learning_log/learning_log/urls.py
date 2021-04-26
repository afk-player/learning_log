from django.contrib import admin
from django.urls import path, include


admin.site.site_header = 'Learning log'
admin.site.site_title = 'Learning log administration panel'
admin.site.index_title = 'Learning log administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning_logs.urls')),
    path('users/', include('users.urls')),
]
