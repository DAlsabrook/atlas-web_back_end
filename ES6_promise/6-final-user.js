import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((results) => results.map((result, index) => {
      if (index === 0) { // signUpUser
        return {
          status: result.status,
          value: result.status === 'fulfilled' ? result.value : `User creation error: ${result.reason.message}`,
        };
      } else { // uploadPhoto
        return {
          status: result.status,
          value: result.status === 'rejected' ? result.reason.message : `Photo uploaded: ${result.value}`,
        };
      }
    }));
}
