jQuery(function($) {
    $(".icon-menu").click(function(){
        $("#mainnavigation-wrapper").toggleClass("menu-aberto");
    });

    $(".icon-menu-aberto").click(function(){
        $("#mainnavigation-wrapper").toggleClass("menu-aberto");
    });
  
    $( "#portal-globalnav li:has(.submenu)" ).addClass( "tem-submenu" );

    $(window).scroll(function() {
      if ($(document).scrollTop() > 60) {
        $("body").addClass("header-fixo");
      } else {
        $("body").removeClass("header-fixo");
      }
    });
});
