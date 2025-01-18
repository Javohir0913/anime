document.addEventListener('DOMContentLoaded', () => {
    const burger = document.querySelector('.burger');
    const navLinks = document.querySelector('.nav-links');

    // Burger menu click event
    burger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        burger.classList.toggle('toggle');
    });
});

// Modalni olish
let modal = document.getElementById("tagModal");

// Modalni ochirish uchun "Anime tags" tugmasini olish
let animeTagsButton = document.getElementById("id_anime_tags");

// Modalni yopish uchun "x" tugmasini olish
let span = document.getElementsByClassName("close")[0];

// Modalni ochirish
animeTagsButton.addEventListener("click", function() {
  modal.style.display = "block";
});

// Modalni yopish
span.onclick = function() {
  modal.style.display = "none";
}

// OK tugmasini bosganda tanlangan taglarni ko'rsatish
document.getElementById("okBtn").addEventListener("click", function() {
  let selectedTags = Array.from(document.getElementById("modalTags").selectedOptions)
                            .map(option => option.text);

  // Tanlangan taglarni "Anime tags" selectga qo'shish
  let select = document.getElementById("id_anime_tags");
  select.innerHTML = ""; // Eski elementlarni tozalash
  selectedTags.forEach(tag => {
    let option = document.createElement("option");
    option.value = tag;
    option.text = tag;
    select.appendChild(option);
  });

  modal.style.display = "none"; // Modalni yopish
});

// Agar modalga tashqaridan bosilsa, uni yopish
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

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