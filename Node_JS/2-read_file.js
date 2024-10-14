const fs = require('fs');

function countStudents(path) {
  const file = fs.readFileSync(path, 'utf8', (err) => {
    if (err) {
      process.stdout('Cannot load the database');
    }
  }).trim();
  let lineCount = 0;
  const studentsInField = {};
  const fileLines = file.split('\n');
  fileLines.slice(1).forEach((line) => {
    lineCount += 1;
    const column = line.split(',');
    const field = column[3].trim();
    const firstName = column[0].trim();
    if (!studentsInField[field]) {
      studentsInField[field] = [];
    }
    studentsInField[field].push(firstName);
  });

  // process.stdout.write(JSON.stringify(studentsInField) + "\n")
  for (const [field, studentsList] of Object.entries(studentsInField)) {
    process.stdout.write(`Number if students in ${
      field
    }: ${
      studentsList.length
    }. List: ${
      studentsList.join(', ')}\n`);
  }
  process.stdout.write(`Number of students: ${lineCount.toString()}\n`);
}
countStudents('./database.csv');
module.exports = countStudents;
