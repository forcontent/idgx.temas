jQuery(function($) {
   $(document).ready(function(){        
     var originalSize = $('div').css('font-size');         
    // reset        
     $(".resetMe").click(function(){           
    $('body').css('font-size', originalSize);         
     });
   
     // Increase Font Size          
     $(".increase").click(function(){         
    var currentSize = $('div').css('font-size');         
    var currentSize = parseFloat(currentSize)*1.2;          
    $('body').css('font-size', currentSize);         
    return false;          
    });        

     // Decrease Font Size       
     $(".decrease").click(function(){        
     var currentFontSize = $('div').css('font-size');        
     var currentSize = $('div').css('font-size');        
     var currentSize = parseFloat(currentSize)*0.8;        
     $('body').css('font-size', currentSize);         
     return false;         
     });         
   });
});


