#!/usr/bin/node
const fs = require('fs');
// const path = require('path');

function concatFiles (sourceFilePath1, sourceFilePath2, destinationFilePath) {
  const content1 = fs.readFileSync(sourceFilePath1, 'utf8');
  const content2 = fs.readFileSync(sourceFilePath2, 'utf8');

  const concated = content1 + content2;

  fs.writeFileSync(destinationFilePath, concated, 'utf8');
}

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js <sourceFilePath1> <sourceFilePath2> <destinationFilePath>');
  process.exit(1);
}

const [, , sourceFilePath1, sourceFilePath2, destinationFilePath] = process.argv;
concatFiles(sourceFilePath1, sourceFilePath2, destinationFilePath);
