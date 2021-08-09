from django.contrib import admin
from community.models import Board, BoardComment, Qna, QnaComment, Tips, TipsComment


admin.site.register(Board)
admin.site.register(BoardComment)
admin.site.register(Qna)
admin.site.register(QnaComment)
admin.site.register(Tips)
admin.site.register(TipsComment)
