export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name === "string") {
      this._name = name;
    }
    if (typeof length === "number" && !isNaN(length)) {
      this._length = length;
    }
    if (typeof students === "object" && students.every(student => {typeof student === "string"})) {
      this._students = students;
    }
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName === "string") {
      this._name = newName;
    }
  }

  get length() {
    return this.length;
  }

  set length(newLength) {
    if (typeof newLength === "number" && !isNaN(newLength)) {
      this._length = newLength;
    }
  }

  get students() {
    return this._students;
  }

  set students(newStudents) {
    if (typeof newStudents === "object" && newStudents.every(student => { typeof student === "string" })) {
      this._students = newStudents;
    }
  }
}
