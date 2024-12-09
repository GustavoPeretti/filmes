document.querySelector('.enviar').addEventListener('click', async (e) => {
    e.preventDefault();

    let usuario = document.getElementsByName('usuario')[0].value;
    let email = document.getElementsByName('email')[0].value;
    let senha = document.getElementsByName('senha')[0].value;

    if (!usuario || !email || !senha) {
        Swal.fire({
            icon: "error",
            title: "Erro",
            text: "Não deixe campos vazios ao realizar o cadastro.",
        });

        return;
    }

    let resposta = await fetch('/auth/cadastrar', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'usuario': usuario,
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