import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    if (Pricing.validate(amount, 'amount')) {
      this._amount = amount;
    }
    if (Pricing.validate(currency, 'currency')) {
      this._currency = currency;
    }
  }

  get amount() {
    return this._amount;
  }

  set amount(newAmount) {
    if (Pricing.validate(newAmount, 'amount')) {
      this._amount = newAmount;
    }
  }

  get currency() {
    return this._currency;
  }

  set currency(newCurrency) {
    if (Pricing.validate(newCurrency, 'currency')) {
      this._currency = newCurrency;
    }
  }

  static validate(arg, type) {
    if (type === 'amount' && typeof arg !== 'number') {
      throw new TypeError('Amount must be a number.');
    }
    if (type === 'currency' && !(arg instanceof Currency)) {
      throw new TypeError('Currency must be an instance of Currency.');
    }
    return true;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number') {
      throw new TypeError('Amount must be a number.');
    }
    if (typeof conversionRate !== 'number') {
      throw new TypeError('Conversion Rate must be a number');
    }
    return amount * conversionRate;
  }
}
