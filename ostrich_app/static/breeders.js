$(function(){


    $('#show_breeder_list_div').load( "/show_breeders/" );


    var breeders_div = $('#show_add_breeder_form_div');
    breeders_div.load( "/add_breeder/" );


    $(document).on("click", '.show_breeders_td', function(){
        var this_el = $(this),
            hidden_div = this_el.parent().next().children().eq(0).children().eq(0),
            hidden_div_text = hidden_div.text();

        if (hidden_div_text == 'a' ){
            hidden_div.text('');
            $.ajax({
                url:
                "/get_breeder/" + $(this).parent().data("id") + "/?format=json",
            }).done(function(data) {
                var sex = '',
                    year = (new Date()).getFullYear() - data.birth_year;
                if(data.sex==1){sex = 'female'}
                else{sex = 'male'}
                hidden_div.append(
                    'Sex: '+sex+'<br>Age: '+year+'<br>Description: '+data.description);
            });
        };

        this_el.parent().next().toggle();
    });


    $(document).on("click", '#deceased_breeder_btn', function(){
        $('[data-is_alive="False"]').toggle();
    });


    $('#add_breeder_btn').on('click', function(e){
        e.preventDefault();
        breeders_div.load( "/add_breeder/" );
        breeders_div.slideDown();

        // var wasVisible = $("#elementXX").is(":visible");
        // $("[id^=element]:visible").stop().slideUp("slow");
        // if (!wasVisible) {
        //     $("#elementXX").slideDown("slow");
        // }

        $(document).on('submit','#add_breeder_form',function(e){
            e.preventDefault();

            $.ajax({
                url: "/add_breeder/",
                data: $(this).serialize(),
                type: "POST"
            }).done(function(){
                $('#show_breeder_list_div').load( "/show_breeders/" );
            });

        });
    });


    $(document).on("click", '#modify_breeder_btn', function(){
        var this_el_pp_id = $(this).parent().parent().data('id');
        breeders_div.load( "/modify_breeder/"+this_el_pp_id);
        breeders_div.slideDown();

        $(document).off("submit", "#add_breeder_form");
        $(document).on('submit','#add_breeder_form',function(e){
            e.preventDefault();

            $.ajax({
                url: "/modify_breeder/"+this_el_pp_id+'/',
                data: $(this).serialize(),
                type: "POST"
            }).done(function(){
                $('#show_breeder_list_div').load( "/show_breeders/" );
            });

        });


    });


});

