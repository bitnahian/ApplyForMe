$(document).ready(function() {
    var cart_length = $("#length").attr('value');

    $("#keno").click(function(){
        var total = 0;
        for(var i = 0; i < cart_length ; ++ i) {
            var j = parseInt(i) + 1;
            var selector = "input[name='" + j + "']";
            var money = $(selector).val();
            if(money != "")
              total += parseInt(money);
        }
        var html = '<i class="material-icons prefix">attach_money</i>' + total;
        $("#output").html(html);
    });

    $('#submit').on('click', function(event) {
      var budget = [];
      for(var i = 0; i < cart_length ; ++ i) {
          var j = parseInt(i) + 1;
          var selector = "input[name='" + j + "']";
          var money = $(selector).val();
          if(money != "")
            budget.push(parseInt(money));
          else
            budget.push(-1);
      }
  		$.getJSON('/submit_jobs', {
        budgets : JSON.stringify(budget)
  		}, function(data) {
        alert("Success");
        window.location.href = $SCRIPT_ROOT;
  		});
  		return false;
  	});
});
