var Respostas = $('#Respostas')
$('#slide').on('click', function(){
    Respostas.slideDown(500);
});

$('#esconder').on('click', function(){
    Respostas.fadeOut(500);
});