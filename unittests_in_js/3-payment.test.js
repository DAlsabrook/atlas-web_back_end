const sinon = require("sinon");
const sendPaymentRequestToApi = require('./3-payment.js');
const Utils = require('./utils.js');
const assert = require('assert');

describe("sendPaymentRequestToApi", function () {
    beforeEach(function () {
        sinon.spy(Utils, "calculateNumber");
    });

    afterEach(function () {
        sinon.restore();
    });

    it("3: check if calculateNumber called and math checks out", function () {
        const consoleSpy = sinon.spy(console, 'log');
        sendPaymentRequestToApi(100, 20);
        assert(Utils.calculateNumber.calledWith('SUM', 100, 20));
        assert(consoleSpy.calledWith('The total is: 120'));
        consoleSpy.restore();
    });
});
