#!/usr/bin/node
const argument = process.argv[2];

if (!isNaN(argument)) {
  console.log('My number: ' + argument);
} else {
  console.log('Not a number');
}
