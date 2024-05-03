export default class Currency {
  constructor(code, name) {
    if (Currency.validate(code, 'code')) {
      this._code = code;
    }
    if (Currency.validate(name, 'name')) {
      this._name = name;
    }
  }

  get code() {
    return this._code;
  }

  set code(newCode) {
    if (Currency.validate(newCode, 'code')) {
      this._code = newCode;
    }
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    if (Currency.validate(newName, 'name')) {
      this._name = newName;
    }
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }

  static validate(arg, attr) {
    if (typeof arg !== 'string') {
      if (attr === 'name') {
        throw new TypeError('Name must be a string');
      } else if (attr === 'code') {
        throw new TypeError('Code must be a string');
      }
    }
    return true;
  }
}
