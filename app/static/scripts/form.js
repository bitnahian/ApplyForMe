$(document).ready(function() {

	$('form').on('submit', function(event) {
    $.getJSON('/process', {
				  keywords: $('#input').val(),
				}, function(data) {
          if (data.error) {
    				$('#result').html(data.error);
    			} else {
    				$('#result').html(data);
    			}
				});
        return false;
      });
});
