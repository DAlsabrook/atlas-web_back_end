export default function getResponseFromAPI() {
  const p = new Promise((resolve, reject) => {
    if (1 === 1) {
      resolve(true);
    } else {
      reject(false);
    }
  })
  return p;
}
