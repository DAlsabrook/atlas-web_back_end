const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
    // SUM tests
    it('Simple SUM Test', () => {
        assert.strictEqual(calculateNumber('SUM', 1, 1), 2);
    });

    // SUBTRACT tests
    it('Simple SUBTRACT test', () => {
        assert.strictEqual(calculateNumber('SUBTRACT', 2, 1), 1);
    });

    // DIVIDE tests
    it('Simple DIVIDE test', () => {
        assert.strictEqual(calculateNumber('DIVIDE', 10, 5), 2);
    });
})
