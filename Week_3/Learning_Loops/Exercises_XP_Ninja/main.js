//--------------------EXERCISE 1:--------------------

console.log("=============\nExercise 1: Checking The BMI\n============="); 

let personOne = {
    fullName: "John Smith",
    mass: 100,
    height: 178,
    bmi : function() {
        return Math.pow((this.mass / this.height), 2).toFixed(2);
    }
};

let personTwo = {
    fullName: "Keily Green",
    mass: 74,
    height: 154,
    bmi : function() {
        return Math.pow((this.mass / this.height), 2).toFixed(2);
    }
};

function compareBMI(firstPerson, secondPerson) {
    return firstPerson.bmi() > secondPerson.bmi() ? firstPerson.fullName : secondPerson.fullName;
}

let greaterBMI = compareBMI(personOne, personTwo);
console.log(`${greaterBMI} has the largest BMI.`);

//--------------------EXERCISE 2:--------------------

console.log("=============\nExercise 2 : Grade Average\n============="); 

//--------FUNCTIONS--------

function findAvg(gragesList) {
    let avg = 0;
    for (x in gragesList) {
        avg += gragesList[x];
    }
    avg /= grages.length;
    console.log("Average of the grades: " + avg);
    return checkPassing(avg);
}

function checkPassing(gradeAvg) {
    let pass = "You passed! Congratulations!";
    let notPass = "You didn't pass. Repeat the course.";
    alert(gradeAvg < 65 ? notPass : pass);
}

//--------VARIABLES--------

let grages = [78, 90, 65, 88, 98, 100, 74];

//--------MAIN--------

console.log("User's grades: " + grages.toString());
findAvg(grages);