from random import randint

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model, update_session_auth_hash
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.forms import PasswordChangeForm

from .forms import RegistrationForm
from .models import CustomUser

User = get_user_model()
# Create your views here.


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Siz muvaffaqiyatli chiqdingiz!')
        return redirect('login-register')  # Chiqishdan so'ng login sahifasiga yo'naltirish
    else:
        return redirect('login-register')


def signup_and_login(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    elif request.method == 'POST':
        if request.POST.get('password1'):
            if request.POST.get('password1') == request.POST.get('password2'):
                form = RegistrationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Sizning hisobingiz yaratildi!')
                    return redirect('home_page')  # Yangi hisob yaratildi, login sahifasiga yo'naltirish
                else:
                    messages.error(request, 'Ro‘yxatdan o‘tishda xatolik yuz berdi!')
            else:
                messages.error(request, 'Parollar mos kelmaydi!')

        else:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Welcome back!')
                return redirect('home_page')  # Redirect to home page after login
            else:
                messages.error(request, 'Invalid username or password!')
                return redirect('login-register')  # Login sahifasiga qaytarish
    else:
        form = RegistrationForm()

    return render(request, 'registration/register and login.html', {'form': form})


def check_username(request):
    username = request.GET.get('reg-username', None)  # URL-dan "reg-username" olish
    if username:
        # Username mavjud yoki yo'qligini tekshirish
        is_taken = User.objects.filter(username=username).exists()
        return JsonResponse({'is_taken': is_taken})
    return JsonResponse({'error': 'Username kiritilmadi!'}, status=400)


# ----------------- url va template qilinmagan -----------------
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', context={'form': form})


def send_email_code(request):
    username = request.user.username
    user = CustomUser.objects.get(username=username)
    if request.method == 'POST':
        confirm_email_cod = f'{randint(100, 999)}-{randint(100, 999)}'

        CustomUser.objects.filter(username=username).update(confirm_email_cod=confirm_email_cod)
        return redirect('confirm_email')
    else:
        return render(request, 'registration/send_code_email.html', context={'user': user})


def confirm_email(request):
    username = request.user.username
    user = CustomUser.objects.get(username=username)
    if request.method == 'POST':
        if user.confirm_email_cod == f"{request.POST.get('num1')}-{request.POST.get('num2')}":
            CustomUser.objects.filter(username=username).update(verified_email=True)
            return redirect('index')
        else:
            return redirect('confirm_email')

    send_mail(
        'Confirm email',
        f"'{user.confirm_email_cod}' bu xabarni hechkimga ko'rsatmang!",
        'Python.com',
        [user.email],

    )
    return render(request, 'registration/confirm_email.html', context={'user': user})
