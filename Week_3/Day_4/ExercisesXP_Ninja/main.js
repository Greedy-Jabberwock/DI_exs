//--------------------EXERCISE 1:--------------------

console.log("=============\nExercise 1: Age Difference\n============="); 

let youngerYear = 2019;
let olderYear = 1976;
let testYear = 2022;
let youngerAge = testYear - youngerYear;
let olderAge = testYear - olderYear;

console.log(`Current year: ${testYear}
    \nYounger born in ${youngerYear}, and he is ${youngerAge} years old.
    \nOlder born in ${olderYear}, and he is ${olderAge} years old.`);

while (youngerAge != olderAge/2) {
    youngerAge++;
    olderAge++;
}

let result = youngerAge + youngerYear;
console.log(`\nSo younger one will be exactly half younger than older in ${result}.`);

//--------------------EXERCISE 2:--------------------

console.log("\n=============\nExercise 2: Zip Codes\n============="); 

console.log("\n----------\nWithout regular expression\n----------\n"); 

let zipcode = String(prompt("Enter your zip-code:"));

if (!isNaN(Number(zipcode)) && zipcode >= 0 && String(zipcode).length <= 5) {
    console.log("Success.");
}
else {
    console.log("Error.")
}


console.log("\n----------\nWith the regular expression\n----------\n"); 

let pattern = /\b\d{1,5}\b/;
console.log("Regular expression: " + pattern);

if (zipcode.match(pattern)) {
    console.log("Success!");
}
else {
    console.log("Error.")
}

//--------------------EXERCISE 3:--------------------

console.log("\n=============\nExercise 3: Secret Word\n============="); 

let userPrompt = prompt("Enter the word:");
pattern = /[a,e,i,o,u]/gi;

console.log("User prompt: " + userPrompt);
console.log("Without vowels: " + (userPrompt.replace(pattern, '')));
console.log("Replace vowels: " + (userPrompt.replace(pattern, '?')))