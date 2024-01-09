#!/usr/bin/node
const fls = require('fs');

const ftArg = fls.readFileSync(process.argv[2]).toString();
const sdArg = fls.readFileSync(process.argv[3]).toString();
fls.writeFileSync(process.argv[4], ftArg + sdArg);
