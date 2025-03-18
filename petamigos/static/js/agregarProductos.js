// Inicializar el contador del carrito
var contadorCarrito = 0;
    
// Función para agregar un producto al carrito
function agregarAlCarrito(productoId) {
    contadorCarrito++;
    actualizarBadge();
}

// Función para actualizar el contador del carrito
function actualizarBadge() {
    var badge = document.getElementById('contadorCarrito');
    badge.innerText = contadorCarrito; 
}