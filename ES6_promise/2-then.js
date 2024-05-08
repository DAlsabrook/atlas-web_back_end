export default function handleResponseFromAPI(promise) {
  promise.then(() => {
    console.log('Got a response from the API');
    return { body: 'success', status: 200 };
  }).catch(() => {throw new Error()});
}
