document.querySelector('#deletar').addEventListener('click', async e => {
    e.preventDefault();

    let resposta = await fetch('/user', {
        method: 'DELETE'
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

    window.location.href = '/auth/login';
});

document.querySelector('.nome-lapis').addEventListener('click', () => {
    document.querySelector('#nome').setAttribute('contenteditable', 'true');
});

document.querySelector('#salvar-nome').addEventListener('click', async e => {
    e.preventDefault();

    let usuario = document.querySelector('#nome').textContent;

    if (!usuario) {
        Swal.fire({
            icon: "error",
            title: "Erro",
            text: "Não deixe campos vazios ao realizar a edição.",
        });

        return;
    }

    let resposta = await fetch('/user/usuario', {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            usuario: usuario
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

    window.location.reload();
});

document.querySelector('#salvar-email').addEventListener('click', async e => {
    e.preventDefault();

    let email = document.querySelector('.email-input').value;

    if (!email) {
        Swal.fire({
            icon: "error",
            title: "Erro",
            text: "Não deixe campos vazios ao realizar a edição.",
        });

        return;
    }

    let resposta = await fetch('/user/email', {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: email
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

    window.location.href = '/auth/verificar';
});

document.querySelector('#salvar-senha').addEventListener('click', async e => {
    e.preventDefault();

    let senha = document.querySelector('.senha-input').value;
    let senhaConfirmacao = document.querySelector('.senha-confirmar-input').value;

    if (!senha || !senhaConfirmacao) {
        Swal.fire({
            icon: "error",
            title: "Erro",
            text: "Não deixe campos vazios ao realizar a edição.",
        });

        return;
    }

    if (senha != senhaConfirmacao) {
        Swal.fire({
            icon: "error",
            title: "Erro",
            text: "As senhas digitadas são diferentes.",
        });

        return;
    }

    let resposta = await fetch('/user/senha', {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            senha: senha
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

    window.location.href = '/auth/login';
});