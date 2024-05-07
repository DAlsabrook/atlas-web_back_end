export default function createInt8TypedArray(length, position, value) {
  if (position > (length - 1)) {
    throw new Error('Position outside range');
  }
  let ab = new ArrayBuffer(length); //Arraybuffer() takes in its size in bytes
  let view = new Int8Array(ab); //creatte a data view to look at and change ab
  view[position] = value; // set new number in array buffer
  return view;
}
