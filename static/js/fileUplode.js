$(document).ready(function(){
  let fileTarget = $('.file-box .upload-hidden');

    fileTarget.on('change', function(){
        if(window.FileReader){
            let filename = $(this)[0].files[0].name;
        } else {
            let filename = $(this).val().split('/').pop().split('\\').pop();
        }

        $(this).siblings('.upload-name').val(filename);
    });
});
