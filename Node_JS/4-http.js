const http = require('http');

const app = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
}).listen(1245);

module.exports = app;


// got this to look at after work when i get home:
// https://stackoverflow.com/questions/5998694/how-to-create-an-https-server-in-node-js
// https://nodejs.org/api/https.html#httpscreateserveroptions-requestlistener
