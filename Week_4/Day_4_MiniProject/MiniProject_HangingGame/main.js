let hangingGame = () => {
    let attempts = 10;
    let player_1 = validationCheck(1);
    let hidden_word = "*".repeat(player_1.length);
    let border = '-----------------------------'
    let alreadyUsed = '';
    console.log(`${border}\n${hidden_word}\n${border}`);
    
    for (let i = 1; i <= 10; i++) {
        if (hidden_word != player_1) 
        {
            let player2 = validationCheck(2);
            if (alreadyUsed.includes(player2)) {
                console.log("You tried this already. Try another letter.");
                i--;
                continue;
            } else {
                alreadyUsed = alreadyUsed.concat(player2);
            }
            if (player_1.includes(player2)) 
            {
                alreadyUsed = alreadyUsed.concat(player2);
                hidden_word = checkPlayer_2(player_1, hidden_word, player2);
                i--;
            }
            console.log(hidden_word);
            console.log(`Attempts remain: ${attempts - i}`);
        } else {
            console.log(`${border}\nYou win!\n${border}`);
            return 1;
        }
    }
    console.log(`${border}\nYou lose\n${border}`)
    
}

let validationCheck = (playerNumber) => {
    switch (playerNumber) {
        case 1: 
            let userInput = prompt("Player 1: give me a word for player2.").toLowerCase();
            let pattern = /^[a-z]+$/;
            if (userInput.match(pattern) != null) {
                return userInput;
            } else {
                validationCheck(1);
            }
        case 2: 
            let patternPlayer2 = /^[a-z]$/;
            let player2_Input = prompt("Player 2: give me a letter for player1.").toLowerCase();
            if (player2_Input.match(patternPlayer2) != null) {
                    return player2_Input;
            } else {
                validationCheck(2);
            }
    }
}

let checkPlayer_2 = (firstPlayerWord, hiddenWord, player2Letter) => {
    let firstPlayerArray = firstPlayerWord.split("");
    let hiddenArray = hiddenWord.split('');
    firstPlayerArray.forEach((element, index) => {
        if (player2Letter == element) {
            hiddenArray[index] = player2Letter;
        }
    });
    hiddenWord = hiddenArray.join('');
    return hiddenWord;
}

let checkLetter = (player2, usedLetters) => {
    if (usedLetters.includes(player2)) {
        player2 = prompt('You tried this already. Try another letter.');
        checkLetter(player2, usedLetters);
    } else {
        alreadyUsed = usedLetters.concat(player2);
        return usedLetters;
    }
}

hangingGame();

