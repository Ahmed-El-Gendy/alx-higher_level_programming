#!/usr/bin/node
const myVar = process.argv.length;
if (myVar <= 3) {
  console.log(0);
} else {
  let x = -10000000000;
  for (let i = 2; i < myVar; i++) {
    if (parseInt(process.argv[i]) > x) {
      x = parseInt(process.argv[i]);
    }
  }
  let y = -10000000000;
  for (let i = 2; i < myVar; i++) {
    if (parseInt(process.argv[i]) > y && parseInt(process.argv[i]) < x) {
      y = parseInt(process.argv[i]);
    }
  }
  console.log(y);
}
