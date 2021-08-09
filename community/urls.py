from django.urls import path
from . import views


app_name = 'community'


urlpatterns = [
    path('login/', views.login, name='login'),
    path('account/', views.account, name='account'),
    path('logout/', views.logout, name='logout'),
    path('tips/', views.tips, name='tips'),
    path('qna/', views.qna, name='qna'),
    path('board/', views.board, name='board'),
    path('hospital/', views.hospital, name='hospital'),
    path('shelter/', views.shelter, name='shelter'),
    path('tips/tips_create/', views.tips_create, name='tips_create'),
    path('qna/qna_create/', views.qna_create, name='qna_create'),
    path('board/board_create/', views.board_create, name='board_create'),
    path('tips/tips_detail/', views.tips_detail, name='tips_detail'),
    path('qna/qna_detail/', views.qna_detail, name='qna_detail'),
    path('board/board_detail/', views.board_detail, name='board_detail'),
]
