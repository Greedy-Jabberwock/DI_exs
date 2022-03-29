//--------------------EXERCISE 1:--------------------

console.log("=============\nExercise 1:\n============="); 

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];

fruits.shift();                 // remove first element
fruits.sort();                  // sorting array
fruits.push("Kiwi");            // adding element to the end of the array
fruits.splice(0, 1);            // another method to delete first element
fruits.reverse();               // reversing array

console.log(fruits); 

//--------------------EXERCISE 2:--------------------

console.log("=============\nExercise 2:\n============="); 

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];

console.log(moreFruits[1][1][0])