const fs = require('fs');

function readDatabase(path) {
    return new Promise((resolve, reject) => {
        fs.readFile(path, 'utf8', (err, data) => {
            if (err) {
                reject(new Error('Cannot load the database'));
                return;
            }

            const fileLines = data.trim().split('\n');
            if (fileLines.length <= 1) {
                resolve({});
                return;
            }

            const studentsInField = {};

            fileLines.slice(1).forEach((line) => {
                const columns = line.split(',');
                const field = columns[3].trim();
                const firstName = columns[0].trim();
                if (!studentsInField[field]) {
                    studentsInField[field] = [];
                }
                studentsInField[field].push(firstName);
            });

            resolve(studentsInField);
        });
    });
}

module.exports = readDatabase;
