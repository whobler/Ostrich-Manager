$(function(){

    var show_babies_ul = $('.show_eggs_babies');
    show_babies_ul.children().each(function(li) {
        $(this).on("click", function (){
            console.log('CLICKING BABY');
            $.ajax({
                url:
                "/eggs_babies/" + $(this).data("id") + "/?format=json",

                }).done(function(data) {
                    var baby_div=$('#egg_baby_div');
                    baby_div.text('');
                    var sex = '';
                    if(data.sex==1){sex = 'female'}
                    else{sex = 'male'}
                    baby_div.append(
                        'Sex: '+sex+'<br>Description: '+data.description);
                });

        });
    });

    var deceased_btn = $('#deceased_egg_baby_btn');
    var deceased_babies = $('[data-is_alive="False"]');
    deceased_babies.toggle();
    deceased_btn.on("click", function(){
        deceased_babies.slideToggle();
    });
});

