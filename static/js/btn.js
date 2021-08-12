// 좋아요
function tips_like_click() {
    document.location.href = '/community/' + $('#board_id').text() + '/like_tips/'
}


function qna_like_click() {
    document.location.href = '/community/' + $('#board_id').text() + '/like_qna/'
}


function board_like_click() {
    document.location.href = '/community/' + $('#board_id').text() + '/like_board/'
}


// 삭제
function tips_delete_click() {
    let result = confirm('정말로 삭제하시겠습니까?')
    if (result) {
        document.location.href = '/community/' + $('#board_id').text() + '/delete_tips/'
    }
}


function qna_delete_click() {
    let result = confirm('정말로 삭제하시겠습니까?')
    if (result) {
        document.location.href = '/community/' + $('#board_id').text() + '/delete_qna/'
    }
}


function board_delete_click() {
    let result = confirm('정말로 삭제하시겠습니까?')
    if (result) {
        document.location.href = '/community/' + $('#board_id').text() + '/delete_board/'
    }
}


//수정
function tips_edit_btn() {
    document.location.href = '/community/' + $('#board_id').text() + '/tips_edit/'
}


// 댓글
$(function (event){
    //tips 댓글 등록버튼 클릭시
    $('#tips_comment_create_btn').on('click',function(event) {

        $.ajax({
            async : true,
            url : '/community/tips_commentCreate/',
            type : 'GET',
            data : {
                board_id : $('#board_id').text(),
                comment_author : $('#c_name').val(),
                comment_content : $('#c_content').val()
            },
            dataType : 'json',
            timeout : 3000,
            success : function(result) {
                let tr = $('<tr></tr>')
                let author_td = $('<td></td>').text(result.c_author)
                let content_td = $('<td></td>').text(result.c_content)
                let btn_td = $('<td></td>')
                let del_btn = $('<button></button>').attr('type','button')
                del_btn.attr('data-comment_id', result.c_id)
                del_btn.addClass('btn btn-danger')
                del_btn.attr('id','comment_delete_btn')
                del_btn.text('삭제')
                del_btn.on('click',function(event) {
                    $.ajax({
                        async : true,
                        url : '/community/commentDelete/',
                        type : 'GET',
                        data : {
                            comment_id : result.c_id
                        },
                        dataType : 'json',
                        timeout : 3000,
                        success : function(result) {
                            tr.remove()
                        },
                        error : function(err) {
                            alert('댓글 삭제 실패!')
                        }
                    })
                })

                btn_td.append(del_btn)

                tr.append(author_td)
                tr.append(content_td)
                tr.append(btn_td)

                $('#comment_body').append(tr)

            },
            error : function(err) {

                alert('댓글 등록 실패!')
            }
        })
    })

    //tips 댓글 삭제버튼 클릭시
    $('#tips_comment_delete_btn').on('click',function(event) {
        let del_tr = $(this)
        $.ajax({
            async : true,
            url : '/community/tips_commentDelete/',
            type : 'GET',
            data : {
                comment_id : $(this).attr('data-comment_id')
            },
            dataType : 'json',
            timeout : 3000,
            success : function(result) {
                del_tr.parent().parent().remove()
            },
            error : function(err) {
                alert('댓글 삭제 실패!')
            }
        })
    })

    // qna 댓글 등록버튼 클릭시
    $('#qna_comment_create_btn').on('click',function(event) {

        $.ajax({
            async : true,
            url : '/community/qna_commentCreate/',
            type : 'GET',
            data : {
                board_id : $('#board_id').text(),
                comment_author : $('#c_name').val(),
                comment_content : $('#c_content').val()
            },
            dataType : 'json',
            timeout : 3000,
            success : function(result) {
                let tr = $('<tr></tr>')
                let author_td = $('<td></td>').text(result.c_author)
                let content_td = $('<td></td>').text(result.c_content)
                let btn_td = $('<td></td>')
                let del_btn = $('<button></button>').attr('type','button')
                del_btn.attr('data-comment_id', result.c_id)
                del_btn.addClass('btn btn-danger')
                del_btn.attr('id','comment_delete_btn')
                del_btn.text('삭제')
                del_btn.on('click',function(event) {
                    $.ajax({
                        async : true,
                        url : '/community/commentDelete/',
                        type : 'GET',
                        data : {
                            comment_id : result.c_id
                        },
                        dataType : 'json',
                        timeout : 3000,
                        success : function(result) {
                            tr.remove()
                        },
                        error : function(err) {
                            alert('댓글 삭제 실패!')
                        }
                    })
                })

                btn_td.append(del_btn)

                tr.append(author_td)
                tr.append(content_td)
                tr.append(btn_td)

                $('#comment_body').append(tr)

            },
            error : function(err) {

                alert('댓글 등록 실패!')
            }
        })
    })

    // qna 댓글 삭제버튼 클릭시
    $('#qna_comment_delete_btn').on('click',function(event) {
        let del_tr = $(this)
        $.ajax({
            async : true,
            url : '/community/qna_commentDelete/',
            type : 'GET',
            data : {
                comment_id : $(this).attr('data-comment_id')
            },
            dataType : 'json',
            timeout : 3000,
            success : function(result) {
                del_tr.parent().parent().remove()
            },
            error : function(err) {
                alert('댓글 삭제 실패!')
            }
        })
    })


    // board 댓글 등록버튼 클릭시
    $('#comment_create_btn').on('click',function(event) {

        $.ajax({
            async : true,
            url : '/community/commentCreate/',
            type : 'GET',
            data : {
                board_id : $('#board_id').text(),
                comment_author : $('#c_name').val(),
                comment_content : $('#c_content').val()
            },
            dataType : 'json',
            timeout : 3000,
            success : function(result) {
                let tr = $('<tr></tr>')
                let author_td = $('<td></td>').text(result.c_author)
                let content_td = $('<td></td>').text(result.c_content)
                let btn_td = $('<td></td>')
                let del_btn = $('<button></button>').attr('type','button')
                del_btn.attr('data-comment_id', result.c_id)
                del_btn.addClass('btn btn-danger')
                del_btn.attr('id','comment_delete_btn')
                del_btn.text('삭제')
                del_btn.on('click',function(event) {
                    $.ajax({
                        async : true,
                        url : '/community/commentDelete/',
                        type : 'GET',
                        data : {
                            comment_id : result.c_id
                        },
                        dataType : 'json',
                        timeout : 3000,
                        success : function(result) {
                            tr.remove()
                        },
                        error : function(err) {
                            alert('댓글 삭제 실패!')
                        }
                    })
                })

                btn_td.append(del_btn)

                tr.append(author_td)
                tr.append(content_td)
                tr.append(btn_td)

                $('#comment_body').append(tr)

            },
            error : function(err) {

                alert('댓글 등록 실패!')
            }
        })
    })

    // board 댓글 삭제버튼 클릭시
    $('#comment_delete_btn').on('click',function(event) {
        let del_tr = $(this)
        $.ajax({
            async : true,
            url : '/community/commentDelete/',
            type : 'GET',
            data : {
                comment_id : $(this).attr('data-comment_id')
            },
            dataType : 'json',
            timeout : 3000,
            success : function(result) {
                del_tr.parent().parent().remove()
            },
            error : function(err) {
                alert('댓글 삭제 실패!')
            }
        })
    })

})