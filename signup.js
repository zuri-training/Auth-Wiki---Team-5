const menuControls = document.querySelector('.hamburger-menu');
const myMenu = document.querySelector('nav ul');
menuControls.addEventListener('click', menuDisplays);

function menuDisplays(){
     myMenu.classList.toggle('show-ul')
}