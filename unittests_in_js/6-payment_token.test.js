const getPaymenTokenFromApi = require('./6-payment_token');
const assert = require('assert');

describe('getPaymentTokenFromApi', () => {
    it('True test', async () => {
        const result = await getPaymenTokenFromApi(true);
        assert.strictEqual(result.data, 'Successful response from the API');
    });
});
