import handleProfileSignup from './6-final-user.js';
const result = handleProfileSignup('John', 'Doe', 'Gerald.jpg');
console.log(result);
result.then((resultResult) => console.log(resultResult));
