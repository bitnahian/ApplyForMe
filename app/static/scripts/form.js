$(document).ready(function() {

		$('form').on('submit', function(event) {
    $.getJSON('/process', {
				  keywords: $('#input').val(),
					page: 1
				}, function(data) {
          if (data.error) {
    				$('#result').html(data.error);
    			} else {
						$('#next').show();
						$('#prev').show();
						var html = ''
						for(var i = 0; i < data.title.length; ++i){
							  //html +=  "<h1><a href='"+ data.url[i] "'/>" + data.title[i] + "</h1> " +  data.description[i] + "</br>";
								html += '<h1> <a href = "{0}"> {1} </a> </h1> {2} <hr>'.format(data.url[i], data.title[i], data.description[i]);
						}
    				$('#result').html(html);
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
		          if (data.error) {
		    				$('#result').html(data.error);
		    			} else {
								var html = ''
								for(var i = 0; i < data.title.length; ++i){
								    //html +=  "<h1><a href='"+ data.url[i] "'>" + data.title[i] + "</h1> " +  data.description[i] + "</br>";
										html += '<h1> <a href = "{0}"> {1} </a> </h1> {2} <hr>'.format(data.url[i], data.title[i], data.description[i]);
								}
		    			$('#result').html(html);
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
			          if (data.error) {
			    				$('#result').html(data.error);
			    			} else {
									var html = ''
									for(var i = 0; i < data.title.length; ++i){
									    //html +=  "<h1><a href='"+ data.url[i] "'>" + data.title[i] + "</h1> " +  data.description[i] + "</br>";
											html += '<h1> <a href = "{0}"> {1} </a> </h1> {2} <hr>'.format(data.url[i], data.title[i], data.description[i]);
									}
			    				$('#result').html(html);
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
