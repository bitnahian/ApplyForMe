$(document).ready(function() {

	$('form').on('submit', function(event) {
    $.getJSON('/process', {
				  keywords: $('#input').val(),
				}, function(data) {
					var myJSON = JSON.stringify(data);
          if (data.error) {
    				$('#result').html(myJSON.error);
    			} else {
    				$('#result').html(myJSON);
    			}
				});
        return false;
      });
});
