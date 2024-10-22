const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Welcome to the payment system');
})

app.get('/cart/:id', (req, res) => {
    const id = Number(req.params.id);
    if (isNaN(id)) {
        return res.status(404).send('id must be a number');
    }
    return res.status(200).send(`Payment methods for cart ${id}`)
})

app.get('/available_payments', (req, res) => {
    const paymentTypes = {
        payment_methods: {
            credit_cards: true,
            paypal: false
        }
    };
    return res.json(paymentTypes);
});

app.get('/login/:userName', (req, res) => {
    const userName = req.params.userName;
    return res.status(200).send(`Welcome ${userName}`)
});

app.listen(7865, () => {
    console.log('API available on localhost port 7865')
});
