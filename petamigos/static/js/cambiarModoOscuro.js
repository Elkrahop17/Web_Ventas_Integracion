document.getElementById('darkModeToggle').addEventListener('click', function() {
    document.body.classList.toggle('dark-mode');
    document.querySelector('header').classList.toggle('dark-mode');
    document.querySelector('.navbar').classList.toggle('dark-mode');
    document.querySelector('footer').classList.toggle('dark-mode');
    document.getElementById('quienesSomos').classList.toggle('dark-mode');
    document.querySelectorAll('.card').forEach(function(card) {
        card.classList.toggle('dark-mode');
    });

    // Cambiar el icono del modo oscuro al modo claro y viceversa
    const darkModeIcon = document.getElementById('darkModeIcon');
    if (darkModeIcon.getAttribute('src') ===  moonIconPath) {
        darkModeIcon.setAttribute('src', sunIconPath); // Cambiar a icono de sol
        document.getElementById('modeToggleText').textContent = "Modo Claro"; // Cambiar texto
    } else {
        darkModeIcon.setAttribute('src', moonIconPath); // Cambiar a icono de luna
        document.getElementById('modeToggleText').textContent = "Modo Oscuro"; // Cambiar textus
    }

});