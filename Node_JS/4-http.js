const https = require('node:https');
const fs = require('node:fs');

const options = {
    key: fs.readFileSync('test/fixtures/keys/agent2-key.pem'),
    cert: fs.readFileSync('test/fixtures/keys/agent2-cert.pem'),
};

https.createServer(options, (req, res) => {
    res.writeHead(200);
    res.end('hello world\n');
}).listen(8000);

// got this to look at after work when i get home from:
// https://stackoverflow.com/questions/5998694/how-to-create-an-https-server-in-node-js
