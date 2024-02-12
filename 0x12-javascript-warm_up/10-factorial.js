#!/usr/bin/node
let x = 1;
function rec (a) {
  if (a === 1) {
    return;
  }
  x *= a;
  rec (a - 1);
}
if (!isNaN(process.argv[2])) {
  x = parseInt(process.argv[2]);
  rec (x - 1);
  console.log(x);
} else {
  console.log(1);
}
