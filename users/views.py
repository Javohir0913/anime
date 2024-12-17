from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse


User = get_user_model()
# Create your views here.


def logout_view(request):
    logout(request)
    messages.success(request, 'Siz muvaffaqiyatli chiqdingiz!')
    return redirect('login-register')  # Chiqishdan so'ng login sahifasiga yo'naltirish


def signup_and_login(request):
    if request.method == 'POST':
        if request.POST.get('password1'):
            confirm_password = request.POST.get('password2')
            password = request.POST.get('password1')

            if confirm_password == password:
                data_post = request.POST.copy()
                data_post['username'] = data_post['reg-username']
                form = UserCreationForm(data_post)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Sizning hisobingiz yaratildi!')
                    return redirect('login-register')  # Yangi hisob yaratildi, login sahifasiga yo'naltirish
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
                return redirect('login-register')  # Redirect to home page after login
            else:
                messages.error(request, 'Invalid username or password!')

            return render(request, 'registration/register and login.html')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register and login.html', {'form': form})


def check_username(request):
    username = request.GET.get('reg-username', None)  # URL-dan "reg-username" olish
    if username:
        # Username mavjud yoki yo'qligini tekshirish
        is_taken = User.objects.filter(username=username).exists()
        return JsonResponse({'is_taken': is_taken})
    return JsonResponse({'error': 'Username kiritilmadi!'}, status=400)

