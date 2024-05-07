export default function updateStudentGradeByCity(studentsList, city, newGrades) {
  return studentsList
    // Filter the list of students to only from specified city
    .filter(student => student.location === city)
    // Map the filtered list to a new array
    .map(student => {
      // Find the grade object for the current student in the newGrades array
      const gradeObj = newGrades.find(grade => grade.studentId === student.id);
      // Return a new object that includes all properties of the current student
      // and a grade property that is either the new grade or 'N/A' if no new grade was found
      return {
        ...student,
        grade: gradeObj ? gradeObj.grade : 'N/A',
      };
    });
}
