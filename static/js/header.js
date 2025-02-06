// document.addEventListener("DOMContentLoaded", function () {
//     const loginBtn = document.getElementById("login-btn");
//     const userIcon = document.getElementById("user-icon");
//     const popup = document.getElementById("user-popup");
//     const closeBtn = document.querySelector(".close-btn");
//     const logoutBtn = document.getElementById("logout-btn");

//     // Simulando login ao clicar no botão
//     loginBtn.addEventListener("click", function () {
//         loginBtn.classList.add("hidden"); // Esconde o botão de login
//         userIcon.classList.remove("hidden"); // Mostra o ícone do usuário
//     });

//     // Abre o popup ao clicar no ícone do usuário
//     userIcon.addEventListener("click", function (event) {
//         event.stopPropagation();
//         popup.style.display = popup.style.display === "block" ? "none" : "block";
//     });

//     // Fecha o popup ao clicar no botão de fechar
//     closeBtn.addEventListener("click", function () {
//         popup.style.display = "none";
//     });

//     // Fecha o popup ao clicar fora dele
//     document.addEventListener("click", function (event) {
//         if (!popup.contains(event.target) && event.target !== userIcon) {
//             popup.style.display = "none";
//         }
//     });

//     // Simulando logout
//     logoutBtn.addEventListener("click", function () {
//         popup.style.display = "none";
//         loginBtn.classList.remove("hidden"); // Volta a exibir o botão de login
//         userIcon.classList.add("hidden"); // Esconde o ícone do usuário
//     });
// });

// Impede de fazer pesquisas vazias
function checkSearchQuery() {
    const searchQuery = document.querySelector('input[name="search_query"]').value.trim();
    if (searchQuery === '') {
        return false;
    }
    return true;
}