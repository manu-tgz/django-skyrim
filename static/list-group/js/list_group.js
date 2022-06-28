$(document).ready(function(){   
    $('.all').on('click', 'li', function(){    
       $(this).appendTo('.selected');
    });

    $('.selected').on('click', 'li', function(){    
       $(this).appendTo('.all');
    });
});