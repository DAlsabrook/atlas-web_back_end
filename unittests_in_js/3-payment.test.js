const sinon = require("sinon");
const sendPaymentRequestToApi = require('./3-payment.js');
const Utils = require('./utils.js').Utils;
const assert = require('assert');

describe("sendPaymentRequestToApi", function () {
    beforeEach(function () {
        sinon.spy(Utils, "calculateNumber");
    });

    afterEach(function () {
        sinon.restore();
    });

    it("check if Utils.calculateNumber is called", function () {
        const consoleSpy = sinon.spy(console, 'log');
        sendPaymentRequestToApi(100, 20);
        assert(Utils.calculateNumber.calledWith('SUM', 100, 20));
        assert(consoleSpy.calledWith('The total is: 120'));
        consoleSpy.restore();
    });
});
