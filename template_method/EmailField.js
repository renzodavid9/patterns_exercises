const Field = require('./Field.js');

class EmailField extends Field {
  constructor(value, maxLength = 100, minLength = 10) {
    super();
  }

  isValidValue() {
    console.log('Validating email!');
    return true;
  }
}

module.exports = EmailField;