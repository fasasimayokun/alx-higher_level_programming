#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (let nm = 0; nm < list.length; nm++) {
    if (searchElement === list[nm]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
