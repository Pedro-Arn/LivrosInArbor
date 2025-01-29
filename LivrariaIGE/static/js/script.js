// Posicionamento da header e footer
document.getElementById("header").innerHTML = fetch('header.html')
    .then(response => response.text())
    .then(data => document.getElementById('header').innerHTML = data);

document.getElementById("footer").innerHTML = fetch('footer.html')
    .then(response => response.text())
    .then(data => document.getElementById('footer').innerHTML = data);

// Menu em barras
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

// Impede de fazer pesquisas vazias
function checkSearchQuery() {
    const searchQuery = document.querySelector('input[name="search_query"]').value.trim();
    if (searchQuery === '') {
        return false;
    }
    return true;
}
  
// Criação da tela de filtros
var modal = document.getElementById("myModal");
  
var btn = document.getElementById("myBtn");
  
var span = document.getElementsByClassName("close")[0];
  
btn.onclick = function() {
    modal.style.display = "block";
}
  
span.onclick = function() {
    modal.style.display = "none";
}
  
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}