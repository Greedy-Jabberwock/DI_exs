let singSong = () => {
    let bottles = [isValid(), 1, true];
    while(bottles[2]) {
        bottles = printLines(bottles);
    }
};


let isValid = () => {
    let userInput = Number(prompt("How many bottles of beer are on the wall?"));
    if (!isNaN(userInput) && userInput > 0) {
        return userInput;
    } else {
        isValid();
    }
}

let printLines = (bottlesArray) => {
    let _bottlesOnWall = bottlesArray[0];
    let _bottlesTaken = bottlesArray[1]
    let bottles = (_bottlesOnWall <= 1 ? 'bottle' : 'bottles').concat(" of beer");
    let itOrThem = _bottlesTaken == 1 ? 'it' : 'them';
    let wallString = 'on the wall';
    let firstPart = `${_bottlesOnWall} ${bottles}`;
    let finalLine = `No ${bottles} ${wallString}`;

    let firstLine = `${firstPart} ${wallString}`;
    let secondLine = `${firstPart}`;
    let thirdLine = `Take ${_bottlesTaken} down, pass ${itOrThem} down`;
    let bottlesRemainOnWall = _bottlesOnWall;
    _bottlesOnWall -= _bottlesTaken;
    _bottlesTaken++;
    let fourthLine = `${bottlesRemainOnWall} ${bottles} ${wallString}`

    if (_bottlesOnWall <= 0) {
        thirdLine = `Take ${bottlesRemainOnWall} down, pass ${itOrThem} down`;
        console.log(`${firstLine}\n${secondLine}\n${thirdLine}\n${finalLine}\n\n`);
        bottlesArray[2] = false;
        return bottlesArray;
    }

    console.log(`${firstLine}\n${secondLine}\n${thirdLine}\n${fourthLine}\n\n`);
    bottlesArray[0] = _bottlesOnWall;
    bottlesArray[1] = _bottlesTaken;

    return bottlesArray;
} 

singSong();