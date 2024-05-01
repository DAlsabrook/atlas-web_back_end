function createEmployeesObject(departmentName, employees) {
  const employeesObject = {};
  employeesObject[departmentName] = [...employees];

  return employeesObject;
}

console.log(createEmployeesObject("Software", ["Bob", "Sylvie"]));
