const calculateNumber = require('./utils.js');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
    const sum = calculateNumber('SUM', totalAmount, totalShipping)
    console.log(`The total is: ${sum}`);
}
