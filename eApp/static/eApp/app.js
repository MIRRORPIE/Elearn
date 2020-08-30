$(document).ready(function(){
    var owl = $('.owl-carousel');

    owl.owlCarousel({
        loop:true,
        responsiveClass:true,
        autoplay: true,
        autoplayTimeout:5000,
        autoplayHoverPause:true,
        responsive:{
            0:{
                items:1,
                nav:true
            },
            576:{
                items:2,
                nav:true
            },
            992:{
                item:3,
                nav:true
            }
        }
    });

    // owl.on('mousewheel', '.owl-stage', function (e) {
    //     if (e.deltaY>0) {
    //         owl.trigger('next.owl');
    //     } else {
    //         owl.trigger('prev.owl');
    //     }
    //     e.preventDefault();
    // });


});
