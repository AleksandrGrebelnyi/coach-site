// Slider 1 with results of customers
$('.slider').slick({
  infinite: true,
  slidesToShow: 1,
  slidesToScroll: 1
});

// Slider 2 with feedbacks
$('.slider2').slick({
  infinite: true,
  slidesToShow: 1,
  slidesToScroll: 1
});

// Slider 3 with feedbacks
$('.slider3').slick({
  infinite: true,
  slidesToShow: 1,
  slidesToScroll: 1
});

// -----Code for bt-to-top
function backToTop() {
  let button = $('.bt-to-top');

  // ------Hide bt-to-top
  $(window).on('scroll', () => {
    if ($(this).scrollTop() >= 50) {
      button.fadeIn();
    } else {
      button.fadeOut();
    }
  });

  // -----Slow scroll to-top
  button.on('click', (e) => {
    e.preventDefault();
    $('html').animate({scrollTop: 0}, 1000);
  });
}
backToTop();

// -------------Slow scrolling to down to results, tariffs
$(function (){
  $('.nav a').on('click', function (e){
    e.preventDefault();
    $('html, body').animate({scrollTop: $($(this).attr('href')).offset().top}, 1000)
  });
});

// -------------Slow scrolling to down to BOOK PROGRAM
$(function (){
  $('.tariff-button a').on('click', function (e){
    e.preventDefault();
    $('html, body').animate({scrollTop: $($(this).attr('href')).offset().top}, 1000)
  });
});

// -----------Slow scrolling to down to TOP BUTTON
$(function (){
  $('.header-btn a').on('click', function (e){
    e.preventDefault();
    $('html, body').animate({scrollTop: $($(this).attr('href')).offset().top}, 1000)
  });
});

/*<!-- =============== Start burger menu ======= -->*/

const burger = document.querySelector('#burger');
const menu = document.querySelector('#menu');

burger.addEventListener('click', () => {
  menu.classList.toggle('disp');
});
