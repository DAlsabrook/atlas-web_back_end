const sinon = require("sinon");
const sendPaymentRequestToApi = require('./4-payment.js');
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

    it("4: Check correct output using stub on calculateNumber", function () {
        const stub = sinon.stub(Utils, 'calculateNumber').withArgs("SUM", 100, 20).returns(10);
        sendPaymentRequestToApi(100, 20);
        // make sure the calculateNumber method is called with right params
        assert(stub.calledWith('SUM', 100, 20));
        // check that the console has the correct output with the stub output
        assert(consoleSpy.calledWith('The total is: 10'));
    });
});
