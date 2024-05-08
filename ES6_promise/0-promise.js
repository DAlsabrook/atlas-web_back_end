export default function getResponseFromAPI() {
  const p = new Promise((resolve, reject) => {
    if (true) {
      resolve(true);
    } else {
      reject(new Error('REJECTED NERD'));
    }
  })
  return p;
}
