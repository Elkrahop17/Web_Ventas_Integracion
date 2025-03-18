$(document).ready(function(){
    $("#btn-ingresar").click(function(event){
        // Evitar que el formulario se envíe automáticamente
        event.preventDefault();
        
        // Realizar las validaciones
        var email = $("#exampleInputEmail1").val();
        var password = $("#exampleInputPassword1").val();

        // Validación de email y contraseña
        if(email === ""){ 
            alert("Por favor, complete el campo de Email.");
            return;
        }

        if(password === ""){ 
            alert("Por favor, complete el campo de Contraseña.");
            return;
        }

        // Si las validaciones son exitosas, mostramos el modal de ingreso exitoso
        $('#modalIngresoExitoso').modal('show');
    });
});