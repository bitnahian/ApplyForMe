$(document).ready(function() {
		var updatePage = function(data) {
			var html = ''
			html += '<ul class="collapsible" data-collapsible="accordion">'

			for(var i = 0; i < data.title.length; ++i){
			 		 html += '<li><div class="collapsible-header"> <strong>{1}</strong>  </div> <div class="collapsible-body"> <span class="browser-default"> <h2 class="center-align"><a href = "{0}"> {3} </p> </a></h2> {2}<br> <p class="center-align"><a class="waves_effect waves_light btn center-align" href="https://authenticjobs.com/jobs/{4}"> <i class="material-icons left">add_circle</i>Add to List</a></p> </span> </div>  </li>'.format(data.url[i], data.title[i], data.description[i], data.name[i], data.id[i]);
			}
			html += '</ul>'
			
			$('#result').html(html);
			$('.collapsible').collapsible();

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
