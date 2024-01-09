#!/usr/bin/node
const dict = require('./101-data').dict;

const totaList = Object.entries(dict);
const vals = Object.values(dict);
const uniqData = [...new Set(vals)];
const newDict = {};
for (const val in uniqData) {
  const lst = [];
  for (const ky in totaList) {
    if (totaList[ky][1] === uniqData[val]) {
      lst.unshift(totaList[ky][0]);
    }
  }
  newDict[uniqData[val]] = lst;
}
console.log(newDict);
