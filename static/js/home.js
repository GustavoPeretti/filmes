document.querySelector('.info-perfil').addEventListener('click', () => {
    window.location.href = '/auth/conta';
});

document.querySelector('.nova-lista').addEventListener('click', e => {
    e.preventDefault();

    window.location.href = '/lista';
});