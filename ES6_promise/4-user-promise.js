export default function signUpUser(firstNameValue, lastNameValue) {
  return Promise.resolve({
    firstName: firstNameValue,
    lastName: lastNameValue,
  });
}
