$(function(){

    $('#add_breeder_form').on("submit", function(e){
       e.preventDefault();

        $.ajax({
            url: "/add_breeder/",
            data: $(this).serialize(),
            type: "POST",
            // dataType: "json"
        }).done(function(result){
            window.location.href = '/breeders/';
        });


    });


});

