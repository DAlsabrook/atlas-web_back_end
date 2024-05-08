import uploadPhoto from './utils.js';
import createUser from './utils.js';

export default function handleProfilesSignup(){
  return createUser
    .then(() => console.log(`${createUser.body} ${createUser.firstName} ${createUser.lastName}`))
    .catch(() => console.log('Signup system offline'));
}
