export default function getStudentIdsSum(studentList) {
  const initialValue = 0;
  return studentList.reduce(
    (student, currentValue) => student.id + currentValue,
    initialValue,
  );
}
