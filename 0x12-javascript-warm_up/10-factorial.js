#!/usr/bin/node
function rec (a) {
  if (a === 1 || isNaN(a)) {
    return 1;
  }
  else {
    return a * rec(a - 1);
  }
}
console.log(rec(parseInt(process.argv[2])));
