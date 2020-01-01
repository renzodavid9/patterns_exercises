const EmailField = require('./EmailField.js');
const NumberField = require('./NumberField.js');

class Main {
  constructor(fields) {
    this.fields_ = fields;
  }

  run() {
    this.fields_.map((field) => {
      field.validate();
    });
  }
}

const main = new Main([
    new EmailField(),
    new NumberField(),
]);
main.run();