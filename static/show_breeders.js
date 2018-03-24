$(function(){

    $('.show_breeders').children().each(function(li) {
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

    var deceased_btn = $('#deceased_breeder_btn');
    var deceased_breeders = $('[data-is_alive="False"]');
    deceased_breeders.toggle();
    deceased_btn.on("click", function(){
        deceased_breeders.slideToggle();
    });



    $('#add_breeder_a').on('click', function(e){
        e.preventDefault();
        console.log('ADD LINK CLICKED SUCCESFULLY');
        $('#show_add_breeder_form_div').load( "../templates/add_breeder.html" , function(){
            console.log('AAADDDDEEEDDD?????')
        });
    });

});

