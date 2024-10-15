const http = require('http');
const fs = require('fs');
const url = require('url');

// Function to read students from a CSV file asynchronously
function countStudents(path, callback) {
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      callback('Cannot load the database', null);
      return;
    }

    const fileLines = data.trim().split('\n');
    if (fileLines.length <= 1) {
      callback(null, 'No students found in the database');
      return;
    }

    let lineCount = 0;
    const studentsInField = {};

    fileLines.slice(1).forEach((line) => {
      lineCount += 1;
      const columns = line.split(',');
      const field = columns[3].trim();
      const firstName = columns[0].trim();
      if (!studentsInField[field]) {
        studentsInField[field] = [];
      }
      studentsInField[field].push(firstName);
    });

    let result = `Number of students: ${lineCount}\n`;
    for (const [field, studentsList] of Object.entries(studentsInField)) {
      result += `Number of students in ${field}: ${studentsList.length}. List: ${studentsList.join(', ')}\n`;
    }

    callback(null, result.trim());
  });
}

// Create the HTTP server
const app = http.createServer((req, res) => {
  const path = url.parse(req.url).pathname;
  const databaseName = process.argv[2];
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (path === '/') {
    res.end('Hello Holberton School!');
  } else if (path === '/students') {
    res.write('This is the list of our students\n');
    countStudents(databaseName, (err, result) => {
      if (err) {
        res.end(err);
      } else {
        res.end(result);
      }
    });
  }
}).listen(1245);

// Export the server
module.exports = app;
