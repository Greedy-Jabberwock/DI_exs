let attempts = 5;
let score = 0;
let fullSet = false;
let hiddenCode = ''
let lose = false;
const spansToHide = document.querySelectorAll('.hidden > span');
const spansToGuess = document.querySelectorAll('.guess > span');

let createCode = () => {
    codeStr = '';
    for (let i = 0; i < 4; i++) {
        codeStr += Math.floor(Math.random() * 10)
    }
    console.log(codeStr)
    return codeStr
}

let hideCode = (code) => {
    for (let i = 0; i < spansToHide.length; i++) {
        spansToHide[i].innerHTML = "?"
    }
    return code;
}

let addNumber = (someNumber) => {
    let last = spansToGuess[spansToGuess.length - 1]
    if (! last.textContent) {
        for (let i = 0; i < spansToGuess.length; i++) {
            if (!spansToGuess[i].textContent) {
                spansToGuess[i].innerHTML += someNumber
                break
            }
        }
    } else {
        fullSet = true;
    }
}

let clearArea = () => {
    for (let i = 0; i < spansToGuess.length; i++) {
        spansToGuess[i].textContent = '';
    }
}

let checkResult = () => {
    if (!lose) {
        let guessed = 0
        for (let i = 0; i < spansToGuess.length; i++) {
            let hiddenEl = spansToHide[i]
            let guessEl = spansToGuess[i].textContent;
            hiddenEl.innerHTML = guessEl;
            if (guessEl == hiddenCode[i]) {
                hiddenEl.style.color = 'green'
                guessed += 1
            } 
            else if (hiddenCode.includes(guessEl)) {
                hiddenEl.style.color = 'yellow'
            } 
            else {
                hiddenEl.style.color = 'red'
            }
        }
        clearArea()
        if (guessed == 4) {
            alert('You win!')
            score += 1;
            document.getElementById('score').textContent = score;
        } else {
            attempts -= 1;
            document.getElementById('attempts').textContent = attempts;
            if (attempts == 0) {
                alert('You lose.')
                attempts = 0
            }
        }
    }
}

hiddenCode = hideCode(createCode());

document.getElementById('attempts').textContent = attempts;

document.getElementById('score').textContent = score;
