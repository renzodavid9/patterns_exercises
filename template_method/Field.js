class Field {
  constructor(value='', maxLength = 100, minLength = 10) {
    this.value = value;
    this.maxLength = maxLength;
    this.minLength = minLength;
  }

  isEmpty() {
    return this.value
  }

  hasValidLenght() {
    const valueLenght = this.value.length;
    return valueLenght >= this.minLength && valueLenght <= this.maxLength;
  }

  validate() {
    this.isEmpty();
    this.hasValidLenght();
    this.isValidValue();
  }
}

module.exports = Field;