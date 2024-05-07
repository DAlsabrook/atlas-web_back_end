export default function createInt8TypedArray(length, position, value) {
  let ab = new ArrayBuffer(length); //Arraybuffer() takes in its size in bytes
  const view = new Int8Array(ab); //creatte a data view to look at and change ab
  view.setInt8(position, value); // set new number in array buffer
}
