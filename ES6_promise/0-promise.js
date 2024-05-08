export default function getResponseFromAPI() {
  const p = new Promise((resolve, reject) => {
    const a = 1 + 1;
    if (a === 2) {
      resolve(true);
    } else {
      reject(new Error('REJECTED NERD'));
    }
  });
  return p;
}
