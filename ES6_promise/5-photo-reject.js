export default function uploadPhoto(filename) {
  if (typeof filename !== 'string') {
    throw new Error('Filename must be string');
  }
  return new Promise.reject(console.log(`${filename} cannot be processed`));
}
