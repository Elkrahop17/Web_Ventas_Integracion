// Verificacion de campos para registrarse
const alertPlaceholder = document.getElementById('liveAlertPlaceholder');

    const appendAlert = (message, type, timeout = 5000) => {
        const wrapper = document.createElement('div');
        wrapper.innerHTML = `
            <div class="alert alert-${type} alert-dismissible" role="alert">
                <div>${message}</div>
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>`;
    
        alertPlaceholder.append(wrapper);
    
        setTimeout(() => {
            wrapper.remove();
        }, timeout);
    };
    
    const alertTrigger = document.getElementById('liveAlertBtn');
    if (alertTrigger) {
        alertTrigger.addEventListener('click', (event) => {
            event.preventDefault(); // Detener el comportamiento predeterminado del formulario
            
            // Obtener los valores de los campos de entrada
            const nombre = document.getElementById('text1').value;
            const apellido = document.getElementById('text2').value;
            const correo = document.getElementById('exampleInputEmail1').value;
            const contrasena = document.getElementById('exampleInputPassword1').value;
            const confirmarContrasena = document.getElementById('exampleInputPassword2').value;
            
            // Verificar si los campos están vacíos
            if (nombre === '' || apellido === '' || correo === '' || contrasena === '' || confirmarContrasena === '') {
                // Mostrar alerta indicando que los campos están vacíos
                appendAlert('Por favor, complete todos los campos.', 'danger');
            } else {
                // Si los campos están llenos, procede con el registro
                appendAlert('¡Genial, has completado todos los campos!', 'success', 10000);
                
            }
        });
    }