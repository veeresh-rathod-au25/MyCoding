// problem 1

function multiply(num1, num2) {
  return num1 * num2;
}

var num1 = 12;
var num2 = 10;

var res = multiply(num1, num2);
console.log(res);

// [problem 2]

var n1 = 10;
var n2 = 2;

function multy(n1) {
  function double(n2) {
    return n1 * n2;
  }
  return double;
}

var multiplyRes = multy(n1);
console.log(multiplyRes);
var twiceNumber = multiplyRes(n2);
console.log(twiceNumber);
