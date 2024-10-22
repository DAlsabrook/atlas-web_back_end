const request = require('request');
const assert = require('assert');

describe('Index Page', () => {
    it('should return status code 200', (done) => {
        request('http://localhost:7865', (error, response, body) => {
            assert.strictEqual(response.statusCode, 200);
            done();
        });
    });

    it('should return the correct message', (done) => {
        request('http://localhost:7865', (error, response, body) => {
            assert.strictEqual(body, 'Welcome to the payment system');
            done();
        });
    });

    it('should return the correct message with id', (done) => {
        request('http://localhost:7865/cart/123', (error, response, body) => {
            assert.strictEqual(body, 'Payment methods for cart 123');
            done();
        });
    });

    it('id is not a number', (done) => {
        request('http://localhost:7865/cart/abc', (error, response, body) => {
            assert.strictEqual(body, 'id must be a number');
            done();
        });
    });

    // Login route
    it('Normal login', (done) => {
        request('http://localhost:7865/login/Tomas', (error, response, body) => {
            assert.strictEqual(body, 'Welcome Tomas');
            done();
        });
    });

    // Available payments route
    describe('Available Payments', () => {
        it('should return the correct payment methods', (done) => {
            request('http://localhost:7865/available_payments', (error, response, body) => {
                const expectedResponse = {
                    payment_methods: {
                        credit_cards: true,
                        paypal: false
                    }
                };
                assert.deepStrictEqual(JSON.parse(body), expectedResponse);
                done();
            });
        });
    });
});
