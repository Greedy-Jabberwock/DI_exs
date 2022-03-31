//--------------------EXERCISE 1:--------------------

console.log("=============\nExercise 1\n============="); 

let rangeValue = 16;

for (let i = 0; i < rangeValue; i++) {
    console.log(`${i} is ${i % 2 == 0 ? "even" : "odd"}`);    
}

//--------------------EXERCISE 2:--------------------

console.log("=============\nExercise 2\n============="); 

let names= ["john", "sarah", 23, "Rudolf",34];

for (x in names) {
    if (typeof names[x] == "string")
    {
        console.log(names[x].charAt(0).toUpperCase() + names[x].slice(1));
    }
    else {
        continue;
    }
}

for (x in names) {
    if (typeof names[x] == "string")
    {
        console.log(names[x]);
    }
    else {
        break;
    }
}