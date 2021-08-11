from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# 게시판 기능
from .models import Board, Qna, Tips
# 유기동물 보호센터 검색 기능
import xml.etree.ElementTree as ET
import pandas as pd
import requests
import json


# id값이 정렬안됨
# 수정버튼작동 수정등록버튼만들기
# 댓글

def home(request):
    posts_board = Board.objects.all().order_by('-b_date')
    # max_num = max(Board.post_id)
    posts_tips = Tips.objects.all().order_by('-b_date')
    posts_qna = Qna.objects.all().order_by('-b_date')

    return render(request, 'index.html', {
        'posts_board': posts_board,
        'posts_tips': posts_tips,
        'posts_qna': posts_qna
        # 'max_num': max_num
    })


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


# 게시판 리스트
def tips(request):
    posts = Tips.objects.all().order_by('-id')
    return render(request, 'community/tips.html', {'posts': posts})


def qna(request):
    posts = Qna.objects.all().order_by('-id')
    return render(request, 'community/qna.html', {'posts': posts})


def board(request):
    posts = Board.objects.all().order_by('-id')
    return render(request, 'community/board.html', {'posts': posts})


# # 게시판 새 글작성
@login_required(login_url="/community/login/")
def tips_create(request):
    if request.method == 'POST':
        author = request.user
        title = request.POST['title']
        content = request.POST['content']

        for img in request.FILES.getlist('photo'):
            my_photo = img
        tips_board = Tips(b_title=title, b_author=author, b_content=content, b_photo=my_photo)
        tips_board.save()

        return HttpResponseRedirect(reverse('community:tips'))
    else:
        return render(request, 'community/tips_create.html')


@login_required(login_url="/community/login/")
def qna_create(request):
    if request.method == 'POST':
        author = request.user
        title = request.POST['title']
        content = request.POST['content']

        for img in request.FILES.getlist('photo'):
            my_photo = img
        qna_board = Qna(b_title=title, b_author=author, b_content=content, b_photo=my_photo)
        qna_board.save()

        return HttpResponseRedirect(reverse('community:qna'))
    else:
        return render(request, 'community/qna_create.html')


@login_required(login_url="/community/login/")
def board_create(request):
    if request.method == 'POST':
        author = request.user
        title = request.POST['title']
        content = request.POST['content']

        for img in request.FILES.getlist('photo'):
            my_photo = img

        free_board = Board(b_title=title, b_author=author, b_content=content, b_photo=my_photo)
        free_board.save()

        return HttpResponseRedirect(reverse('community:board'))
    else:
        return render(request, 'community/board_create.html')


# 게시판 상세보기
def tips_detail(request, post_id):
    posts = get_object_or_404(Tips, id=post_id)
    # comments = posts.comment_set.all().order_by('-id')  # 댓글 정보

    return render(request, 'community/tips_detail.html', {'posts': posts})


def qna_detail(request, post_id):
    posts = get_object_or_404(Qna, id=post_id)
    # comments = posts.comment_set.all().order_by('-id')  # 댓글 정보

    return render(request, 'community/qna_detail.html', {'posts': posts})


def board_detail(request, post_id):
    posts = get_object_or_404(Board, id=post_id)
    # comments = posts.comment_set.all().order_by('-id')  # 댓글 정보

    return render(request, 'community/board_detail.html', {'posts': posts})


# 좋아요
def like_tips(request, post_id):
    posts = get_object_or_404(Tips, pk=post_id)
    posts.b_like_count += 1
    posts.save()
    return redirect('community:tips_detail', post_id)


def like_qna(request, post_id):
    posts = get_object_or_404(Qna, pk=post_id)
    posts.b_like_count += 1
    posts.save()
    return redirect('community:qna_detail', post_id)


def like_board(request, post_id):
    posts = get_object_or_404(Board, pk=post_id)
    posts.b_like_count += 1
    posts.save()
    return redirect('community:board_detail', post_id)


# 삭제
def delete_tips(request, post_id):
    posts = get_object_or_404(Tips, pk=post_id)
    posts.delete()
    return redirect('community:tips')


def delete_qna(request, post_id):
    posts = get_object_or_404(Qna, pk=post_id)
    posts.delete()
    return redirect('community:qna')


def delete_board(request, post_id):
    posts = get_object_or_404(Board, pk=post_id)
    posts.delete()
    return redirect('community:board')


# 수정
# def b_edit(request, post_id):
#     posts = get_object_or_404(Board, pk=post_id)
#     board_form = BoardForm(instance=posts)
#     return render(request, 'bbs/edit.html', {'board_form': board_form, 'post_id': post_id})


def hospital(request):
    return render(request, 'community/hospital.html')


def shelter(request):
    #    a_serch = animal_serch.object.all()
    #    context = {'animal_serch': animal_serch}
    #    return render(request, 'animal/animal.html', context)

    url = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic'

    payload = {
        'serviceKey': '1zQWNFsLekxRSL9eOgAGYY+0gq339y3pEyBW1vC31LkJf48SZvduvflcNjBC3/Oej9jwqY40e+7yDKdK+gDRRw==',
        'bgnde': '20210730',
        'endde': '20210731',
        'upr_cd': '6110000',
        'numOfRows': 7500
    }

    # root = elementTree.fromstring (request.get(url, verify=False).text)

    response = requests.get(url, params=payload)

    root = ET.fromstring(response.text)

    rows = []

    for item in root.iter('item'):
        row = {}
        for child in list(item):
            row[child.tag] = child.text  # child에 tag랑 text 사용할 수 있게
        rows.append(row)

    item = next(root.iter('item'))

    # 컬럼 목록 준비
    columns = []

    # Accumulation
    for child in list(item):
        columns.append(child.tag)

    df2 = pd.DataFrame(rows, columns=columns)
    df2 = df2.to_json(orient='columns', force_ascii=False)
    result = json.loads(df2)  # json을 python의 dictionary로 변경
    # dataframe을 json으로 변경해서 처리

    context = {'df2': result}

    #    return HttpResponse(json.dumps(df2, ensure_ascii=False),
    #                    content_type="application/json")

    #    return HttpResponse(df2,
    #                    content_type="application/json; charset=utf8")

    return render(request, 'community/shelter.html', context)
