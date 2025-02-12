const btnPeriodo = document.querySelectorAll('.btn-periodo');
const periodos = document.querySelector('.periodos');
const blocos = document.querySelectorAll('.bloco');
const modal = document.getElementById('modal');
const periodosContainer = document.querySelector('.periodos');
const modalTitulo = document.getElementById('modal-titulo');

// Abrir modal ao clicar no bloco do curso
blocos.forEach(bloco => {
  bloco.addEventListener('click', async () => {
    const curso = bloco.getAttribute('data-curso');

    // Buscar períodos do curso via API Django
    const response = await fetch(`/api/periodos/?curso=${curso}`);
    const periodos = await response.json();

    // Atualizar modal com os períodos do curso
    modalTitulo.innerText = `Selecione o Período de ${curso}`;
    periodosContainer.innerHTML = periodos.map(p =>
      `<button class="btn-periodo" data-periodo="${p.id}">${p.numero}º Período</button>`
    ).join("");

    // Exibir modal
    modal.style.display = 'flex';

    // Adicionar evento para os botões de período
    document.querySelectorAll('.btn-periodo').forEach(button => {
      button.addEventListener('click', () => carregarMaterias(button.dataset.periodo));
    });
  });
});

// Carregar matérias do período
async function carregarMaterias(periodoId) {
  const response = await fetch(`/api/materias/?periodo=${periodoId}`);
  const materias = await response.json();

  modalTitulo.innerText = "Selecione a Disciplina";
  periodosContainer.innerHTML = materias.map(m =>
    `<button class="btn-materia" data-materia="${m.id}">${m.nome}</button>`
  ).join("");

  // Adicionar evento para redirecionar ao clicar em uma matéria
  document.querySelectorAll('.btn-materia').forEach(button => {
    button.addEventListener('click', () => {
      window.location.href = `/livros/?materia=${button.dataset.materia}`;
    });
  });
}

// Fechar o modal ao clicar fora
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


