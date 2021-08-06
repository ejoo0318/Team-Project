from django.shortcuts import render


def login(request):
    return render(request, 'community/login.html')


def account(request):
    return render(request, 'community/account.html')


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
    return render(request, 'community/tips/tips_create')


def qna_create(request):
    return render(request, 'community/qna/qna_create')


def board_create(request):
    return render(request, 'community/board/board_create')
