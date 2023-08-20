from django.contrib.auth import get_user_model
from django.contrib.auth import login as django_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from .utils import login_code_generator, referral_code_generator

User = get_user_model()


@api_view(["GET", "POST"])
def login(request):
    if request.method == "GET":
        return render(request, 'registration/login.html')
    elif request.method == "POST":
        phone_number = request.POST['phone_number']
        if phone_number[0] == '8':
            phone_number = phone_number.replace('8', '+7', 1)
        request.session['phone_number'] = phone_number
        request.session['code'] = login_code_generator()
        return redirect('login_code')


@api_view(["GET", "POST"])
def get_code(request):
    phone_number = request.session['phone_number']
    code = request.session['code']

    if request.method == "GET":
        data = {"phone_number": phone_number, "code": code}
        return render(request, "registration/login_code.html", context=data)
    elif request.method == "POST":
        input_code = request.POST['input_code']
        if input_code == code:
            if User.objects.filter(phone_number=phone_number).exists():
                user = User.objects.get(phone_number=phone_number)
                django_login(request._request, user)
                return redirect('profile')
            else:
                return redirect('fill_profile')
        else:
            data = {"phone_number": phone_number, "code": code, "message": "Введенный код неверен, попробуйте еще раз"}
            return render(request, "registration/login_code.html", context=data)


@api_view(["GET", "POST"])
def fill_profile_data(request):
    if request.method == "GET":
        return render(request, "registration/profile_data.html")
    elif request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        referral_code = referral_code_generator()
        phone_number = request.session['phone_number']

        user = User.objects.create(phone_number=phone_number, first_name=first_name, last_name=last_name,
                                   username=username, referral_code=referral_code)

        django_login(request._request, user)
        return redirect('profile')


@login_required
@api_view(["GET", "POST"])
def profile(request):
    user = User.objects.get(phone_number=request.session['phone_number'])
    referrals = User.objects.filter(invite_code=user.referral_code)
    data = {"user": user, "referrals": referrals}

    if request.method == "GET":
        return render(request, "profile.html", context=data)
    if request.method == "POST":
        if 'input_code' in request.POST:
            code = request.POST['input_code']
            if user.referral_code == code:
                message = "Вы не можете вводить свой код"
                data['message'] = message
            elif User.objects.filter(referral_code=code).exists():
                user.invite_code = request.POST['input_code']
                user.save()
            else:
                message = "Вы ввели несуществующий код"
                data['message'] = message
        return render(request, "profile.html", context=data)
