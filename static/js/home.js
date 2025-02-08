const blocos = document.querySelectorAll('.bloco');
const modal = document.getElementById('modal');
const btnPeriodo = document.querySelectorAll('.btn-periodo');
const periodos = document.querySelector('.periodos');
const modalTitulo = document.getElementById('modal-titulo');

// Abrir modal ao clicar no bloco
blocos.forEach(bloco => {
  bloco.addEventListener('click', () => {
    modal.style.display = 'flex';
  });
});

// Atualizar o conteúdo do modal ao clicar no período
btnPeriodo.forEach(button => {
  button.addEventListener('click', () => {
    // Mudar o título do modal para "Selecione a Disciplina"
    modalTitulo.innerText = 'Selecione a Disciplina';

    // Alterar os períodos para as matérias
    periodos.innerHTML = `
      <button class="btn-materia">Matéria 1</button>
      <button class="btn-materia">Matéria 2</button>
      <button class="btn-materia">Matéria 3</button>
      <button class="btn-materia">Matéria 4</button>
      <button class="btn-materia">Matéria 5</button>
      <button class="btn-materia">Matéria 6</button>
    `;

    // Adiciona event listener para redirecionar ao clicar em qualquer botão de matéria
    const btnMaterias = document.querySelectorAll('.btn-materia');
    btnMaterias.forEach(btn => {
      btn.addEventListener('click', () => {
        window.location.href = '../book/book.html';
      });
    });
  });
});


// Fechar o modal
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


