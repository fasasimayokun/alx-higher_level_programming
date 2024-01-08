#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const nm = Number(process.argv[2]);
  for (let x = 0; x < nm; x++) {
    console.log('X'.repeat(nm));
  }
}
