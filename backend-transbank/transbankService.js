const { WebpayPlus } = require('transbank-sdk');
const config = require('./config');

// Crear una transacción WebpayPlus
const createTransaction = async (amount, buyOrder, sessionId, returnUrl) => {
    try {
        // Crear una instancia de transacción de Webpay Plus
        const transaction = new WebpayPlus.Transaction();
        
        // Generar la transacción con los datos recibidos
        const response = await transaction.create(buyOrder, sessionId, amount, returnUrl);

        // Retornar la URL de pago y el token generado
        return { url: response.url, token: response.token };
    } catch (error) {
        console.error('Error al crear la transacción:', error);
        throw error;
    }
};

module.exports = { createTransaction };
