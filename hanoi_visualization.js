function topDisk(a) {
    return Number(a.substring(a.lastIndexOf(' '))); // top disk of a-rod
}

function belowPart(b) {
    return b.substring(0, b.lastIndexOf(' '));  // remaining part of disks on b-rod after removing top one
}

function printRods(p, c1, c2, c3) {
    console.log("Phase " + p + ":");   // print rods A B C
    console.log("          |" + c1.trim());
    console.log("          |" + c2.trim());
    console.log("          |" + c3.trim());
    console.log(" ");
}

console.clear();

function main(n) {
    var A = "";
    var B = "";
    var C = "";
    var tempDisk = "";
    var lastDisk = n;  // last moved disk to stop while loop

    while (n > 0) {
        A += ' ' + n;   // n disks for first rod
        n--;
    }

    var i = 1;  // limit for iterations in while loop below
    var arr = [A, B, C];

    while (i < 2500 && Number(lastDisk) > 0) {
        // console.log(topDisk(A)+" "+topDisk(B)+" "+topDisk(C));  // uncomment this if you need to see disks rotation
        if (lastDisk != topDisk(A) && topDisk(A) != 0 && topDisk(A) < topDisk(C) || topDisk(C) == 0 && lastDisk != topDisk(A)) {
            printRods(i, A, B, C);
            lastDisk = topDisk(A);
            C += " " + topDisk(A);  // moving disk from A to C
            A = belowPart(A);
            i++;
        } else if (lastDisk != topDisk(A) && topDisk(A) != 0 && topDisk(A) < topDisk(B) || topDisk(B) == 0 && lastDisk != topDisk(A)) {
            printRods(i, A, B, C);
            lastDisk = topDisk(A);
            B += " " + topDisk(A);  // moving disk from A to B
            A = belowPart(A);
            i++;
        } else {
            printRods(i, A, B, C);
            tempDisk = C;  // rotation of rods, shift to the right to one position
            C = B;
            B = A;
            A = tempDisk;
            i++;
        }
        arr = [A, B, C];
    }
}