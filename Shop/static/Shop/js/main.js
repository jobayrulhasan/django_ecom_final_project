(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner(0);
    
    
    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 45) {
            $('.nav-bar').addClass('sticky-top shadow-sm');
        } else {
            $('.nav-bar').removeClass('sticky-top shadow-sm');
        }
    });


    // Hero Header carousel
    $(".header-carousel").owlCarousel({
        items: 1,
        autoplay: true,
        smartSpeed: 2000,
        center: false,
        dots: false,
        loop: true,
        margin: 0,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ]
    });


    // ProductList carousel
    $(".productList-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 2000,
        dots: false,
        loop: true,
        margin: 25,
        nav : true,
        navText : [
            '<i class="fas fa-chevron-left"></i>',
            '<i class="fas fa-chevron-right"></i>'
        ],
        responsiveClass: true,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:2
            },
            1200:{
                items:3
            }
        }
    });

    // ProductList categories carousel
    $(".productImg-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        dots: false,
        loop: true,
        items: 1,
        margin: 25,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ]
    });


    // Single Products carousel
    $(".single-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        dots: true,
        dotsData: true,
        loop: true,
        items: 1,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ]
    });


    // ProductList carousel
    $(".related-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        dots: false,
        loop: true,
        margin: 25,
        nav : true,
        navText : [
            '<i class="fas fa-chevron-left"></i>',
            '<i class="fas fa-chevron-right"></i>'
        ],
        responsiveClass: true,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:3
            },
            1200:{
                items:4
            }
        }
    });



   // Back to top button
   $(window).scroll(function () {
    if ($(this).scrollTop() > 300) {
        $('.back-to-top').fadeIn('slow');
    } else {
        $('.back-to-top').fadeOut('slow');
    }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });
})(jQuery);

// password show and hide
    document.querySelectorAll('.toggle-password').forEach(icon => {
        icon.addEventListener('click', function () {
            const input = document.getElementById(this.dataset.target);
            if (input.type === "password") {
                input.type = "text";
                this.classList.remove('fa-eye');
                this.classList.add('fa-eye-slash');
            } else {
                input.type = "password";
                this.classList.remove('fa-eye-slash');
                this.classList.add('fa-eye');
            }
        });
    });


//cart plus
$(".plus-cart").click(function () {
  var id = $(this).attr("productid").toString();
   // find nearest input field
   var quantityInput = $(this).closest(".quantity").find("input");
  console.log(id);
  $.ajax({
    type: "GET",
    url: "/pluscart",
    data: {
      prod_id: id,
    },
    success: function (data) {
      // update only this product's quantity
      quantityInput.val(data.quantity);
      document.getElementById("amount_").innerText = "$ " + data.amount + ".0";
      document.getElementById("totalamount_").innerText = "$ " + data.totalamount + ".0";
      document.getElementById("shippingamount_").innerText = "Flat rate: $ " + data.shippingAmount;
    },
  });
});

//cart minus
$(".minus-cart").click(function () {
  var id = $(this).attr("productid").toString();
  var quantityInput = $(this).closest(".quantity").find("input");
  $.ajax({
    type: "GET",
    url: "/minuscart",
    data: {
      prod_id: id,
    },
    success: function (data) {
      // update only this product's quantity
      quantityInput.val(data.quantity);
      document.getElementById("amount_").innerText = "$ " + data.amount + ".0";
      document.getElementById("totalamount_").innerText = "$ " + data.totalamount + ".0";
      document.getElementById("shippingamount_").innerText = "Flat rate: $ " + data.shippingAmount;
    },
  });
});


//Remove cart product
$(".remove_cart").click(function () {
  var id = $(this).attr("productid").toString();
  var eml = this;
  console.log(id);

  $.ajax({
    type: "GET",
    url: "/remove_cart_value",
    data: {
      prod_id: id,
    },
    success: function (data) {

      // Update totals
      document.getElementById("amount_").innerText = "$ " + data.amount;
      document.getElementById("totalamount_").innerText = "$ " + data.totalamount;
     document.getElementById("shippingamount_").innerText = "Flat rate: $ " + data.shippingamount;

      // Remove the entire row <tr>
      $(eml).closest("tr").remove();

       // If amount becomes 0 → show empty cart
      if (data.totalamount === 0) {
        window.location.href = "/emptycart/";
      }
    },
  });
});