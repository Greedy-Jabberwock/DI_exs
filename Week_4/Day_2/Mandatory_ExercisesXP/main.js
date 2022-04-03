//--------------------EXERCISE 1:--------------------

console.log("=============\nExercise 1: Information\n=============");

//-----Part I:-----

function infoAboutMe() {
    console.log("My name is Vitalii, 28 yo, I love to code.");
}

infoAboutMe();

//-----Part II:-----

function infoAboutPerson(personName, personAge, personFavoriteColor) {
    console.log(`You name is ${personName}, you are ${personAge} years old, your favorite color is ${personFavoriteColor}.`);
}

infoAboutPerson("David", 45, "blue");
infoAboutPerson("Josh", 12, "yellow");

//--------------------EXERCISE 2:--------------------

console.log("=============\nExercise 2: Tips\n=============");

function calculateTip() {
    let bill = Number(prompt("Enter the amount: "));
    if (!isNaN(bill)) {
        let currentTip;
        switch (true) {
            case bill > 200:
                currentTip = 10;
                break;
            case bill <= 200 && bill >= 50:
                currentTip = 15;
                break;
            case bill < 50:
                currentTip = 20;
                break;
        }
        bill += bill / 100 * currentTip;
        console.log(bill);
    }
    else {
        calculateTip()
    }
}

//calculateTip();

//--------------------EXERCISE 3:--------------------

console.log("=============\nExercise 3: Find The Numbers Divisible By 23\n=============");

function isDivisible(divisor = 23) {
    let resultArray = [];
    for (let i = 0; i < 500; i++) {
        if (i % divisor == 0) resultArray.push(i); 
    }
    let arrayString = resultArray.join(' ');
    console.log(`Outcome: ${arrayString}`);
    let summOfElements = 0;
    resultArray.forEach(calcSum);
    console.log(`Summ of element: ${summOfElements}`);

    function calcSum(item) {
        summOfElements += item;
    }
}

isDivisible();
isDivisible(34);

//--------------------EXERCISE 4:--------------------

console.log("=============\nExercise 4: Shopping List\n=============");
//___________________VARIABLES________________________
let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList = ["banana", "orange", "apple"];
let actualShoppingList = [];
let totalAmount = 0;

//___________________FUNCTIONS________________________

function myBill() {
    shoppingList.forEach(isInStock);
    shoppingList.forEach(calculatePrice);
    console.log(`Actual shopping list: ${shoppingList}`)
    console.log(`Total amount: ${totalAmount}.`)
}

function isInStock(item) {
    console.log(`Amount ${item}s in stock before adding to cart: ${stock[item]}`)
    if (stock[item] != 0){
        stock[item]--;
        console.log(`Amount ${item}s in stock after adding to cart: ${stock[item]}`)
    }
    else {
        let notInStock = shoppingList.indexOf(item);
        shoppingList.splice(notInStock, 1);
    }
}

function calculatePrice(item) {
    totalAmount += prices[item];
}

//_____________________MAIN___________________________

myBill();


//--------------------EXERCISE 4:--------------------

console.log("=============\nExercise 4: Shopping List\n=============");

//___________________VARIABLES________________________

let totalInPockets = 0;

//___________________FUNCTIONS________________________

function changeEnough(itemPrice, amountOfChange) {
    totalInPockets = 0;
    amountOfChange.forEach(calculateChange);
    let result = itemPrice < totalInPockets ? true : false;
    console.log("_____________________________________________")
    console.log("Item price: " + itemPrice);
    console.log("Coins in pockets: " + amountOfChange.join(', '));
    console.log("Total amount in pockets: " + totalInPockets);
    console.log("So can you buy it? " + result);
    console.log("_____________________________________________")
}

function calculateChange(item, index) {
    const values = [0.25, 0.10, 0.05, 0.01];
    totalInPockets += item * values[index];
}

//_____________________MAIN___________________________

changeEnough(4.25, [25, 20, 5, 0]);
changeEnough(14.11, [2,100,0,0]);
changeEnough(0.75, [0,0,20,5]);


//--------------------EXERCISE 6:--------------------

console.log("=============\nExercise 6 : Vacations Costs\n=============");

//___________________FUNCTIONS________________________

function totalVacationCost() {
    let nights = Number(prompt("How many nights do you want to stay?"));
    let hotel = hotelCost(nights);
    let destinPoint = prompt("Where do you want to fly?");
    let fly = planeRideCost(destinPoint) * 2;
    let days = Number(prompt("How many days do you want to rent the car?"));
    let car = rentalCarCost(days);
    console.log(`HOTEL: ${hotel}$\nPLANE: ${fly}$\nCAR: ${car}$`);
    let total = hotel + fly + car;
    console.log(`TOTAL: ${total}$`)

}

function hotelCost(numberOfNights) {
    if (isNaN(numberOfNights) || numberOfNights < 0 || numberOfNights === undefined) {
        hotelCost();
    }
    else {
        let costPerNight = 140;
        let result = numberOfNights * costPerNight;
            console.log(`HOTEL: ${costPerNight} * ${numberOfNights} = ${result}`);
        return result;
    }
}

function planeRideCost(destination) {
    const flyPrices = [183, 220, 300];
    
    if (typeof destination != "string" || destination == '') {
        planeRideCost();
    }
    else {
        switch (destination.toLowerCase()) {
            case "london":
                    console.log(`PLANE: ${destination} = ${flyPrices[0]}`);
                return flyPrices[0];
            case 'paris':
                    console.log(`PLANE: ${destination} = ${flyPrices[1]}`);
                return flyPrices[1];
            default:
                    console.log(`PLANE: ${destination} = ${flyPrices[2]}`);
                return flyPrices[2];
        }
    }
}

function rentalCarCost(daysOfRent) {
    
    console.log(daysOfRent);
    if (isNaN(daysOfRent) || daysOfRent < 0 || daysOfRent === undefined) {
        rentalCarCost();
        
    } 
    else {
        let rentCost = daysOfRent * 40;
        let discount = rentCost / 100 * 5;
        let result = daysOfRent > 10 ? rentCost - discount : rentCost;
        console.log(`CAR: ${daysOfRent} * 40 = ${result}`);

        return result;
    }
}

//_____________________MAIN___________________________

totalVacationCost();