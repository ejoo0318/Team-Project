from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# 유기동물 보호센터 검색 기능
import xml.etree.ElementTree as ET
import pandas as pd
import requests
import json
# 댓글
from .models import Board, Qna, Tips, BoardComment, QnaComment, TipsComment
from django.http import JsonResponse


def home(request):
    posts_board = Board.objects.all().order_by('-id')
    posts_tips = Tips.objects.all().order_by('-id')
    posts_qna = Qna.objects.all().order_by('-id')

    return render(request, 'index.html', {
        'posts_board': posts_board,
        'posts_tips': posts_tips,
        'posts_qna': posts_qna,
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
        my_photos = request.FILES.getlist('photo')

        if len(my_photos) != 0:
            my_photo = my_photos[0]
            tips_board = Tips(b_title=title, b_author=author, b_content=content, b_photo=my_photo)
        else:
            tips_board = Tips(b_title=title, b_author=author, b_content=content)

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
        my_photos = request.FILES.getlist('photo')

        if len(my_photos) != 0:
            my_photo = my_photos[0]
            qna_board = Qna(b_title=title, b_author=author, b_content=content, b_photo=my_photo)
        else:
            qna_board = Qna(b_title=title, b_author=author, b_content=content)

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
        my_photos = request.FILES.getlist('photo')

        if len(my_photos) != 0:
            my_photo = my_photos[0]
            board_board = Board(b_title=title, b_author=author, b_content=content, b_photo=my_photo)
        else:
            board_board = Board(b_title=title, b_author=author, b_content=content)

        board_board.save()

        return HttpResponseRedirect(reverse('community:board'))
    else:
        return render(request, 'community/board_create.html')


# tips 댓글
def tips_detail(request, post_id):
    posts = get_object_or_404(Tips, id=post_id)
    comments = posts.tipscomment_set.all().order_by('-id')  # 댓글 정보

    return render(request, 'community/tips_detail.html',
                  {'posts': posts,
                   'comments': comments})


def tips_c_create(request):
    comment = TipsComment()
    comment.c_author = request.GET['comment_author']
    comment.c_content = request.GET['comment_content']
    comment.board_id = request.GET['board_id']
    print('author : ' + request.GET['comment_author'])
    print('content : ' + request.GET['comment_content'])
    print('board_id : ' + request.GET['board_id'])
    comment.save()
    return JsonResponse({
        'code': '200',  # code 200의 의미는 삭제성공의 의미로 가정
        'c_author': request.GET['comment_author'],
        'c_content': request.GET['comment_content'],
        'c_id': comment.id
    }, json_dumps_params={'ensure_ascii': True})


def tips_c_delete(request):
    comment = get_object_or_404(TipsComment, id=request.GET['comment_id'])
    comment.delete()
    return JsonResponse({
        'code': '200'  # code 200의 의미는 삭제성공의 의미로 가정
    }, json_dumps_params={'ensure_ascii': True})


# qna 댓글
def qna_detail(request, post_id):
    posts = get_object_or_404(Qna, id=post_id)
    comments = posts.qnacomment_set.all().order_by('-id')

    return render(request, 'community/qna_detail.html',
                  {'posts': posts,
                   'comments': comments})


def qna_c_create(request):
    comment = QnaComment()
    comment.c_author = request.GET['comment_author']
    comment.c_content = request.GET['comment_content']
    comment.board_id = request.GET['board_id']
    print('author : ' + request.GET['comment_author'])
    print('content : ' + request.GET['comment_content'])
    print('board_id : ' + request.GET['board_id'])
    comment.save()
    return JsonResponse({
        'code': '200',  # code 200의 의미는 삭제성공의 의미로 가정
        'c_author': request.GET['comment_author'],
        'c_content': request.GET['comment_content'],
        'c_id': comment.id
    }, json_dumps_params={'ensure_ascii': True})


def qna_c_delete(request):
    comment = get_object_or_404(QnaComment, id=request.GET['comment_id'])
    comment.delete()
    return JsonResponse({
        'code': '200'  # code 200의 의미는 삭제성공의 의미로 가정
    }, json_dumps_params={'ensure_ascii': True})


# board 댓글
def board_detail(request, post_id):
    posts = get_object_or_404(Board, id=post_id)
    comments = posts.boardcomment_set.all().order_by('-id')  # 댓글 정보

    return render(request, 'community/board_detail.html',
                  {'posts': posts,
                   'comments': comments})


def board_c_create(request):
    comment = BoardComment()
    comment.c_author = request.GET['comment_author']
    comment.c_content = request.GET['comment_content']
    comment.board_id = request.GET['board_id']
    comment.save()
    return JsonResponse({
        'code': '200',  # code 200의 의미는 삭제성공의 의미로 가정
        'c_author': request.GET['comment_author'],
        'c_content': request.GET['comment_content'],
        'c_id': comment.id
    }, json_dumps_params={'ensure_ascii': True})


def board_c_delete(request):
    comment = get_object_or_404(BoardComment, id=request.GET['comment_id'])
    comment.delete()
    return JsonResponse({
        'code': '200'  # code 200의 의미는 삭제성공의 의미로 가정
    }, json_dumps_params={'ensure_ascii': True})


# 좋아요
def like_tips(request, post_id):
    posts = get_object_or_404(Tips, pk=post_id)
    posts.b_like_count += 1
    posts.save()
    return HttpResponseRedirect(reverse('community:tips_detail', args=(post_id,)))


def like_qna(request, post_id):
    posts = get_object_or_404(Qna, pk=post_id)
    posts.b_like_count += 1
    posts.save()
    return HttpResponseRedirect(reverse('community:qna_detail', args=(post_id,)))


def like_board(request, post_id):
    posts = get_object_or_404(Board, pk=post_id)
    posts.b_like_count += 1
    posts.save()
    return HttpResponseRedirect(reverse('community:board_detail', args=(post_id,)))


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
def tips_edit(request, post_id):
    posts = Tips.objects.get(pk=post_id)
    return render(request, 'community/tips_edit.html', {'posts': posts})


def qna_edit(request, post_id):
    posts = Qna.objects.get(pk=post_id)
    return render(request, 'community/qna_edit.html', {'posts': posts})


def board_edit(request, post_id):
    posts = Board.objects.get(pk=post_id)
    return render(request, 'community/board_edit.html', {'posts': posts})


# 수정 후 저장
def tips_modify(request, post_id):
    posts = Tips.objects.get(pk=post_id)
    if request.method == "POST":
        posts.b_title = request.POST['title']
        posts.b_content = request.POST['content']

        posts.save()
        return redirect('community:tips')
    else:
        return render(request, 'community/tips_edit.html', post_id)


def qna_modify(request, post_id):
    posts = Qna.objects.get(pk=post_id)
    if request.method == "POST":
        posts.b_title = request.POST['title']
        posts.b_content = request.POST['content']

        posts.save()
        return redirect('community:qna')
    else:
        return render(request, 'community/qna_edit.html', post_id)


def board_modify(request, post_id):
    posts = Board.objects.get(pk=post_id)
    if request.method == "POST":
        posts.b_title = request.POST['title']
        posts.b_content = request.POST['content']

        posts.save()
        return redirect('community:board')
    else:
        return render(request, 'community/board_edit.html', post_id)


# 병원검색
def hospital(request):
    return render(request, 'community/hospital.html')


# 보호동물 입양
def shelter(request):

    url = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic'

    payload = {
        'serviceKey': '1zQWNFsLekxRSL9eOgAGYY+0gq339y3pEyBW1vC31LkJf48SZvduvflcNjBC3/Oej9jwqY40e+7yDKdK+gDRRw==',
        'bgnde': '20210730',
        'endde': '20210731',
        'upr_cd': '6110000',
        'numOfRows': 7500
    }

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

    # 전체 컬럼 :
    # age careAddr careNm careTel chargeNm colorCd desertionNo filename happenDt happenPlace kindCd neuterYn noticeEdt noticeNo noticeSdt officetel orgNm popfile processState sexCd specialMark weight

    # 쓰는 컬럼:
    # age 나이 , careAddr 위치, careTel 보호소 번호, colorCd 색상 , desertionNo 신고번호, happenDt 신고 날짜, happenPlace  신고 위치

    columns = ['age', 'careAddr', 'careTel', 'colorCd', 'desertionNo', 'happenDt', 'happenPlace']
    df2 = pd.DataFrame(rows, columns=columns)
    df2 = df2.to_json(orient='columns', force_ascii=False)
    result = json.loads(df2)  # json을 python의 dictionary로 변경
    # dataframe을 json으로 변경해서 처리

    # data = df2.format(list(result.values()))

    context = {'df2': result,
               # 'data': data
               }

    return render(request, 'community/shelter.html', context)
