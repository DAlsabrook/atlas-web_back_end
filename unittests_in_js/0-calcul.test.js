const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
    it('should return 2 when inputs are 1 and 1', () => {
        assert.strictEqual(calculateNumber(1, 1), 2);
    });

    it('should return 4 when inputs are 1.4 and 2.6', () => {
        assert.strictEqual(calculateNumber(1.4, 2.6), 4);
    });

    it('should return 5 when inputs are 1.5 and 2.5', () => {
        assert.strictEqual(calculateNumber(1.5, 2.5), 5);
    });

    it('should return 3 when inputs are 1.4 and 2.4', () => {
        assert.strictEqual(calculateNumber(1.4, 2.4), 3);
    });
});
