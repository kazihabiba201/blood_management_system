from django.urls import path
from .views import (
    register_view,
    login_view,
    logout_view,
    dashboard_view,
    admin_dashboard,
    approve_request,
    reject_request,
)

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('approve-request/<int:request_id>/', approve_request, name='approve_request'),
    path('reject-request/<int:request_id>/', reject_request, name='reject_request'),
]
