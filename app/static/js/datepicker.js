/* global $ */

$(document).ready(function() {
    
    $('.datepicker').pickadate({
          selectMonths: true,
          selectYears: 200,
          format: 'dddd, dd mmm, yyyy',
          formatSubmit: 'd/m/yyyy',
          hiddenName: true,
          min: new Date(1910,1,1),
          max: new Date(2012,11,31),
          today: '',
          clear: 'Clear Selection',
    });
    
    // $('input.datepicker').click(function(){
    //     // $(this).addClass("valid");
        
    //     alert("clicked");
    //     // var value = $(this).val();
    //     // var div = $(this).parent("div");
        
    //     // div.addClass("valid");
        
    //     // console.log("value is " + value);
        
    //     // if(!value){
    //     //     $(this).removeClass("valid");
    //     // }
    // });
    
});