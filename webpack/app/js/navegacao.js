
jQuery(function($) {
    $(".icon-menu").click(function(){
        $(".icon-menu").toggleClass("menu-aberto");
        $("#mainnavigation-wrapper").toggleClass("menu-aberto");
    });
});

jQuery(function($) {
  $( "#portal-globalnav li:has(.submenu)" ).addClass( "tem-submenu" );
});

jQuery(function($) {
    $("#portal-searchbox .searchField").focusin(function(){
        $("#portal-searchbox").toggleClass("busca-ativada");
    });
    $("#portal-searchbox .searchField").focusout(function(){
        $("#portal-searchbox").toggleClass("busca-ativada");
    });
});