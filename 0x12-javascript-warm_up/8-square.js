#!/usr/bin/node
const x = Number(process.argv[2]);

if (x === undefined || isNaN(x)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < x) {
    console.log('X'.repeat(x));
    i++;
  }
}
