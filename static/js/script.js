$(function(){
  $('.language__item:first-child').on('click', function(e){
    e.preventDefault();
    $('.language__item:not(:first-child)').toggleClass('language-dropdown');
    $('.language__item:first-child').toggleClass('active');
  });

  $('.profile').on('click', function(e){
    e.preventDefault();
    $('.profile-dropdown').toggleClass('active');
  });

  $('.profile').on('click', function(e){
    e.preventDefault();
    $('.profile').toggleClass('active');
  });

  $('.menu-group').on('click', function(e){
    e.preventDefault();
    $('.menu-group .menu-dropdown').toggleClass('menu-group__item');
    $('.menu-group .menu__link').toggleClass('active');
  });

  $('.menu-finance').on('click', function(e){
    e.preventDefault();
    $('.menu-finance .menu-dropdown').toggleClass('menu-finance__item');
    $('.menu-finance .menu__link').toggleClass('active');
  });

  $('.log-in__form-item').on('focusin', function(){
    $(this).addClass('blur');
    if($('.log-in__form-item:first').hasClass('blur')){
      $('.login-label').addClass('blur');
    }
    else{
      $('.login-label').removeClass('blur');
    }
    if($('.log-in__form-item:last').hasClass('blur')){
      $('.password-label').addClass('blur');
    }
    else{
      $('.password-label').removeClass('blur');
    }
  });
  $('.log-in__form-item').on('focusout', function(){
    $(this).removeClass('blur');
    if($('.log-in__form-item:first').hasClass('blur')){
      $('.login-label').removeClass('blur');
    }
   if($('.log-in__form-item:last').hasClass('blur')){
      $('.password-label').removeClass('blur');
    }
  });

  $('.password-icon').on('mousedown', function(){
    $('#password').attr('type', 'text');
  });
  $('.password-icon').on('mouseleave', function(){
    $('#password').attr('type', 'password');
  });

  $('.build-export__item').on('click', function(){
    $('.build-export__dropdown').toggleClass('build-export__dropdown_show');
  });

  $('select.modal-input').on('click', function(){
    this.classList.toggle('active');
  });

  $('.number-rule').on('input', function(){
    this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*?)\..*/g, '$1');
  });

  // FILTER

  let filter =  $('.filter');
  let filterList =  $('.filter-list');

  filter.on('click', function(){
    filter.toggleClass('filter_active');
    filterList.toggleClass('filter-list_active');
    $('.filter-arrow').toggleClass('filter-arrow_active');
  });

  let category =  $('.categories');
  let categoryList =  $('.categories-list');

  category.on('click', function(){
    category.toggleClass('categories_active');
    categoryList.toggleClass('categories-list_active');
  });



});

let edit = document.getElementsByClassName('build-table__item--7');
let item = document.getElementsByClassName('build-table__dropdown');

for(i = 0; i < edit.length; i++){
  edit[i].addEventListener('click', function(){
      this.querySelector('.build-table__dropdown').classList.toggle('build-table__dropdown--active');
  });
}

let menuBtn = document.querySelector('.menu-btn');
let navbar = document.querySelector('.navbar');
let contentItem = document.querySelector('.content-item');
let header = document.querySelector('.header');
let btnWrapper = document.querySelector('.btn-wrapper');
let closer = document.querySelector('.btn-close');

menuBtn.onclick = function(){
  navbar.classList.add('navbar--visible');
  contentItem.classList.add('menu-move');
  header.classList.add('menu-move');
  btnWrapper.classList.add('btn-move');
  closer.style.display = "block";
}

closer.onclick = function(){
  contentItem.classList.remove('menu-move');
  header.classList.remove('menu-move');
  btnWrapper.classList.remove('btn-move');
  navbar.classList.remove('navbar--visible');
  closer.style.display = "none";
}

window.onclick = function(event){
  if(event.target == navbar){
    navbar.classList.remove('navbar--visible');
    contentItem.classList.remove('menu-move');
    header.classList.remove('menu-move');
    btnWrapper.classList.remove('btn-move');
  }
}

let button = document.getElementsByClassName('btn-edit');
let btnClose = document.querySelector('#modal-close');
let modal = document.querySelector('#modal');
let enter = document.querySelector('.enter');

for(let i = 0; i < button.length; i++){
  button[i].onclick = function(){
    modal.classList.add('active');
  }
}


enter.onclick = function(e){
  e.preventDefault();
  modal.classList.add('active');
}

btnClose.onclick = function(){
  modal.classList.remove('active');
}

window.onclick = function(event){
  if(event.target == modal) {
    modal.classList.remove('active');
  }
}

let greyBtn = document.getElementsByClassName('grey-btn');

for(let i = 0; i < greyBtn.length; i++){
  greyBtn[i].onclick = function(){
    this.querySelector('.grey-arrow').classList.toggle('active');
  }
  
}