const navTriggerBtn = document.querySelector('#nav_trigger_btn');
const navMenu = document.querySelector('#nav_menu');

// event listener

navTriggerBtn.addEventListener('click', () => {
    navMenu.classList.toggle('nav-is-open');
});

// swiper
const swiper = new Swiper('.swiper', {
    loop: true,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },

    // breakpoints
    slidesPerView: 1,
    spaceBetween: 20,
    breakpoints: {
        320: {
            slidesPerView: 1,
            spaceBetween: 20
        },
        640: {
            slidesPerView: 1,
            spaceBetween: 20
        },
        1024: {
            slidesPerView: 1,
            spaceBetween: 20
        }
    }
});

// scroll reveal animations
const sr = ScrollReveal({
    origin: 'bottom',
    distance: '60px',
    duration: 1500,
    delay: 200,
    reset: false,
});

// Hero
sr.reveal('.hero__text', {origin: 'top'});

// Steps
sr.reveal('.steps__step', {distance: '100px', interval: 100});

// About

sr.reveal('.about__text', {origin: 'left'});
sr.reveal('.about__img', {origin: 'right', delay: 800});

// Bags
sr.reveal('.bags__bg', {delay: 800});
sr.reveal('.bags__title');
sr.reveal('.bags__slider', {delay: 800});

// brands
sr.reveal('.brands__img', {delay: 600, distance: '100px', interval: 100});

// work
sr.reveal('.work__title');
sr.reveal('.work__subtittle', {delay: 600});
sr.reveal('.work__grid', {delay: 600});

// stats
sr.reveal('.stats');
sr.reveal('.stats__item', {distance: '100px', interval: 100});

// news
sr.reveal('.news__title');
sr.reveal('.news__subtitle', {delay: 600});
sr.reveal('.news__grid', {delay: 600});
sr.reveal('.news_item', {distance: '100px', interval: 100, delay: 600});

// contact
sr.reveal('.contact__container');
sr.reveal('.contact__text', {delay: 600});

// footer
sr.reveal('.footer__item', {distance: '100px', interval: 100});
sr.reveal('.footer__copyright');