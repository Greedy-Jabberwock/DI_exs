const wordCollection = {
    noun: ['brigand', 'goblet', 'sword'],
    adjective: ['good', 'bad', 'cold'],
    person: ['Jack', 'Susie', 'Archer'],
    verb: ['store', 'hate', 'jelaous of'],
    place: ['castle', 'office building', 'camp']
};

let addListener = () => {
    let libButton = document.getElementById('lib-button');
    libButton.addEventListener('click', makeStory);
};

let valuesIsValid = (userInputs) => {
    let marker = 0;
    userInputs.forEach(element => {
        if (element.value == '') {
            marker++;
        }
    });
    if (marker == 0) {
        return true;
    } else {
        return false;
    }
}

let saveValues = (userValues) => {
    let sentence = [];
    userValues.forEach(item => {
        wordCollection[item.id].push(item.value);
        sentence.push(item.value);
    })
    console.log(wordCollection);
    return sentence;
}

let printSentence = (wordsArray) => {
    let noun = wordsArray[0];
    let adjective = wordsArray[1];
    let person = wordsArray[2];
    let verb = wordsArray[3];
    let place = wordsArray[4];
    let fullSentence = `${person} ${verb} ${adjective} ${noun} in the ${place}`;
    let span = document.getElementById('story');
    span.innerText = fullSentence;
}

let makeStory = () => {
    let inputs = document.querySelectorAll('input');
    if (valuesIsValid(inputs)) {
        printSentence(saveValues(inputs));
    } else {
        alert('Fill all inputs.')
    }
};

let shuffle = () => {
    let length = wordCollection.noun.length;
    let keys = Object.keys(wordCollection);
    let sentence = [];
    keys.forEach(item => {
        sentence.push(wordCollection[item][(Math.random()*(length-1)).toFixed(0)]);
    })
    printSentence(sentence);
}

let makeButton = () => {
    let button = document.createElement('button');
    let p = document.querySelector('p');
    let body = document.querySelector('body');
    
    button.innerHTML = 'Shuffle!';
    body.insertBefore(button, p);

    button.addEventListener('click', shuffle);
}

let makeShuffle = () => {
    makeButton();
}

let makeExercise = () => {
    addListener();
    makeShuffle();
};


makeExercise();
