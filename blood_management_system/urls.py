from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from accounts.views import login_view, register_view, dashboard_view, logout_view
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import admin_dashboard, approve_request, reject_request, logout_view
# Simple home redirect
def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Already logged in → go to dashboard
    else:
        return redirect('login')

urlpatterns = [
    path('', home_redirect), 
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('api/', include('blood.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('approve-request/<int:request_id>/', approve_request, name='approve_request'),
    path('reject-request/<int:request_id>/', reject_request, name='reject_request'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
