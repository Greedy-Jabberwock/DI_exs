//--------------------EXERCISE 1:--------------------

console.log("=============\nExercise 1: Favorite color\n============="); 

let sentence = ["my","favorite","color","is","blue"];
console.log(sentence.join(" "));

//--------------------EXERCISE 2:--------------------

console.log("=============\nExercise 2: Mixup\n============="); 

let str_1 = "Java";
let str_2 = "Script";
let swapper = str_1.slice(0, 2);
str_1 = str_1.replace(str_1.slice(0, 2), str_2.slice(0, 2));
str_2 = str_2.replace(str_2.slice(0, 2), swapper);
let result = `${str_1} ${str_2}`
console.log(result);

//--------------------EXERCISE 3:--------------------

console.log("=============\nExercise 2: Calculator\n============="); 
let num1 = Number(prompt("Enter first number: "));
let sign = prompt('Enter the sign for calculation (+, -, /, *, ^)')
let num2 = Number(prompt("Enter second number: "));
let total;
switch (sign) {
    case "+":
        total = num1 + num2;
        break;
    case "-":
        total = num1 - num2;
        break;
    case "/":
        total = num1 / num2;
        break;
    case "*": 
        total = num1 * num2;
        break;
    case "^":
        total = Math.pow(num1, num2);
        break;
}
if (!isNaN(total)) {
    alert(`${num1} ${sign} ${num2} = ${total}`);
} else {
    alert("Something goes wrong.");
}
    