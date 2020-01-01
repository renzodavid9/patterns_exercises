const Field = require('./Field.js');

class NumberField extends Field{
  constructor(value, maxLength = 100, minLength = 10) {
    super();
  }

  isValidValue() {
    console.log('Validating number!');
    return false;
  }
}

module.exports = NumberField;