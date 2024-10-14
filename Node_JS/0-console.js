/**
 *
 * @param {string} message String to print to stdout
 */

function displayMessage(message) {
    // Write to STDOUT
    process.stdout.write(message);
}

module.exports = displayMessage;
