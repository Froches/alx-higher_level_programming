#!/usr/bin/node
const x = Number(process.argv[2]);

if (x === undefined || isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
