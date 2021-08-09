from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# def login(request):
#     return render(request, 'community/login.html')
#
#
# def account(request):
#     return render(request, 'community/account.html')
# 로그인
def login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'community/login.html', {'error': 'user_name or password is incorrect.'})
    else:
        return render(request, 'community/login.html')


# 회원가입
def account(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['user_name'],
                password=request.POST['password1'],
                email=request.POST['email'], )
            auth.login(request, user)
            return redirect('/')
        return render(request, 'community/account.html')
    return render(request, 'community/account.html')


# 로그아웃
def logout(request):
    auth.logout(request)
    return redirect('/')


def tips(request):
    return render(request, 'community/tips.html')


def qna(request):
    return render(request, 'community/qna.html')


def board(request):
    return render(request, 'community/board.html')


def hospital(request):
    return render(request, 'community/hospital.html')


def shelter(request):
    return render(request, 'community/shelter.html')


def tips_create(request):
    return render(request, 'community/create.html')


def qna_create(request):
    return render(request, 'community/create.html')


def board_create(request):
    return render(request, 'community/create.html')


def tips_detail(request):
    return render(request, 'community/detail.html')


def qna_detail(request):
    return render(request, 'community/detail.html')


def board_detail(request):
    return render(request, 'community/detail.html'
                  )