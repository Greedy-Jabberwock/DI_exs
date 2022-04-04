//--------------------EXERCISE 1:--------------------

console.log("=============\nExercise 1: Random Number\n=============");

let randNumber = () => {
    let range = (Math.random() * 101).toFixed();
    console.log(`Random number is: ${range}`);
    for (let i = 0; i < range; i++) {
        if (!(i%2)) {
            console.log(i);
        }
    };
};

randNumber();


//--------------------EXERCISE 2:--------------------

console.log("\n=============\nExercise 2: Capitalized Letters\n=============");

let testString = 'cafasfaga';

function capitalize(someString) {
    let capitalizeEven = '';
    let capitalizeOdd = '';

    for (let x = 0; x < someString.length; x++) {
        if (x % 2) {
            capitalizeOdd += someString[x].toUpperCase();
            capitalizeEven += someString[x];
        }
        else
        {
            capitalizeOdd += someString[x];
            capitalizeEven += someString[x].toUpperCase();
        }
    }

    return [capitalizeEven, capitalizeOdd];
}

console.log(capitalize(testString));

//--------------------EXERCISE 3:--------------------

console.log("\n=============\nExercise 3: Is Palindrome?\n=============");

testString = "cooolllloooc";

function isPalindrome (someString) {
    someString = someString.toLowerCase();
    for (let i = 0; i < someString.length; i++) {
        if (someString.at(i) != someString.at(-(i+1))) {
            return "not a palindrome."
        }
    }
    return "a palindrome.";
} 

console.log(`${testString} is ${isPalindrome(testString)}`);

//--------------------EXERCISE 4:--------------------

console.log("\n=============\nExercise 4: Biggest Number\n=============");

const numbersArray = [1, "300", -97, "a", 200, 0];
let biggest = 0;

numbersArray.forEach((item) => {
    if (typeof item == "number") {
        biggest = biggest <= item ? item : biggest;
    }
});

console.log(`Current array: ${numbersArray.join(" | ")}`);
console.log(`Biggest number is: ${biggest}`);


//--------------------EXERCISE 5:--------------------

console.log("\n=============\nExercise 5: Unique Elements\n=============");

let list=[1,2,3,'3',3,'r',4,5, 7, 7, 0, 1, 2, -2, 7, 9];
let uniuqueValues = [];

list.forEach((item) => {
    let marker = 0;
    for (let i = 0; i < uniuqueValues.length; i++)
    {
        if (uniuqueValues[i] == item)
        {
            marker++;
        }
    }
    if (marker == 0) {
        uniuqueValues.push(item);
    }
})

console.log(`Current array: [ ${list.join(", ")} ]`);
console.log(`List of unique values: [ ${uniuqueValues.sort().join(", ")} ]`);
