from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# 게시판 기능
from .forms import BoardForm, BoardDetailForm
from .models import Board, BoardComment, Qna, QnaComment, Tips, TipsComment


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


############## 글 목록 보는 기능 (자유/Tip/QnA 게시판 별로) ##############
def tips(request):
    posts = Tips.objects.all().order_by('-id')
    return render(request, 'community/tips.html', {'posts': posts})


def qna(request):
    posts = Qna.objects.all().order_by('-id')
    return render(request, 'community/qna.html', {'posts': posts})


def board(request):
    posts = Board.objects.all().order_by('-id')
    return render(request, 'community/board.html', {'posts': posts})


############## 글 쓰는 기능 (자유/Tip/QnA 게시판 별로) ##############
def tips_create(request):
    # 글 작성 화면에서 저장 버튼을 눌렀을 때
    if request.method == 'POST':
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            new_post = board_form.save(commit=False)
            new_post.save()
            return redirect('community/tips.html')  # 작성하면 글 목록 화면으로 redirect

    # 리스트 화면에서 새글 작성 버튼을 눌렀을 때
    else:
        board_form = BoardForm()

    return render(request, 'community/tips_create.html', {
        'board_form': board_form
    })


def qna_create(request):
    # 글 작성 화면에서 저장 버튼을 눌렀을 때
    if request.method == 'POST':
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            new_post = board_form.save(commit=False)
            new_post.save()
            return redirect('community/qna.html')  # 작성하면 글 목록 화면으로 redirect

    # 리스트 화면에서 새글 작성 버튼을 눌렀을 때
    else:
        board_form = BoardForm()

    return render(request, 'community/qna_create.html', {
        'board_form': board_form
    })


def board_create(request):
    # 글 작성 화면에서 저장 버튼을 눌렀을 때
    if request.method == 'POST':
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            new_post = board_form.save(commit=False)
            new_post.save()
            return redirect('community/board.html')  # 작성하면 글 목록 화면으로 redirect

    # 리스트 화면에서 새글 작성 버튼을 눌렀을 때
    else:
        board_form = BoardForm()

    return render(request, 'community/board_create.html', {
        'board_form': board_form
    })


############## 글 조회 기능 (자유/Tip/QnA 게시판 별로) ##############
def tips_detail(request, board_id):
    post = get_object_or_404(Tips, id=board_id)
    board_detail_form = BoardDetailForm(instance=post)
    board_detail_form.show_board_detail()
    comments = post.comment_set.all().order_by('-id') # 댓글 정보

    return render(request, 'community/tips_detail.html',
                  {'board_detail_form': board_detail_form,
                   'comments': comments})


def qna_detail(request, board_id):
    post = get_object_or_404(Qna, id=board_id)
    board_detail_form = BoardDetailForm(instance=post)
    board_detail_form.show_board_detail()
    comments = post.comment_set.all().order_by('-id') # 댓글 정보

    return render(request, 'community/qna_detail.html',
                  {'board_detail_form': board_detail_form,
                   'comments': comments})


def board_detail(request, board_id):
    post = get_object_or_404(Board, id=board_id)
    board_detail_form = BoardDetailForm(instance=post)
    board_detail_form.show_board_detail()
    comments = post.comment_set.all().order_by('-id') # 댓글 정보

    return render(request, 'community/board_detail.html',
                  {'board_detail_form': board_detail_form,
                   'comments': comments})


# 변경 전 코드

# def login(request):
#     return render(request, 'community/login.html')
#
#
# def account(request):
#     return render(request, 'community/account.html')

#
# def tips(request):
#     return render(request, 'community/tips.html')
#
#
# def qna(request):
#     return render(request, 'community/qna.html')
#
#
# def board(request):
#     return render(request, 'community/board.html')


def hospital(request):
    return render(request, 'community/hospital.html')


def shelter(request):
    return render(request, 'community/shelter.html')


# def tips_create(request):
#     return render(request, 'community/tips_create.html')
#
#
# def qna_create(request):
#     return render(request, 'community/tips_create.html')
#
#
# def board_create(request):
#     return render(request, 'community/tips_create.html')


# def tips_detail(request):
#     return render(request, 'community/tips_detail.html')
#
#
# def qna_detail(request):
#     return render(request, 'community/tips_detail.html')
#
#
# def board_detail(request):
#     return render(request, 'community/tips_detail.html')
