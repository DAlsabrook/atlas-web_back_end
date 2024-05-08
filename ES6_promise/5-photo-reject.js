export default function uploadPhoto(filename) {
  if (typeof filename !== 'string') {
    throw new Error('Filename must be string');
  }
  return Promise.reject(new Error(`Error: ${filename} cannot be processed`));
}
