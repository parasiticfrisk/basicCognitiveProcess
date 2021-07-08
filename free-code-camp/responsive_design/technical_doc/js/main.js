// Author: August Frisk
// Course: freeCodeCamp Responsive Design - Summer 2018
// Project: Technical Documentation Page

let menu = document.querySelector('.menu')
let navbar = document.querySelector('#navbar')
let closeBtn = document.querySelector('.btn-close')

let openDrawer = () => {
  navbar.style.left = '0'
  menu.style.display = 'none'
}

let closeDrawer = () => {
  navbar.style.left = '-25rem'
  menu.style.display = 'block'
}

menu.addEventListener('click', openDrawer)
closeBtn.addEventListener('click', closeDrawer)