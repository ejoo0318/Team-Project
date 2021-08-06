from django.urls import path
from . import views


app_name = 'community'


urlpatterns = [
    path('login/', views.login, name='login'),
    path('account/', views.account, name='account'),
    path('tips/', views.tips, name='tips'),
    path('qna/', views.qna, name='qna'),
    path('board/', views.board, name='board'),
    path('hospital/', views.hospital, name='hospital'),
    path('shelter/', views.shelter, name='shelter'),
    path('tips/tips_create/', views.tips_create, name='tips'),
    path('qna/qna_create/', views.qna_create, name='qna'),
    path('board/board_create/', views.board_create, name='board'),
]
