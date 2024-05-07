export default function getStudentIdsSum(studentList) {
  const initialValue = 0;
  return studentList.reduce(
    (accumulator, student) => accumulator + student.id,
    initialValue,
  );
}
