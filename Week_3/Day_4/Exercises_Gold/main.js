//--------------------EXERCISE 1:--------------------

let userInput = prompt("Which language do you speak?").toLowerCase();

switch (userInput) {
    case "french":
        alert("Bonjoir!");
        break;
    case "english":
        alert("Hello!");
        break;
    case "hebrew":
        alert("Shalom!");
        break;
    default:
        alert("01110011 01101111 01110010 01110010 01111001");
}

//--------------------EXERCISE 2:--------------------

userInput = Number(prompt("Which grade do you have(0-100)?"));

if (userInput < 70) {
    alert("D");
}
else if (userInput <= 80) {
    alert("C");
}
else if (userInput <= 90) {
    alert("B");
} 
else {
    alert("A");
}

//--------------------EXERCISE 3:--------------------

userInput = prompt("Enter the verb:");
let length = userInput.length;
let endWithM = userInput.endsWith("m");
let pattern = "ing";

if (length < 3) {
    alert(userInput);
} 
else if (length >= 3) {
    if (userInput.endsWith(pattern)) {
        userInput = userInput.concat("ly");
    }
    else {
        userInput = userInput.concat(endWithM ? "ming" : "ing");
    }
    alert(userInput);
}
