#!/usr/bin/node
exports.converter = function (base) {
  if (typeof arguments[1] !== 'number' || isNaN(arguments[1])) {
    throw new Error('Invalid input. Please provide a valid number.');
  }

  const convertRecursive = (number, base) =>
    number === 0 ? '' : convertRecursive(Math.floor(number / base), base) + (number % base);

  return convertRecursive(arguments[1], base);
};
