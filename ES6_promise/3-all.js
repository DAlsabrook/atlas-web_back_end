import { uploadPhoto, createUser } from './utils.js';

export default function handleProfilesSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then(([photo, user]) => console.log(`${user.body} ${user.firstName} ${user.lastName}`))
    .catch(() => console.log('Signup system offline'));
}
