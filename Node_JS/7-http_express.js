const express = require('express')
const fs = require('fs');
const app = express()
const port = 1245

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

app.all('/', (req, res) => {
    res.send('Hello Holberton School!')
});

app.get('/students', (req, res) => {
    const databaseName = process.argv[2];
    countStudents(databaseName, (err, result) => {
        if (err) {
            res.send(err);
        } else {
            res.send(`This is the list of our students\n${result}`);
        }
    });
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
});

module.exports = app;
