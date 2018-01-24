function get_votes() {
    $.ajax({
        url:'/get-votes',
        success: function (data) {
            total = data['nairobi'] + data['athens'] + data['bangkok'] + data['reykjavik']
            max_val = Math.max(data['nairobi'] ,data['athens'], data['bangkok'] ,data['reykjavik'])
            update_column(data, "nairobi",0, total, max_val)
            update_column(data, "athens",1, total, max_val)
            update_column(data, "bangkok",2, total, max_val)
            update_column(data, "reykjavik",3, total, max_val)
        }
    });
}

function update_column(data, city, position, total, max_val) {
   n = parseInt($("#" + city).html())
   diff = data[city] - n
   for (var i = 0; i < diff; i++ ) {
        myBarChart.addToken({category:position})
   }
   $("#" + city).html(data[city])
   percentage = ((data[city] / total) * 100).toFixed(0)
   $("#cat-" + city).html(percentage + "%")
   if (max_val == data[city]) {
        $(".pos-" + position + " button").removeClass("button-blue")
        $(".pos-" + position + " button").addClass("button-red")
   } else {
        $(".pos-" + position + " button").removeClass("button-red")
        $(".pos-" + position + " button").addClass("button-blue")
   }
}

$( document ).ready(function() {
    $(".option button").click(function() {
        var answer = $(this).html()
        $.ajax({
            url:'/cast-vote?answer=' + answer,
            success: function (data) {
                console.log(data.answer)
                console.log(data.response)
            }
        });
    });

    setInterval(function(){ get_votes() }, 3000);
})