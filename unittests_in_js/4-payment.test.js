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

    it("check if calculateNumber is called and called correctly", function () {
        const consoleSpy = sinon.spy(console, 'log');
        sendPaymentRequestToApi(100, 20);
        // make sure the calculateNumber method is called with right params
        assert(Utils.calculateNumber.calledWith('SUM', 100, 20));
        // check that the console has the correct output
        assert(consoleSpy.calledWith('The total is: 120'));
        consoleSpy.restore();
    });
});
