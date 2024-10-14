const fs = require('fs');

function countStudents(path) {
    const file = fs.readFileSync(path, 'utf8', (err, data) => {
        if (err) {
            process.stdout('Cannot load the database')
        };
    }).trim();
    let lineCount = -1; // Removes column description line
    let studentsInField = {};
    file.split('\n').forEach(line => {
        lineCount += 1;
        const column = line.split(',');
        process.stdout.write(`\tColumn: ${column[1]}\n`)
    })
    process.stdout.write(`Number of students: ${lineCount.toString()}\n`);

}
countStudents('./database.csv')
module.exports = countStudents;
