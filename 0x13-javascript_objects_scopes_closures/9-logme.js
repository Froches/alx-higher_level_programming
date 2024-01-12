#!/usr/bin/node
let printedArgumentsCount = 0;

exports.logMe = function (item) {
  console.log(`${printedArgumentsCount}: ${item}`);
  printedArgumentsCount++;
};
