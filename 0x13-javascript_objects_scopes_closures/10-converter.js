#!/usr/bin/node
exports.converter = function (base) {
  const numberToConvert = arguments[1];
  if (typeof numberToConvert !== 'number' || isNaN(numberToConvert)) {
    throw new Error('Invalid input. Please provide a valid number.');
  }

  const convertRecursive = (number, base) => {
    if (number === 0) {
      return '';
    } else {
      return convertRecursive(Math.floor(number / base), base) + (number % base);
    }
  };
  return convertRecursive(numberToConvert, base);
};
