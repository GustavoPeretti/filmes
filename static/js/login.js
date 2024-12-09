document.getElementById('enviar-login').addEventListener('click', async e => {
    e.preventDefault();

    let email = document.getElementsByName('email')[0].value;
    let senha = document.getElementsByName('senha')[0].value;

    if (!email || !senha) {
        Swal.fire({
            icon: "error",
            title: "Erro",
            text: "Não deixe campos vazios ao realizar o cadastro.",
        });

        return;
    }

    let resposta = await fetch('/auth/login', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'email': email,
            'senha': senha
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

document.querySelector('#redirecionar-cadastro').addEventListener('click', () => {
    window.location.href = '/auth/cadastrar';
});
