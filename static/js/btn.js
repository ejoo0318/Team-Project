// 좋아요
function tips_like_click() {
    document.location.href = '/community/' + $('#post_id').text() + '/like_tips/'
}


function qna_like_click() {
    document.location.href = '/community/' + $('#post_id').text() + '/like_qna/'
}


function board_like_click() {
    document.location.href = '/community/' + $('#post_id').text() + '/like_board/'
}


// 삭제
function tips_delete_click() {
    let result = confirm('정말로 삭제하시겠습니까?')
    if (result) {
        document.location.href = '/community/' + $('#post_id').text() + '/delete_tips/'
    }
}


function qna_delete_click() {
    let result = confirm('정말로 삭제하시겠습니까?')
    if (result) {
        document.location.href = '/community/' + $('#post_id').text() + '/delete_qna/'
    }
}


function board_delete_click() {
    let result = confirm('정말로 삭제하시겠습니까?')
    if (result) {
        document.location.href = '/community/' + $('#post_id').text() + '/delete_board/'
    }
}
//수정
// $('#edit').on('click',function(event) {
//    $("#title, #author, #content").removeAttr('disabled');
// }  )

// $(function (event) {
//     $('#edit_btn').on('click', function (event) {
//         $("#title, #author, #content").removeAttr('disabled');
//         // document.location.href = '/bbs/'+ $('#post_id').text() + '/b_edit/'
//     })
// })

function tips_edit_btn() {
    $(document).removeAttr("disabled")
}