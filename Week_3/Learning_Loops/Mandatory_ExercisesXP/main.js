//--------------------EXERCISE 1:--------------------

console.log("=============\nExercise 1: List Of People\n============="); 

console.log("------\nPart I\n------");

let people = ["Greg", "Mary", "Devon", "James"];
console.log("\nSource array: " + people.toString());


people.splice(people.indexOf("Greg"), 1);
console.log("\nRemove 'Greg' from array: " + people.toString());

people[people.indexOf("James")] = "Jason";
console.log("\nChange 'James' to 'Jason': " + people.toString());

people.push("Vitalii");
console.log("\nAdding my name to the end of the array: " + people.toString());

console.log("Finding index of 'Mary': " + people.indexOf("Mary"));

let slisedArray = people.slice(1, people.length - 1);
console.log("\nCopy array without 'Mary' and my name: " + slisedArray.toString());

console.log("\nFinding index of 'Foo': " + slisedArray.indexOf("Foo"));
console.log("It returned -1 because there is no such element in the array.");

let last = slisedArray[slisedArray.length - 1];
console.log("\nLast element of the slicedArray array: " + last);
console.log("Last element of the array has a value 'arrayLength - 1'");

console.log("------\nPart II\n------");


console.log("\nDisplay each element of 'people' array:\n");
for (x in people) {
    console.log(people[x]);
}


console.log("\nDisplay each element of 'people' array till 'Jason':\n");
x = 0;
do {
    console.log(people[x]);
    x++;
} 
while (x != people.indexOf("Jason") + 1) {
    
}

//--------------------EXERCISE 2:--------------------

console.log("=============\nExercise 2: Your Favorite Colors\n=============");

let colors = ["green", "olive", "blue", "black", "purple"];

console.log("\nFirst colors array: ");
for (x in colors) {
    let currentNumber = Number(x) + 1;
    console.log(`My #${currentNumber} choice is ${colors[x]}`);
}

console.log("\nSecond colors array(with suffixes): ");
let suffixes = ['st', 'nd', 'rd', 'th'];
for (x in colors) {
    let currentNumber = Number(x) + 1;
    let currentSuffix = x > 2 ? suffixes[suffixes.length-1] : suffixes[x];
    console.log(`My ${currentNumber}${currentSuffix} choice is ${colors[x]}`);
}

//--------------------EXERCISE 3:--------------------

let marker = true;
let userInput = Number(prompt("Enter the number:"));

while(marker) {
    if (!isNaN(userInput)) {
        if (userInput < 10) {
            userInput = Number(prompt("Enter the number:"));
        }
        else {
            break;
        }
    }
    else {
        userInput = Number(prompt("Enter the NUMBER:"));
    }
}

//--------------------EXERCISE 4:--------------------

console.log("=============\nExercise 4 : Building Management\n=============");

let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },
}

console.log(`\nNumber of floors: ${building.numberOfFloors}`);

let firstAndThirdFloors = building.numberOfAptByFloor.firstFloor + building.numberOfAptByFloor.thirdFloor;
console.log(`\nNumber of apartments on floors 1 and 3: ${firstAndThirdFloors}`);

let secondTenant = building.nameOfTenants[1];
let secondTenantLower = secondTenant.toLowerCase();
let secondTenantRent = building.numberOfRoomsAndRent.dan[0];

console.log(`\nName of the second tenant: ${secondTenant}
Number of his rooms: ${secondTenantRent}`)

let sarahAndDavidRent = building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1];
let danRent = building.numberOfRoomsAndRent.dan[1];
if (sarahAndDavidRent > danRent) {
    building.numberOfRoomsAndRent.dan[1] = 1200;
}
console.log("\nCurrent Dan's rent: " + building.numberOfRoomsAndRent.dan[1])

//--------------------EXERCISE 5:--------------------

console.log("=============\nExercise 5 : Family\n=============");

let family = {
    'mother': 'Sarah',
    'father': 'Tony',
    'son': 'Elliot',
    'dog': 'Cherry',
}

console.log("\nKeys of the object:");
for (x in family) {
    console.log(x);
}

console.log("\nValues of the object:");
for (x in family) {
    console.log(family[x]);
}

//--------------------EXERCISE 6:--------------------

console.log("=============\nExercise 6\n=============");

let details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }
let result = "";

for (x in details) {
    result += x + " " + details[x] + " ";
}
console.log(result);

//--------------------EXERCISE 7:--------------------

console.log("=============\nExercise 7 : Secret Group\n=============");

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let sortedNames = names.sort();
result = "";

for (x in sortedNames) {
    result += sortedNames[x][0];
}
console.log(result);