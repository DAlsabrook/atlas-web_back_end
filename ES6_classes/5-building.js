// Define a class named Building
export default class Building {
  // The constructor takes one argument: sqft
  constructor(sqft) {
    // Check if the method is there. If not throw an error
    if (this.constructor !== Building && !this.evacuationWarningMessage) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    // Check if sqft is a number, if not throw an error
    if (typeof sqft !== 'number') {
      throw new TypeError('Sqft must be a number.');
    }
    // Store sqft in an underscore attribute version
    this._sqft = sqft;
  }

  // Getter for sqft
  get sqft() {
    return this._sqft;
  }
}
