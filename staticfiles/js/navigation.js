document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
  
      const section = document.querySelector(this.getAttribute('href'));
      const topOffset = section.offsetTop;
  
      window.scrollTo({
        top: topOffset,
        behavior: 'smooth'
      });
    });
  });
//   const body = document.querySelector("body"),
//   modeToggle = body.querySelector(".mode-toggle");
//   sidebar = body.querySelector("nav");
//   sidebarToggle = body.querySelector(".sidebar-toggle");
//   modeText = body.querySelector(".link-mode")
// let getMode = localStorage.getItem("mode");
// if(getMode && getMode ==="dark"){
// body.classList.toggle("dark");
// modeText.innerText = "Light Mode";
// }

// let getStatus = localStorage.getItem("status");
// if(getStatus && getStatus ==="close"){
// sidebar.classList.toggle("close");
// }

// modeToggle.addEventListener("click", () =>{
// body.classList.toggle("dark");
// if(body.classList.contains("dark")){
//     localStorage.setItem("mode", "dark");
//     modeText.innerText = "Light Mode";

// }else{
//     localStorage.setItem("mode", "light");
//     modeText.innerText = "Dark Mode";
// }
// });

// sidebarToggle.addEventListener("click", () => {
// sidebar.classList.toggle("close");
// if(sidebar.classList.contains("close")){
//     localStorage.setItem("status", "close");
// }else{
//     localStorage.setItem("status", "open");
// }
// })