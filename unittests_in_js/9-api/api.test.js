const request = require('request');
const assert = require('assert');

describe('Index Page', () => {

    // Plain ol GET
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

    // Cart route
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
});
