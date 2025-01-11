document.addEventListener("DOMContentLoaded", function () {
    const burger = document.querySelector('.burger');
    const navLinks = document.querySelector('.nav-links');

    burger.addEventListener('click', function () {
        // Burger menyusi animatsiyasini faollashtirish
        burger.classList.toggle('toggle');
        // Navigatsiya menyusini ko'rinadigan/ko'rinmaydigan qilish
        navLinks.classList.toggle('active');
    });
});
