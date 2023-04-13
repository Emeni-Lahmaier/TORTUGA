const menuBtn = document.querySelector('.plus-btn');
const body = document.querySelector('body');
menuBtn.addEventListener('click', () => {
body.classList.toggle('menu-open');
});