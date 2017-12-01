$(document).ready(function() {
	//getCurrentSessionCart();
	var updatePage = function(data) {
		var html = ''
		html += '<ul class="collapsible" data-collapsible="accordion">'

		for(var i = 0; i < data.title.length; ++i){
			var str = '<li><div class="collapsible-header"> <strong>{1}</strong>  ' +
			'</div> <div class="collapsible-body"> <span class="browser-default"> ' +
			'<h2 class="center-align"><a href = "{0}"> {3} </p> </a></h2> {2}<br> ' +
			'<p class="center-align"><a id="button-{5}" class="addToList waves-effect waves-light btn"><i class="material-icons left">add_circle</i>Add Job</a> </p> </span> </div> </li>';

			html += str.format(data.url[i], data.title[i], data.description[i], data.name[i], data.id[i], i);
		}
		html += '</ul>'
		$('#result').html(html);
		initialise(data);
		$('.collapsible').collapsible();


	}




	$('form').on('submit', function(event) {
		$('.progress').show();
		$.getJSON('/process', { //This gets the JSON returned from the process function, by sending keywords and page parameter
			keywords: $('#input').val(), //This gets keywords user entered
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
				$('.progress').hide();
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


var initialise = function intialise(data) {
	$(".addToList").on("click", function(){
		var jsdata = $(this).attr('id');
		var index = jsdata.split("-");
		var indexVal = index[1];
		var title = data.title[indexVal];
		var descr = data.description[indexVal];
		var id = data.id[indexVal]
		$(this).text("Remove Job");
		$.getJSON("/add_cart", {
			cartID: id,
			title: title,
			description: descr
		}, function(response) {
			updateCart(response);
		})
});
}

var updateCart = function(data) {
		var html = ''
		html += '<ul class="collapsible" data-collapsible="accordion">'

		for(var i = 0; i < data.title.length; ++i){
			var str = '<li><div class="collapsible-header"> <strong>{0}</strong>  ' +
			'</div> <div class="collapsible-body"> <span class="browser-default"> {1}' +
			'<p class="center-align"><a id ="button-{2}" class="removeFromList waves-effect waves-light btn"><i class="material-icons left">add_circle</i>Remove Job</a> </p> </span> </div> </li>';

			html += str.format(data.title[i], data.description[i], i);
		}
		html += '</ul>'
		$('#result2').html(html);
		$('.collapsible').collapsible();

		denitialise(data);
 	}

 var denitialise = function intialise(data) {
	$(".removeFromList").on("click", function(){
		var jsdata = $(this).attr('id');
		var index = jsdata.split("-");
		var indexVal = index[1];
		var id = data.id[indexVal];
		$(this).text("Remove Job");
		$.getJSON("/add_cart", {
			cartID: id,
		}, function(response) {
			updateCart(response);
		})
});
}


// var currCart = function getCurrentSessionCart(data) {
// 	console.log("getting current session")
// 	$.getJSON("/get_cart", {
// 			cartID: id,
// 			title: title,
// 			description: descr
// 		}, function(response) {
// 			updateCart(response);
// 		})
// 	};
