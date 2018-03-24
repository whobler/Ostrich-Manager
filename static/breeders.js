$(function(){

    $('#show_breeder_list_div').load( "/show_breeders/" );

    var breeders_div = $('#show_add_breeder_form_div');
    breeders_div.load( "/add_breeder/" );


    $('.show_breeders').children().each(function() {
        $(this).on("click", function (){
            $.ajax({
                url:
                "/breeders/" + $(this).data("id") + "/?format=json",

                }).done(function(data) {
                    var breeder_div=$('#breeder');
                    breeder_div.text('');
                    var sex = '',
                        year = (new Date()).getFullYear() - data.birth_year;
                    if(data.sex==1){sex = 'female'}
                    else{sex = 'male'}
                    breeder_div.append(
                        'Sex: '+sex+'<br>Age: '+year+'<br>Description: '+data.description);
                });

        });
    });


    $(document).on("click", '#deceased_breeder_btn', function(){
        $('[data-is_alive="False"]').toggle();
    });


    $('#add_breeder_btn').on('click', function(e){
        e.preventDefault();
        breeders_div.slideToggle();

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
        console.log('im in modify button nana');
    });


});

