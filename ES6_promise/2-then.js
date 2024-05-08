export default function handleResponseFromAPI(promise) {
  promise.then(() => {
    console.log('Got a response from the API');
  }).catch(() => {
    return new Error();
  });
  return { body: 'success', status: 200 };
}
