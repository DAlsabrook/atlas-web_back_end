const sinon = require("sinon");
const sendPaymentRequestToApi = require('./5-payment.js');
const Utils = require('./utils.js');
const assert = require('assert');

describe("sendPaymentRequestToApi", function () {

    let consoleSpy;

    beforeEach(function () {
        consoleSpy = sinon.spy(console, 'log');
    });

    afterEach(function () {
        sinon.restore();
    });

    it("5: Console only called once", function () {
        sendPaymentRequestToApi(100, 20);
        assert(consoleSpy.calledOnce)
        // check that the console has the correct output with the stub output
        assert(consoleSpy.calledWith('The total is: 120'));
    });

    it("5: Check correct output using stub on calculateNumber", function () {
        sendPaymentRequestToApi(10, 10);
        assert(consoleSpy.calledOnce)
        // check that the console has the correct output with the stub output
        assert(consoleSpy.calledWith('The total is: 20'));
    });
});
