import handleResponseFromAPI from "./2-then.js";

const promise = Promise.resolve();
console.log(handleResponseFromAPI(promise));
