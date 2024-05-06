// Define a class named Building
export default class Building {
  // The constructor takes one argument: sqft
  constructor(sqft) {
    // Check if the class being instantiated is Building
    // If it is, throw an error because Building is an abstract class and should not be instantiated directly
    if (this.constructor === Building) {
      throw new TypeError('Cannot instantiate abstract class.');
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

  // Method that should be overridden by any class that extends Building
  // If it's not overridden and this method is called, it will throw an error
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
