from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import CustomUser
from .forms import CustomUserCreationForm
from blood.models import BloodDonationRequest, BloodBank
from blood.forms import BloodDonationRequestForm, BloodBankForm


# Registration
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        role = request.POST.get('role')

        if form.is_valid():
            user = form.save(commit=False)

            # Assign role
            if role == 'admin':
                user.is_staff = True
                user.is_donor = False
            elif role == 'donor':
                user.is_staff = False
                user.is_donor = True

            user.save()
            login(request, user)
            messages.success(request, f"{role.capitalize()} registered successfully!")
            return redirect('dashboard')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})

# Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')  # get selected role

        user = authenticate(request, username=username, password=password)
        if user:
            # Check role
            if role == 'admin' and user.is_staff:
                login(request, user)
                return redirect('dashboard')
            elif role == 'donor' and not user.is_staff:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, f"You are not allowed to login as {role}.")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'accounts/login.html')


# Logout
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have logged out successfully!")
    return redirect('login')


# Dashboard
@login_required
def dashboard_view(request):
    if request.user.is_staff:
        # Admin
        total_donors = CustomUser.objects.filter(is_donor=True).count()
        blood_banks = BloodBank.objects.all()
        pending_requests = BloodDonationRequest.objects.filter(status='Pending')
        return render(request, 'accounts/admin_dashboard.html', {
            'total_donors': total_donors,
            'blood_banks': blood_banks,
            'pending_requests': pending_requests
        })
    else:
        # Donor
        donations = BloodDonationRequest.objects.filter(donor=request.user)
        if request.method == 'POST':
            form = BloodDonationRequestForm(request.POST)
            if form.is_valid():
                donation = form.save(commit=False)
                donation.donor = request.user
                donation.save()
                messages.success(request, "Donation request submitted!")
                return redirect('dashboard')
        else:
            form = BloodDonationRequestForm()
        return render(request, 'accounts/donor_dashboard.html', {
            'donations': donations,
            'form': form,
            'blood_groups': BloodBank.objects.all()
        })


@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('dashboard')

    total_donors = CustomUser.objects.filter(is_donor=True).count()
    blood_banks = BloodBank.objects.all()
    pending_requests = BloodDonationRequest.objects.filter(status='Pending')

    context = {
        'total_donors': total_donors,
        'blood_banks': blood_banks,
        'pending_requests': pending_requests
    }
    return render(request, 'accounts/admin_dashboard.html', context)

@login_required
def approve_request(request, request_id):
    donation_request = get_object_or_404(BloodDonationRequest, id=request_id)
    donation_request.status = 'Approved'
    donation_request.save()

    # Update BloodBank units
    bank = BloodBank.objects.filter(blood_group=donation_request.blood_group).first()
    if bank:
        bank.units_available += donation_request.units
        bank.save()

    return redirect('admin_dashboard')


@login_required
def reject_request(request, request_id):
    donation_request = get_object_or_404(BloodDonationRequest, id=request_id)
    donation_request.status = 'Rejected'
    donation_request.save()
    return redirect('admin_dashboard')
