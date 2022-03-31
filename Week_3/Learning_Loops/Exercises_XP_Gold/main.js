//--------------------EXERCISE 1:--------------------

console.log("=============\nExercise 1: Divisible By Three\n============="); 

let numbers = [123, 8409, 100053, 333333333, 7];

for (x in numbers) {
    console.log(`Is ${numbers[x]} divided by 3: ${numbers[x] % 3 == 0}`);
}

//--------------------EXERCISE 2:--------------------

console.log("\n=============\nExercise 2: Attendance\n============="); 

let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
  }

let studentName = String(prompt("Student, enter your name:"));

if (studentName in guestList) {
    console.log(`\nHi! I'm ${studentName}, and I'm from ${guestList[studentName]}.`);
}
else {
    console.log("\nHi! I'm a guest.");
}

//--------------------EXERCISE 3:--------------------

console.log("\n=============\nExercise 3: Playing With Numbers\n============="); 

let age = [20,5,12,43,98,55];
let sum = 0;
let highestAge = 0;

for (x in age) {
    sum += age[x];
    
    if (age[x] > highestAge) {
        highestAge = age[x];
    }
}

console.log(`\nSumm of the all elements in the 'age' array: ${sum}`);
console.log(`Highest age in the array: ${highestAge}`);
