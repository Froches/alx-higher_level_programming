#!/usr/bin/node
exports.converter = function (base) {
  return function convertNumberToBase (number) {
    if (isNaN(number) || isNaN(base) || base < 2 || base > 36) {
      return 'Invalid input';
    }

    return number.toString(base);
  };
};
