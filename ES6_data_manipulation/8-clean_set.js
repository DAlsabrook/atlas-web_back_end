export default function cleanSet(set, startString) {
  let returnString = '';
  set.forEach(element => {
    if (element.startsWith(startString) && startString !== '') {
      returnString += '-' + element.slice(startString.length);
    }
  });
  return returnString.slice(1);
}
