const numbers = [5,0,9,1,7,4,2,6,3,8];

let arrayChanged = true;

console.log(numbers.toString())

while (arrayChanged) {
    let marker = 0;
    for (let i=0; i < numbers.length - 1; i++) {
        let swap;
        if (numbers[i] < numbers[i + 1]) {
            swap = numbers[i];
            numbers[i] = numbers[i + 1];
            numbers[i + 1] = swap;
            marker++;
        }
    }
    if (marker == 0) {
        arrayChanged = false;
    }
}

console.log(numbers.toString());
console.log(numbers.join('-$-'));
