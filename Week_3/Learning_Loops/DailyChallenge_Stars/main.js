//--------------------Using one loop:--------------------

console.log("=============\nUsing one loop:\n============="); 

let star = "*";
let pyramid = "";

for (let i = 0; i < 6; i++) {
    pyramid += star;
    console.log(pyramid);
}

//--------------------Using two loop:--------------------

console.log("=============\nUsing nested loop:\n============="); 

for (let i = 1; i < 7; i++) {
    pyramid = "";
    for (let z = 0; z < i; z++) {
        pyramid += star;
    }
    console.log(pyramid);
}
