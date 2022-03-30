//--------------------EXERCISE 1:--------------------

console.log("=============\nExercise 1:\n============="); 

let x = 10;
let y = -75;

if (x == y) {
    console.log("Numbers are equal.");
} 
else if (x > y) {
    console.log("x is the biggest number.");
}
else {
    console.log("y is the biggest number.");
}

//--------------------EXERCISE 2:--------------------

console.log("=============\nExercise 2:\n============="); 

let newDog = "Chihuahua";

console.log(`How many letters in ${newDog}: ${newDog.length}`);
console.log(`To upper case: ${newDog.toUpperCase()}`);
console.log(`To lower case: ${newDog.toLowerCase()}`);

if (newDog == "Chihuahua") {
    console.log("I love Chihuahuas, it’s my favorite dog breed");
} 
else {
    console.log("I dont care, I prefer cats");
}

//--------------------EXERCISE 3:-------------------- 

console.log("=============\nExercise 3:\n============="); 

let userNumber = Number(prompt("Enter the number:"));
let errorString = "It's not a number";
let result = "Your number is ";

if (!isNaN(userNumber)) {
    if (userNumber == 0) {
        alert(`${result} zero.`)
    }
    else if (userNumber % 2 == 0) {
        alert(`${result} even.`)
    }
    else {
        alert(`${result} odd.`)
    }
}
else {
    alert(errorString);
}

//--------------------EXERCISE 4:--------------------

console.log("=============\nExercise 4:\n============="); 

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let usersArraysLength = users.length;

switch (true) {
    case usersArraysLength == 0:
        console.log("No one is online.");
        break;
    case usersArraysLength == 1:
        console.log(`${users.toString()} is online.`);
        break;
    case usersArraysLength == 2:
        console.log(`${users.join(", ")} are online.`);
        break;
    case usersArraysLength > 2:
        let firstTwoUsers = users.slice(0, 2);
        let additionalLength = usersArraysLength - firstTwoUsers.length;
        console.log(`${firstTwoUsers.join(", ")} and ${additionalLength} more are online.`);
        break;
}