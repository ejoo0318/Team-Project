from django import forms
from .models import Board


# 자유게시판
class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['b_title', 'b_author', 'b_content']


class BoardDetailForm(forms.ModelForm):

    b_title = forms.CharField(label='글제목')
    # b_author = forms.CharField(label='글작성자')
    b_content = forms.CharField(label='글내용')
    b_comment_count = forms.IntegerField(label='댓글수')
    b_like_count = forms.IntegerField(label='좋아요')

    class Meta:
        model = Board
        fields = '__all__'

    def show_board_detail(self):
        fields = self.get_all_fields_from_form(BoardDetailForm)
        for field in fields:
            self.fields[field].widget.attrs.update({
                'readonly': 'readonly'
            })

        self.fields['b_author'].widget.attrs.update({
            'disabled': 'disabled'
        })

    def show_board_update(self):
        self.fields['b_author'].widget.attrs.update({
            'disabled': 'disabled'
        })
        self.fields['b_like_count'].widget.attrs.update({
            'readonly': 'readonly'
        })
        self.fields['b_comment_count'].widget.attrs.update({
            'readonly': 'readonly'
        })

    @staticmethod
    def get_all_fields_from_form(instance):

        fields = list(instance().base_fields)

        for field in list(instance().declared_fields):
            if field not in fields:
                fields.append(field)
        return fields
