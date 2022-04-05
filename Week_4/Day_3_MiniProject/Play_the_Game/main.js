function playTheGame() {
    if(confirm("Want to play a game?")) {
        let userNumber = checkValue(getUserNumber());
        let computerNumber = (Math.random()*10).toFixed(0);
        let test = 0;
        for (let i = 0; i < 3; i++) {
            console.log(computerNumber + '    ' + userNumber);
            test = testNumbers(userNumber, computerNumber);
            if (test == 1) {
                return true;
            }
            else {
                userNumber = checkValue(getUserNumber());
            }
        }
        alert("Out of chance.");
        
    }
    else {
        alert("Ok, goodbye");
    }
}

let getUserNumber = () => {
    let userPromt = Number(prompt("Enter the number between 0 - 10"))
    return checkValue(userPromt);
}

let checkValue = value => {
    if (isNaN(value) || (value < 0 || value > 10) || value == "undefined") {
        getUserNumber();
    } 
    else {
        return value;
    }
}

let testNumbers = (userNumber, computerNumber) => {
    if (userNumber == computerNumber) {
        alert("WINNER!!!")
        return 1;
    }
    else if (userNumber > computerNumber){
        alert("Your number is bigger then the computer’s, guess again");
    }
    else {
        alert("Your number is smaller then the computer’s, guess again");
    }
    return 0;
}