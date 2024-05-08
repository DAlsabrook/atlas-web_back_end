import handleProfileSignup from './6-final-user.js';
const result = handleProfileSignup("Bob", "Dylan", "bob_dylan.jpg");
console.log(result);
result.then((resultResult) => console.log(resultResult));
