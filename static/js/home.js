const blocos = document.querySelectorAll('.bloco');
const modal = document.getElementById('modal');
const periodosContainer = document.querySelector('.periodos');
const modalTitulo = document.getElementById('modal-titulo');

// Open modal when a course block is clicked
blocos.forEach(bloco => {
  bloco.addEventListener('click', () => {
    const curso = bloco.getAttribute('data-curso');
    const periodos = bloco.getAttribute('data-periodos').split(',');

    // Update modal with the course's periods
    modalTitulo.innerText = `Selecione o Período de ${curso}`;
    periodosContainer.innerHTML = periodos.map(p =>
      `<button class="btn-periodo" data-periodo="${p}" data-curso="${curso}">${p}º Período</button>`
    ).join("");

    // Display the modal
    modal.style.display = 'flex';

    // Add event listeners to period buttons
    document.querySelectorAll('.btn-periodo').forEach(button => {
      button.addEventListener('click', () => {
        const periodoId = button.dataset.periodo;
        const curso = button.dataset.curso;
        window.location.href = `/livros/?query_filter=${curso}&periodo=${periodoId}`;
      });
    });
  });
});

// Close the modal when clicking outside
window.addEventListener('click', (e) => {
  if (e.target === modal) {
    modal.style.display = 'none';
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const livros = document.querySelectorAll(".livro");
  const materiaTexto = document.getElementById("materia-livro");
  const carrossel = document.querySelector(".carrossel");
  let currentIndex = 0;
  let totalLivros = livros.length;

  function avancarCarrossel() {
    // Move o primeiro livro para o final, mantendo sempre 3 visíveis
    const primeiroLivro = carrossel.firstElementChild;
    carrossel.appendChild(primeiroLivro);

    // Remove destaque de todos os livros
    livros.forEach(livro => livro.classList.remove("destaque"));

    // O livro central sempre será o terceiro na fila após a rotação
    let novoLivroDestaque = carrossel.children[2];
    novoLivroDestaque.classList.add("destaque");

    // Atualiza o nome da matéria correspondente
    materiaTexto.textContent = `Matéria: ${novoLivroDestaque.dataset.materia}`;
  }

  // Faz o loop contínuo do carrossel
  setInterval(() => {
    avancarCarrossel();
  }, 3000);
});


