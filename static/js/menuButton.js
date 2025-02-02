function semestresMenu() {
    console.log("Menu clicado");
    document.getElementById("semestres").classList.toggle("show");
}

window.onclick = function(event) {
    if (!event.target.closest('.menu-button')) {
        var dropdowns = document.getElementsByClassName("menu-content");
        for (var i = 0; i < dropdowns.length; i++) {
            if (dropdowns[i].classList.contains('show')) {
                dropdowns[i].classList.remove('show');
            }
        }
    }
};