$(document).ready(function() {

		var updatePage = function(data) {
			var html = ''
			for(var i = 0; i < data.title.length; ++i){
					html += '<h1> {1} </h1> <p> <a href = "{0}"> {3} </p> </a> {2} </br> <p> <a href ="https://authenticjobs.com/jobs/{4}"> APPLY HERE </a> </p> <hr>'.format(data.url[i], data.title[i], data.description[i], data.name[i], data.id[i]);
			}
			$('#result').html(html);
		}

		$('form').on('submit', function(event) {
    $.getJSON('/process', {
				  keywords: $('#input').val(),
					page: 1
				}, function(data) {
          if (data.title.length == 0) {
    				$('#result').html("<p> Sorry, no results found! Please try with different keywords. </p> ");
    			} else {
						$('#next').show();
						$('#prev').show();
						$('#add').show();
						updatePage(data);
						$('#page').html(1);
    			}
				});
        return false;
      });

			$('#next').on('click', function(event) {
				var pageStr = $('#page').text();
				var page = parseInt(pageStr) + 1;
				console.log(page);
		    $.getJSON('/process', {
						  keywords: $('#input').val(),
							page : page
						}, function(data) {
							if (data.title.length == 0) {
		    				$('#result').html("<p> Sorry, no results found! Please try with different keywords. </p> ");
		    			} else {
								updatePage(data);
								$('#page').html(page);
		    			}
					});
		      return false;
				});

				$('#prev').on('click', function(event) {
					var pageStr = $('#page').text();
					var page = parseInt(pageStr) - 1;
					console.log(page);
					$.getJSON('/process', {
							  keywords: $('#input').val(),
								page : page
							}, function(data) {
								if (data.title.length == 0) {
			    				$('#result').html("<p> Sorry, no results found! Please try with different keywords. </p> ");
			    			} else {
									updatePage(data);
									$('#page').html(page);
			    			}
							});
			        return false;
						});

});

String.prototype.format = function () {
  var args = arguments;
  return this.replace(/\{\{|\}\}|\{(\d+)\}/g, function (m, n) {
    if (m == "{{") { return "{"; }
    if (m == "}}") { return "}"; }
    return args[n];
  });
};
