#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const x = parseInt(process.argv[2]);
  for (let n = 0; n < x; n++) {
    console.log('C is fun');
  }
}
