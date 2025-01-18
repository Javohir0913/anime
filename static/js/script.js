document.addEventListener('DOMContentLoaded', () => {
    const burger = document.querySelector('.burger');
    const navLinks = document.querySelector('.nav-links');

    // Burger menu click event
    burger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        burger.classList.toggle('toggle');
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