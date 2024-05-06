import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    if (typeof sqft !== 'number') {
      throw new TypeError('sqft must be a number');
    }
    if (typeof floors !== 'number') {
      throw new TypeError('Floors must be a number');
    }
    this._sqft = sqft;
    this._floors = floors;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(newSqft) {
    if (typeof sqft !== 'number') {
      throw new TypeError('sqft must be a number');
    }
    this._sqft = newSqft;
  }

  get floors() {
    return this._floors;
  }

  set floors(newFloors) {
    if (typeof floors !== 'number') {
      throw new TypeError('Floors must be a number');
    }
    this._floors = newFloors;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
