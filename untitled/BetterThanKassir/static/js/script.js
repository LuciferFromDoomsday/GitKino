<<<<<<< HEAD
// updated 2019
const input = document.getElementById("search-input");
const searchBtn = document.getElementById("search-btn");

const expand = () => {
  searchBtn.classList.toggle("close");
  input.classList.toggle("square");
};

searchBtn.addEventListener("click", expand);
=======
    // updated 2019
    const input = document.getElementById("search-input");
    const searchBtn = document.getElementById("search-btn");

    const expand = () => {
        searchBtn.classList.toggle("close");
        input.classList.toggle("square");
    };

searchBtn.addEventListener("mouseover", expand);
input.addEventListener("mouseout", expand);
>>>>>>> b52f121ebd95f8e108df03c602b9a872fcacec61




<<<<<<< HEAD
//  old version / jquery
//
// function expand() {
//   $(".search").toggleClass("close");
//   $(".input").toggleClass("square");
//   if ($('.search').hasClass('close')) {
//     $('input').focus();
//   } else {
//     $('input').blur();
//   }
// }
// $('button').on('click', expand);
//
=======
    //  old version / jquery
    //
    // function expand() {
    //   $(".search").toggleClass("close");
    //   $(".input").toggleClass("square");
    //   if ($('.search').hasClass('close')) {
    //     $('input').focus();
    //   } else {
    //     $('input').blur();
    //   }
    // }
    // $('button').on('click', expand);
    //
>>>>>>> b52f121ebd95f8e108df03c602b9a872fcacec61
