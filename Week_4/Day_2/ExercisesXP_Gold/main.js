//--------------------EXERCISE 1:--------------------

console.log("=============\nExercise 1: Is_Blank\n=============");

let isBlank = text => text === "";

console.log("'' is blank? " + isBlank(""));
console.log("'abc' is blank? " + isBlank("abcd"));

//--------------------EXERCISE 2:--------------------

console.log("=============\nExercise 2: Abbrev_name\n=============");

function abbrevName(fullName) {
    let pattern = /[^A-Z][a-z]*$/;
    return fullName.replace(pattern, ".");
}

let someName = "Robin Singh";
console.log("Given name: " + someName);
console.log(abbrevName(someName));

//--------------------EXERCISE 3:--------------------

console.log("=============\nExercise 3: SwapCase\n=============");

let userStr = prompt('Give me a sentence, please: ');

function swapCase(userStr) {
        let result = '';
        let pattern = /[a-z]/;
    for (let i=0; i < userStr.length; i++) {
         result += userStr[i].match(pattern) !== null ? userStr[i].toUpperCase() : userStr[i].toLowerCase();
    }
    return result;
}

console.log(swapCase(userStr));

//--------------------EXERCISE 4:--------------------

console.log("=============\nExercise 4: Omnipresent Value\n=============");

let numArray = [[1, 0], [1, 0], [0, 1], [6, 0]];
let valueToCheck = 0;

function isOmnipresent(_numArray, valueToCheck) {
    for (let i = 0; i < _numArray.length; i++) {
        let checker = 0;
        for (let z = 0; z < _numArray[i].length; z++) {
            if (valueToCheck != _numArray[i][z]) {
                checker++;
            }
            if (checker == _numArray[i].length) {
                return false;
            }
        }
    }
    
    return true;
}

console.log(`Array: [ ${numArray.join(" | ")} ]`)
console.log(`Value to check: ${valueToCheck}`)
console.log(isOmnipresent(numArray, valueToCheck));