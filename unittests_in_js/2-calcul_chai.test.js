const calculateNumber = require('./2-calcul_chai.js');

async function runTests() {
    try {
        const { expect } = await import('chai');

        describe('calculateNumber', () => {
            it('should return 2 when inputs are 1 and 1', () => {
                expect(calculateNumber("SUM", 1, 1)).to.equal(2);
            });

            it('should return 4 when inputs are 1.4 and 2.6', () => {
                expect(calculateNumber("SUM", 1.4, 2.6)).to.equal(4);
            });

            it('should return 5 when inputs are 1.5 and 2.5', () => {
                expect(calculateNumber("SUM", 1.5, 2.5)).to.equal(5);
            });

            it('should return 3 when inputs are 1.4 and 2.4', () => {
                expect(calculateNumber("SUM", 1.4, 2.4)).to.equal(3);
            });

            it('should return -2 when inputs are 1.4 and 2.6 for SUBTRACT', () => {
                expect(calculateNumber("SUBTRACT", 1.4, 2.6)).to.equal(-2);
            });

            it('should return 3.3333333333333335 when inputs are 1.4 and 2.6 for DIVIDE', () => {
                expect(calculateNumber("DIVIDE", 10.4, 2.6)).to.equal(3.3333333333333335);
            });

            it('should return "Error" when inputs are 1.4 and 0 for DIVIDE', () => {
                expect(calculateNumber("DIVIDE", 1.4, 0)).to.equal('Error');
            });
        });

        // Run the tests
        run();
    } catch (error) {
        console.error('Failed to load module:', error);
    }
}

runTests();
