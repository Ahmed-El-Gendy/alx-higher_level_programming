#!/usr/bin/node
if (!isNaN(process.argv[2])) {
  let x = 1;
  for (let i = 1; i <= parseInt(process.argv[2]); i++) {
    x *= i;
  }
  console.log(x);
} else {
  console.log(1);
}
