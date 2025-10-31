from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from accounts.views import register_view, login_view, dashboard_view
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import logout_view
from accounts.views import admin_dashboard, approve_request, reject_request, logout_view
# Simple home redirect
def home_redirect(request):
    return redirect('dashboard')  

urlpatterns = [
    path('', home_redirect), 
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('api/', include('blood.urls')),
    path('logout/', logout_view, name='logout'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('approve-request/<int:request_id>/', approve_request, name='approve_request'),
    path('reject-request/<int:request_id>/', reject_request, name='reject_request'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
