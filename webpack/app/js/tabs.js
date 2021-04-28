jQuery(function($) {
    $(document).ready(function() {    

    $('#tabs li a:not(:first)').addClass('inactive');
    $('.tabcontainer').hide();
    $('.tabcontainer:first').show();
        
    $('#tabs li a').click(function(){
        var t = $(this).attr('id');
      if($(this).hasClass('inactive')){ //this is the start of our condition 
        $('#tabs li a').addClass('inactive');           
        $(this).removeClass('inactive');
        
        $('.tabcontainer').hide();
        $('#'+ t + 'C').fadeIn('slow');
     }
    });

    });
});


