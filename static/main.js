const toggleBtn = document.querySelector('.navbar__toggleBtn');
const navbar__menu = document.querySelector('.navbar__menu');
const navbar__icons = document.querySelector('.navbar__icons');

toggleBtn.addEventListener('click', () => {
    navbar__menu.classList.toggle('active');
    navbar__icons.classList.toggle('active');
})

