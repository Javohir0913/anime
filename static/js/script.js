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

// <script>
//     function togglePassword(inputId) {
//     const input = document.getElementById(inputId);
//     const icon = event.target;
//
//     if (input.type === "password") {
//     input.type = "text";
//     icon.classList.remove('fa-eye');
//     icon.classList.add('fa-eye-slash');
// } else {
//     input.type = "password";
//     icon.classList.remove('fa-eye-slash');
//     icon.classList.add('fa-eye');
// }
// }
// </script>