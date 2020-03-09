function pullover() {
    document.querySelector(".full-screen-menu").classList.add("active");
    document.body.classList.add("locked");
}

function pullback(){
    document.querySelector(".full-screen-menu").classList.remove("active");
    document.body.classList.remove("locked");
}

document.querySelector(".menu").addEventListener("click", pullover);
document.querySelector(".exit").addEventListener("click", pullback);
