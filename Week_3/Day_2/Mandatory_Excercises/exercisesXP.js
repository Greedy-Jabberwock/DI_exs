//-------------------EXERCISE 1: YOUR FAVORITE FOOD-------------------------

console.log("\n---EXERCISE 1: YOUR FAVORITE FOOD---\n\n");

let favoriteFood = "jambalaya";
let favoriteMeal = 'dinner';
let result = `I eat ${favoriteFood} at every ${favoriteMeal}.`;

console.log(result + '\n\n')

//-------------------EXERCISE 2: SERIES-------------------------------------

    console.log("\n---EXERCISE 2: SERIES---\n\n");

//-----------Part I-------------

let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength = myWatchedSeries.length;
let myWatchedSeriesSentence = myWatchedSeries.slice(0, myWatchedSeriesLength-1).join(", ")
    .concat(", and " + myWatchedSeries[myWatchedSeriesLength-1]);

console.log(`I watched ${myWatchedSeriesLength} series: ${myWatchedSeriesSentence}`);

//-----------Part II-------------

myWatchedSeries.splice(myWatchedSeries.indexOf("the big bang theory"), 1, "the friends");

myWatchedSeries.push("american history of horrors");

myWatchedSeries.unshift("castle-rock");

let blackMirrorIndex = myWatchedSeries.indexOf("black mirror");
myWatchedSeries.splice(blackMirrorIndex,1);

console.log(myWatchedSeries[1][2]);
console.log(myWatchedSeries.toString());

//-------------------EXERCISE 3: THE TEMPERATURE CONVERTER------------------

console.log("\n---EXERCISE 3: THE TEMPERATURE CONVERTER---\n\n");

let celsius = 100;
console.log(`${celsius}°C is ${celsius / 5 * 9 + 32}°F`);

//-------------------EXERCISE 4: GUESS THE ANSWER #1------------------------

console.log("\n---EXERCISE 4: GUESS THE ANSWER #1---\n\n");

    let c;
    let a = 34;
    let b = 21;

    console.log(a+b) //first expression
    // Prediction: 55, because both variables are numbers, and summ of 34 and 21 will be 55.
    // Actual: 55

    a = 2;

    console.log(a+b) //second expression
    // Prediction: 23, because variable a was reassigned by value 2, and summ of 2 and 21 will be 23.
    // Actual: 23

    console.log(c);
    // Prediction: Value of c is undefined, because we are not assigned value to the variable c.
    // Actual: undefined

    console.log(3 + 4 + '5');
    // Prediction: 75, becuse first two numbers are number type, and they will be summed, and the "5" is a string, and previous summ
    //             will be concateneted and converted in string type.
    // Actual: 75

    //-------------------EXERCISE 5: GUESS THE ANSWER #2------------------------

typeof(15)
// Prediction: number type, because there are no quotes
// Actual: number.

typeof(5.5)
// Prediction: number type, because JS doesn't have different types for integer and float numbers.
// Actual: number.

typeof(NaN)
// Prediction: NaN, Not a Number type. 
// Actual: number. WAT?!

typeof("hello")
// Prediction: string type, cause it is semantical value, set of characters.
// Actual: string

typeof(true)
// Prediction: boolean, because there are no qoutes, so this is not a string
// Actual: boolean

typeof(1 != 2)
// Prediction: boolean, bacause it is comparsion
// Actual: 

"hamburger" + "s"
// Prediction: "hamburgers", simple concatenation
// Actual: "hamburgers"

"hamburgers" - "s" 
// Prediction: undefined, because strings connot be subtrackted
// Actual: NaN. I'm not sure here and farther in the similar sutiations.

"1" + "3"
// Prediction: "13", because both values are string, this is concatenation
// Actual: "13"

"1" - "3"
// Prediction: undefined.
// Actual: -2. In case subtracktion values tried to change type to number, i suppose.

"johnny" + 5
// Prediction: "johnny5". In the case when first value is string, next values will be tried to change to the string type 
// Actual: "johnny5"

"johnny" - 5
// Prediction: undefined, because the subtracting a number from a string is undefined
// Actual: NaN. 

99 * "hello"
// Prediction: NaN, because the result is undefied number. I am not sure.
// Actual: NaN. More guess than knowledge.

1 != 1
// Prediction: false, because they are equal
// Actual: false, as expected.

1 == "1"
// Prediction: true, because they have same values
// Actual: true. 

1 === "1"
// Prediction: false, because they have different types.
// Actual: false

//-------------------EXERCISE 6: GUESS THE ANSWER #3------------------------

5 + "34"
// Prediction: "534". Number changes type to string, and concatenate.
// Actual: "534"

5 - "4"
// Prediction: 1, because in this case string "4" changed to number type
// Actual: 1

10 % 5
// Prediction: 0, because there is no remainder after division
// Actual: 0

5 % 10
// Prediction: 5, because result of division is 0.5, and reminder is 5.
// Actual: 5

"Java" + "Script"
// Prediction: "JavaScript", concatenation
// Actual: 'JavaScript'

" " + " "
// Prediction: "  "
// Actual: '  '

" " + 0
// Prediction: " 0"
// Actual: ' 0'

true + true
// Prediction: 2, because true is 1 as a number.
// Actual: 2

true + false
// Prediction: 1, because true is 1 and false is 0
// Actual:

false + true
// Prediction: 1, because true is 1 and false is 0
// Actual:

false - true
// Prediction: -1, because true is 1 and false is 0
// Actual: -1

!true
// Prediction: false, because ! is NOT
// Actual: false

3 - 4
// Prediction: -1, because both are numbers 
// Actual: -1

"Bob" - "bill"
// Prediction: NaN, because i saw it in previous exercise.
// Actual: NaN.  Not sure why is not undefined
