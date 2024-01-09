#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let nm = 0;
  while ((len - nm) > 0) {
    const taux = list[len];
    list[len] = list[nm];
    list[nm] = taux;
    nm++;
    len--;
  }
  return list;
};
