export default function getFullResponseFromAPI(bool) {
  return new Promise((resolve, reject) => {
    if (bool === true) {
      resolve({ status: 200, body: 'Success' });
    } else if (bool === false) {
      reject(new Error('The fake API is not working currently'));
    }
  });
}
