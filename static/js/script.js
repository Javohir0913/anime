document.addEventListener('DOMContentLoaded', () => {
    const burger = document.querySelector('.burger');
    const navLinks = document.querySelector('.nav-links');

    // Burger menu click event
    burger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        burger.classList.toggle('toggle');
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const themeToggle = document.getElementById("theme-toggle");
    const icon = themeToggle.querySelector("i");
    const body = document.body;

    if (localStorage.getItem("theme") === "dark") {
        body.classList.add("dark-mode");
        icon.classList.replace("bi-moon-fill", "bi-sun-fill"); // Quyosh belgisi
    }

    themeToggle.addEventListener("click", function () {
        body.classList.toggle("dark-mode");

        if (body.classList.contains("dark-mode")) {
            icon.classList.replace("bi-moon-fill", "bi-sun-fill"); // Quyosh rejimi
            localStorage.setItem("theme", "dark");
        } else {
            icon.classList.replace("bi-sun-fill", "bi-moon-fill"); // Kechki rejim
            localStorage.setItem("theme", "light");
        }
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