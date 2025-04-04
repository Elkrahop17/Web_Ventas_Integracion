const express = require('express');
const { createTransaction } = require('./transbankService');
const cors = require('cors');  // Solo si es necesario habilitar CORS

const app = express();
const port = 3000;

// Middleware para permitir solicitudes JSON
app.use(express.json());
app.use(cors({
    origin: ['http://localhost:8000', 'http://127.0.0.1:8000'],
    credentials: true
  }));  // Configuración específica de CORS para Django

// 🔹 Ruta para verificar que el servidor funciona correctamente
app.get('/', (req, res) => {
    res.send('Servidor funcionando correctamente.');
});

// 🔹 Ruta para crear una transacción
app.post('/create-transaction', async (req, res) => {
    const { amount, buyOrder, sessionId, returnUrl } = req.body;

    try {
        // Llamada a la función de creación de transacción
        const transaction = await createTransaction(amount, buyOrder, sessionId, returnUrl);

        // Enviar la URL de pago como respuesta
        res.json(transaction);
    } catch (error) {
        // Manejo de errores
        res.status(500).json({ message: 'Error al crear la transacción', error });
    }
});

// 🔹 Arrancar el servidor
app.listen(port, () => {
    console.log(`Servidor corriendo en http://localhost:${port}`);
});
