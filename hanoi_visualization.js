function topR(a) {
  return Number(a.substring(a.lastIndexOf(' ')).trim());
}

function belowR(b) {
  return b.replace(topR(b),'').trim();
}

function printRings(p, c1, c2, c3){
  console.log("Phase "+p+":");
  console.log("          "+c1.trim());
  console.log("          "+c2.trim());
  console.log("          "+c3.trim());
  console.log(" ");
}

console.clear();

var n = 8;  // number of rings, 9 is maximum!
var A = "";
var B = "";
var C = "";
var lastR = n;

while (1 <= n) {
  A += ' '+n;
  n--;
}

var i = 1;
var arr = [A,B,C];

while(i < 600 && lastR > 0){
  if(lastR != topR(A) && topR(A) != 0 && topR(A) < topR(C) || topR(C) == 0 && lastR != topR(A)){
    printRings(i, A, B, C);
    lastR = topR(A);
    C += " "+topR(A);
    A = belowR(A);
    i++;
  }
  else if(lastR != topR(A) && topR(A) != 0 && topR(A) < topR(B) || topR(B) == 0 && lastR != topR(A)){
    printRings(i, A, B, C);
    lastR = topR(A);
    B += " "+topR(A);
    A = belowR(A);
    i++;
  }
  else{
    var c = C;
    C = B;
    B = A;
    A = c;
  }
  arr = [A,B,C];
}