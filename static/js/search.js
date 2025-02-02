document.addEventListener("DOMContentLoaded", function () {
    const filtroCurso = document.getElementById("curso");
    const filtroPeriodo = document.getElementById("periodo");
    const filtroDisciplina = document.getElementById("disciplina");
    const filtroLivro = document.getElementById("livro");
    const filtroAutor = document.getElementById("autor");
    const botaoFiltrar = document.querySelector(".btn-filtrar");
    const listaLivros = document.querySelector(".livros");
    
    //Simulação de um banco de dados
    const livros = [
        { curso: "civil", periodo: "1", disciplina: "Cálculo", titulo: "Cálculo Aplicado", autor: "Roberto Lima" },
        { curso: "computaçao", periodo: "2", disciplina: "Algoritmos", titulo: "Lógica de Programação", autor: "Carlos Souza" },
        { curso: "mecanica", periodo: "3", disciplina: "Física", titulo: "Fundamentos de Mecânica", autor: "Maria Souza" },
        { curso: "eletrica", periodo: "4", disciplina: "Circuitos", titulo: "Teoria dos Circuitos", autor: "José Almeida" }
    ];

    botaoFiltrar.addEventListener("click", function () {
        const cursoSelecionado = filtroCurso.value;
        const periodoSelecionado = filtroPeriodo.value;
        const disciplinaDigitada = filtroDisciplina.value.toLowerCase();
        const livroDigitado = filtroLivro.value.toLowerCase();
        const autorDigitado = filtroAutor.value.toLowerCase();

        const livrosFiltrados = livros.filter(livro => {
            return (cursoSelecionado === "" || livro.curso === cursoSelecionado || cursoSelecionado === "todos") &&
                   (periodoSelecionado === "" || livro.periodo === periodoSelecionado || periodoSelecionado === "todos") &&
                   (disciplinaDigitada === "" || livro.disciplina.toLowerCase().includes(disciplinaDigitada)) &&
                   (livroDigitado === "" || livro.titulo.toLowerCase().includes(livroDigitado)) &&
                   (autorDigitado === "" || livro.autor.toLowerCase().includes(autorDigitado));
        });

        exibirLivros(livrosFiltrados);
    });

    function exibirLivros(livrosFiltrados) {
        listaLivros.innerHTML = "";

        if (livrosFiltrados.length === 0) {
            listaLivros.innerHTML = "<p>Nenhum livro encontrado.</p>";
            return;
        }

        livrosFiltrados.forEach(livro => {
            const livroHTML = `
                <div class="livro">
                    <img src="../static/img/image.png" alt="${livro.titulo}">
                    <div class="info">
                        <h3>${livro.titulo}</h3>
                        <p>Autor: ${livro.autor}</p>
                        <button class="btn-comprar" onclick="window.location.href='pagina_destino.html';">Comprar</button>
                    </div>
                </div>
            `;
            listaLivros.innerHTML += livroHTML;
        });
    }
});
