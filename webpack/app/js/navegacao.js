
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
    $("#portal-searchbox .searchField").focus(function(){
        $("#portal-searchbox").toggleClass("busca-ativada");
    });
    $("#portal-searchbox .searchField").blur(function(){
        $("#portal-searchbox").toggleClass("busca-ativada");
    });
});

jQuery(function($) {
  $(window).scroll(function() {
    if ($(document).scrollTop() > 60) {
      $("body").addClass("header-fixo");
    } else {
      $("body").removeClass("header-fixo");
    }
  });
});
