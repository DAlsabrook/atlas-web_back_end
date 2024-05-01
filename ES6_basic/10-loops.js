function appendToEachArrayValue(array, appendString) {
  for (let idx of array.keys()) {
    array[idx] = appendString + array[idx];
  }

  return array;
}

console.log(appendToEachArrayValue(['appended', 'fixed', 'displayed'], 'correctly-'));
