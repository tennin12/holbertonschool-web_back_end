import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((data) => {
      for (const res of data) {
        if (res.status === 'rejected') {
          res.value = `Error: ${res.reason.message}`;
          return res.reason;
        }
      }
      return data;
    });
}
