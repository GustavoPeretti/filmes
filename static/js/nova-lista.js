async function pesquisar() {
    document.querySelector('#poster-lista-filmes').innerHTML = '';

    let pesquisa = document.querySelector('#pesquisa-filmes').value;

    let resposta = await fetch('/api/filme/' + pesquisa);

    let respostaJSON = await resposta.json();

    if (!respostaJSON.ok) {
        Swal.fire({
            icon: "error",
            title: "Erro",
            text: respostaJSON.mensagem
        });
        
        return;
    }

    let resultado = respostaJSON.resultado;

    for (let item of resultado) {
        let id = item.id;
        let titulo = item.titulo;
        let imagem = item.imagem;

        let poster = document.createElement('div');
        poster.classList.add('poster-titulo');
        poster.classList.add(`filme-${id}`);

        let checkbox = document.createElement('input');
        checkbox.setAttribute('type', 'checkbox');

        let label = document.createElement('label');

        let img = document.createElement('img');
        img.setAttribute('src', imagem);

        let divTitulo = document.createElement('div');
        divTitulo.classList.add('titulo-filme')

        let pTitulo = document.createElement('p');
        pTitulo.textContent = titulo;

        divTitulo.appendChild(pTitulo);

        label.appendChild(img);
        label.appendChild(divTitulo);

        poster.appendChild(checkbox);
        poster.appendChild(label);

        document.querySelector('#poster-lista-filmes').appendChild(poster);

        poster.addEventListener('click', () => {
            checkbox.click();
        })
    }
}

document.addEventListener('DOMContentLoaded', pesquisar)

document.querySelector('#pesquisa-filmes').addEventListener('keyup', pesquisar)

document.querySelector('button').addEventListener('click', async () => {
    let titulo = document.querySelector('.nome-da-lista').value;
    let privado = document.querySelector('#switch').checked;
    let filmes = [];

    for (let item of document.querySelector('#poster-lista-filmes').children) {
        if (item.querySelector('input').checked) {
            filmes.push(Array.from(item.classList).filter(e => e.substring(0, 6) == 'filme-')[0].split('-').at(-1));
        }
    }

    if (!titulo) {
        Swal.fire({
            icon: "error",
            title: "Erro",
            text: "Não deixe campos vazios ao realizar o cadastro.",
        });

        return;
    }

    let resposta = await fetch('/api/lista', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'titulo': titulo,
            'privado': privado,
            'filmes': filmes
        })
    });

    let respostaJSON = await resposta.json();

    if (!respostaJSON.ok) {
        Swal.fire({
            icon: "error",
            title: "Erro",
            text: respostaJSON.mensagem
        });
        
        return;
    }

    window.location.href = '/';
});
