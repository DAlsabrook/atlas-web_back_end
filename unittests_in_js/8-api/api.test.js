const request = require('supertest');

describe('Index Page', () => {
    it('should return status code 200', (done) => {
        request('http://localhost:7865')
            .get('/')
            .expect(200, done);
    });

    it('should return the correct message', (done) => {
        request('http://localhost:7865')
            .get('/')
            .expect('Welcome to the payment system', done);
    });
});
