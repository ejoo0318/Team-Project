
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
