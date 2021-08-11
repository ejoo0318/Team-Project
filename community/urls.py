from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'community'


urlpatterns = [
    # 회원관리
    path('login/', views.login, name='login'),
    path('account/', views.account, name='account'),
    path('logout/', views.logout, name='logout'),
    # 게시판 리스트
    path('tips/', views.tips, name='tips'),
    path('qna/', views.qna, name='qna'),
    path('board/', views.board, name='board'),
    path('hospital/', views.hospital, name='hospital'),
    path('shelter/', views.shelter, name='shelter'),
    # 게시판 새 글작성
    path('tips/tips_create/', views.tips_create, name='tips_create'),
    path('qna/qna_create/', views.qna_create, name='qna_create'),
    path('board/board_create/', views.board_create, name='board_create'),
    # 게시판 상세보기
    path('<int:post_id>/tips_detail/', views.tips_detail, name='tips_detail'),
    path('<int:post_id>/qna_detail/', views.qna_detail, name='qna_detail'),
    path('<int:post_id>/board_detail/', views.board_detail, name='board_detail'),
    # 좋아요
    path('<int:post_id>/like_tips/', views.like_tips, name="like_tips"),
    path('<int:post_id>/like_qna/', views.like_qna, name="like_qna"),
    path('<int:post_id>/like_board/', views.like_board, name="like_board"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
