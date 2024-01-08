#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let nm = 0; nm < x; nm++) {
    theFunction();
  }
};
