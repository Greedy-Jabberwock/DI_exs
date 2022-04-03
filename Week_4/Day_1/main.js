//--------------------EXERCISE 1:--------------------

console.log("=============\nExercise 1\n=============");

function parentsAges(childAge) {
    let momAge = childAge * 2;
    let dadAge = (momAge * 1.2).toFixed(0);
    console.log(`Your age is ${childAge}
\rYour mom's age is ${momAge}
\rYour dad's age is ${dadAge}`);
}

let myAge = 28;
parentsAges(myAge);

//--------------------EXERCISE 2:--------------------

console.log("=============\nExercise 2\n=============");

function motherAge(childAge) {
    return childAge*2;
}

childAge = 12;
let momAge = motherAge(childAge);
console.log(`If child is ${childAge} years old, then his mom is ${momAge} years old.`);