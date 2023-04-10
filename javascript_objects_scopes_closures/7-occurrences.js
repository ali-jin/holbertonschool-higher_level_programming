#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  let occ;

  for (occ of list) {
    if (occ === searchElement) {
      counter++;
    }
  }
  return counter;
};
