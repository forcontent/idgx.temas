jQuery(function($) {
    $('.tile-faq dt').on('click', function () {
        $(this).next("dd").slideToggle();
        $(this).toggleClass("aberto");
    });
});


