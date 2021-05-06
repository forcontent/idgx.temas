jQuery(function($) {

    $("#portal-searchbox .searchField").focus(function(){
        $("#portal-searchbox").addClass("busca-ativada");
    });

    $('.fechar-busca').on('click', function () {
        $("#portal-searchbox").removeClass("busca-ativada");
    });

});

