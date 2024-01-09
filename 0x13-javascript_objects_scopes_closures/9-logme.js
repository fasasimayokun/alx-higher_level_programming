#!/usr/bin/node
let nwArg = 0;

exports.logMe = function (item) {
  console.log(nwArg + ': ' + item);
  nwArg++;
};
