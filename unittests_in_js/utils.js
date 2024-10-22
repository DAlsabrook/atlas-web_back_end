const Utils = {
    calculateNumber: (type, a, b) => {
        const roundA = Math.round(a);
        const roundB = Math.round(b);
        const possibleTypes = {
            'SUM': roundA + roundB,
            'SUBTRACT': roundA - roundB,
            'DIVIDE': roundB !== 0 ? roundA / roundB : 'Error'
        };

        if (type in possibleTypes) {
            return possibleTypes[type];
        } else {
            return 'Error: Wrong type. Must use SUM, SUBTRACT, DIVIDE';
        }
    }
}

module.exports = Utils;
