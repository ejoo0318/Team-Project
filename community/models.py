from django.db import models


# 자유게시판
class Board(models.Model):

    b_title = models.CharField(max_length=30)
    b_author = models.CharField(max_length=20)
    b_content = models.TextField()
    b_date = models.DateTimeField(auto_now=True)
    b_comment_count = models.IntegerField(default=0)
    b_like_count = models.IntegerField(default=0)
    b_photo = models.ImageField(blank=True, null=True, default='../media/noimage.jpg')

    def __str__(self):
        return self.b_title


class BoardComment(models.Model):
    c_author = models.CharField(max_length=20)
    c_content = models.CharField(max_length=100)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)  # 어떤 게시글의 댓글인지 FK 설정

    def __str__(self):
        return self.c_content


# Q&A 게시판
class Qna(models.Model):
    b_title = models.CharField(max_length=30)
    b_author = models.CharField(max_length=20)
    b_content = models.TextField()
    b_date = models.DateTimeField(auto_now=True)  # 글 수정하면 수정한 시각으로 갱신됨
    b_comment_count = models.IntegerField(default=0)
    b_like_count = models.IntegerField(default=0)
    b_photo = models.ImageField(blank=True, null=True, default='../media/noimage.jpg')

    def __str__(self):
        return self.b_title


class QnaComment(models.Model):
    c_author = models.CharField(max_length=20)
    c_content = models.CharField(max_length=100)
    board = models.ForeignKey(Qna, on_delete=models.CASCADE)  # 어떤 게시글의 댓글인지 FK 설정

    def __str__(self):
        return self.c_content


# Tip 게시판
class Tips(models.Model):
    b_title = models.CharField(max_length=30)
    b_author = models.CharField(max_length=10)
    b_content = models.TextField()
    b_date = models.DateTimeField(auto_now=True)
    b_comment_count = models.IntegerField(default=0)
    b_like_count = models.IntegerField(default=0)
    b_photo = models.ImageField(blank=True, null=True, default='../media/noimage.jpg')

    def __str__(self):
        return self.b_title


class TipsComment(models.Model):
    c_author = models.CharField(max_length=20)
    c_content = models.CharField(max_length=100)
    board = models.ForeignKey(Tips, on_delete=models.CASCADE)  # 어떤 게시글의 댓글인지 FK 설정

    def __str__(self):
        return self.c_content
