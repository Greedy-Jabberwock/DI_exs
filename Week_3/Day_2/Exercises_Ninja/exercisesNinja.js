//--------------------EXERCISE 1:--------------------

//console.log("=============\nExercise 1: Evaluation\n=============");

    5 >= 1          // true, both are numbers and 5 is bigger than 1
    0 === 1         // false, because both values are numbers, but doesn't equal
    4 <= 1          // false, because 4 is bigger than 1
    1 != 1          // false, because values are equal
    "A" > "B"       // false, because "A" has code 065 and "B" has code 066, so "B" is bigger
    "B" < "C"       // true, bacause "B" ASCII code (066) lesser then "C" ASCII code (067) 
    "a" > "A"       // true, because "a" has code 097 and "A" has code 065
    "b" < "A"       // false, because "b" has code 098 and "A" has code 065
    true === false  // false, because they both has boolean type, but their values are nor equal
    true != true    // false, because true == true.   

//--------------------EXERCISE 2:--------------------

console.log("=============\nExercise 2: Ask for numbers\n=============");

let userInputArray = prompt("Enter numbers, separated by comma.").split(",");
let arrayElementsSum = userInputArray.reduce(summArray);
function summArray(total, num) {
    return Number(total) + Number(num);
}
console.log(arrayElementsSum);

//--------------------EXERCISE 3:--------------------

console.log("=============\nExercise 3: Find Nemo\n=============");

let userSentence = prompt("Type a sentence with or without word 'Nemo'");
let indexOfNemo = userSentence.indexOf("Nemo");
if (indexOfNemo != -1) {
    console.log(`I found Nemo at ${indexOfNemo}`);
} else {
    console.log("I can’t find Nemo");
}

//--------------------EXERCISE 4:--------------------

console.log("=============\nExercise 4: Boom\n=============");

let boom = 'boom';
let userChoice = prompt("Enter a number, and you will see, what will happen.");
if (userChoice < 2) {
    alert(boom);
} 
else {
    boom = 'b' + 'o'.repeat(userChoice) + 'm';
    if (userChoice % 2 == 0) {
        boom = boom.concat("!");
    }
    if (userChoice % 5 == 0) {
        boom = boom.toUpperCase();
    }
    alert(boom);
}   
