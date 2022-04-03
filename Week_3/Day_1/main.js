
//--------------------INTRODUTION TO JAVASCRIPT--------------------------------

console.log("-----------Introdution to JavaScript:-----------\n");

// Exercise 1

console.log("\nExercise 1:");
let addressNumber, addressStreet, country, globalAddress;
addressNumber = 6;
addressStreet = "Sderot Herzl";
country = "Israel";
globalAddress = "I live in " + addressStreet + " " + addressNumber +
    ", in " + country;
console.log(globalAddress);

// Exercise 2

console.log("\nExercise 2:");
let birthYear = 1994;
let futureYear = 2023;
result = "I will be " + (futureYear - birthYear) + " in " + futureYear;
console.log(result);

//--------------------JAVASCRIPT ARRAYS--------------------------------

console.log("\n-----------JavaScript arrays-----------\n");

// Exercise 3
console.log("\nExercise 3:");
let pets = ['cat', 'dog', 'fish', 'rabbit', 'cow'];
console.log(pets[1]);
pets.splice(3, 1, "horse");
console.log(pets.length);