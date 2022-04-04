let userString = prompt("Please, enter several words, separated by commas.");
let stringArray = userString.split(/\s*,\s*/);

function makeDecor(userArray) {
    let longestWord = '';
    
    userArray.forEach(item => {
        longestWord = longestWord.length < item.length ? item : longestWord

    });

    let edges = ["* ", " *"];
    let edgesLength = edges[0].length + edges[1].length;
    let longestLine = edgesLength + longestWord.length;
    let starsLine = "*".repeat(longestLine);

    console.log(starsLine);

    for (let i = 0; i < userArray.length; i++) {
        let currentElement = userArray[i];
        if (currentElement != "") {
            let currentLineLength = edgesLength + currentElement.length;
        if (currentLineLength < longestLine) {
            let spaces = longestLine - currentLineLength;
            currentElement = currentElement.concat(" ".repeat(spaces));
        }
        let wholeLine = `${edges[0]}${currentElement}${edges[1]}`;
        console.log(wholeLine);
        }
    }

    console.log(starsLine);
}

makeDecor(stringArray);