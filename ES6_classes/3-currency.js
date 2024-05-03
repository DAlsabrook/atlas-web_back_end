export default class Currency {
  constructor(code, name) {
    if (this.validate(code, 'code')) {
      this._code = code;
    }
    if (this.validate(name, 'name')) {
      this._name = name;
    }
  }

  get code() {
    return this._code;
  }

  set code(newCode) {
    if (this.validate(newCode, 'code')) {
      this._code = newCode;
    }
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    if (this.validate(newName, 'name')) {
      this._name = newName;
    }
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
  
  validate(arg, attr) {
    if (typeof arg === 'string') {
      return true;
    } else {
      if (attr === 'name') {
        throw new TypeError('Name must be a string');
      } else if (attr === 'code') {
        throw new TypeError('Code must be a string');
      }
    }
  }
}
