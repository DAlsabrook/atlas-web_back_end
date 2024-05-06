// Import the Currency class from another module
import Currency from './3-currency';

// Define a new class called Pricing
export default class Pricing {
  // The constructor takes two arguments: amount and currency
  constructor(amount, currency) {
    // Validate the amount and currency before setting them
    if (Pricing.validate(amount, 'amount')) {
      this._amount = amount;
    }
    if (Pricing.validate(currency, 'currency')) {
      this._currency = currency;
    }
  }

  // Getter for the amount
  get amount() {
    return this._amount;
  }

  // Setter for the amount, with validation
  set amount(newAmount) {
    if (Pricing.validate(newAmount, 'amount')) {
      this._amount = newAmount;
    }
  }

  // Getter for the currency
  get currency() {
    return this._currency;
  }

  // Setter for the currency, with validation
  set currency(newCurrency) {
    if (Pricing.validate(newCurrency, 'currency')) {
      this._currency = newCurrency;
    }
  }

  // Static method to validate the amount and currency
  static validate(arg, type) {
    if (type === 'amount' && typeof arg !== 'number') {
      throw new TypeError('Amount must be a number.');
    }
    if (type === 'currency' && !(arg instanceof Currency)) {
      throw new TypeError('Currency must be an instance of Currency.');
    }
    return true;
  }

  // Method to display the full price
  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  // Static method to convert the price
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
