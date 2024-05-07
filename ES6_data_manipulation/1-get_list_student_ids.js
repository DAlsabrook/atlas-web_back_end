export default function getListStudentsIds(studentsList) {
  if (!(studentsList instanceof Array)) {
    return [];
  }
  return studentsList.map((students) => students.id);
}
