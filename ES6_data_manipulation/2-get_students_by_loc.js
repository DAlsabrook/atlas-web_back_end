export default function getStudentsByLocation(studentsList, city) {
  if (!(studentsList instanceof Array) && typeof city === 'string') {
    return [];
  }
  return studentsList.filter((students) => students.location === city);
}
