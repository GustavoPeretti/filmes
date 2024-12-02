document.getElementById('enviar-login').addEventListener('click', e => {
    e.preventDefault();
    window.location.href = '/'; 
});

document.getElementById('redirecionar-cadastro').addEventListener('click', e => {
    window.location.href = '/auth/cadastrar'; 
});
