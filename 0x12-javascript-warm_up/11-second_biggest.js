#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const numArr = process.argv.slice(2).map(function (a) { return (parseInt(a)); });
  const secBig = numArr.sort(function (a, b) { return b - a; })[1];
  console.log(secBig);
}
