let makeHeader = (value) => {
    console.log('====================================')
    console.log(`Exercise ${value}`);
    console.log('====================================')
}

//=========================EXERCISE 1==========================================

makeHeader('1 : Change The Article');

//______________VARIABLES_______________

const article = document.querySelector('article');

//_______________FUNCTIONS______________

let retrieveH1 = () => {
    let h1 = document.querySelector('h1');
    console.log(h1);
}

let removeLastP = () => {
    let lastP = document.querySelector('article > p:last-child');
    article.removeChild(lastP);
}

let changeBgH2 = () => {
    let h2 = document.querySelector('h2');
    h2.addEventListener('click', () => h2.style.background = 'red');
};

let addEventListenerH3 = () => {
    let h3 = document.querySelector('h3');
    h3.addEventListener('click', () => h3.style.display = 'none');
};

let addBoldButton = () => {
    let paragraghs = document.querySelectorAll('article > p');
    let buttonText = document.createTextNode('Make BOLD!');
    let button = document.createElement('button');
    button.append(buttonText);
    button.addEventListener('click', () => {
        paragraghs.forEach((item) => item.style.fontWeight = 'bold');
    });
    article.appendChild(button);
};

let makeExercise1 = () => {
    retrieveH1();
    removeLastP();
    changeBgH2();
    addEventListenerH3();
    addBoldButton();
    //randomSizeH1();
    fadeSecondP();
}

//________________BONUS PART_______________

let randomSizeH1 = () => {
    let h1 = document.querySelector('h1');
    h1.addEventListener('mouseover', () => {
        let randomSize = Math.random() * 101;
        h1.style.fontSize = `${randomSize}px`;
    })
};

let fadeSecondP = () => {
    let secondP = document.querySelectorAll('article > p')[1];
    secondP.style['transition'] = '0.5s';
    secondP.addEventListener('mouseover', () => secondP.style.opacity = '50%');
    secondP.addEventListener('mouseout', () => secondP.style.opacity = '100%');
};

//________________MAIN______________________

makeExercise1();

//=========================EXERCISE 2==========================================

makeHeader('2 : Work With Forms');

//_______________FUNCTIONS______________

let retrieveForm = () => {
    console.log('Retrieving form:');
    const form = document.forms[0];
    console.log(form);
    return form;
};

let retrieveInputsById = (form) => {
    console.log('Retrieving form inputs by id:');
    let idArray = ['fname', 'lname', 'submit'];
    idArray.forEach(item => console.log(form.elements[item]));
};

let retrieveInputsByName = (form) => {
    console.log('Retrieving form inputs by names:');
    let namesArray = ['fname', 'lname'];
    let inputsArray = [];
    namesArray.forEach(item => {
        let el = form.elements[item]
        console.log(el)
        el.setAttribute('required', true);
        inputsArray.push(el);    
    });
    return inputsArray;
};

let getFormAndInputs = () => {
    let form = retrieveForm();
    retrieveInputsById(form);
    let inputs = retrieveInputsByName(form);
    makeExercise2(form, inputs);
}

let createLiElements = (inputs) => {
    let ul = document.querySelector('.usersAnswer');
    
    inputs.forEach(item => {
        let li = document.createElement('li');
        let text = document.createTextNode(item.value);
        li.append(text);
        ul.append(li);
    });
}

let makeExercise2 = (form, inputs) => {
    let submitForm = event => {
        createLiElements(inputs);
        event.preventDefault();
    }

    form.addEventListener('submit', submitForm)
}

//________________MAIN______________________

getFormAndInputs();

//=========================EXERCISE 3==========================================

makeHeader('3 : Transform The Sentence');

//______________VARIABLES_______________

let allBoldItems = [];

//_______________FUNCTIONS______________

let getBold_items = () => {
    allBoldItems = document.querySelectorAll('strong');
}

let highlight = () => {
    allBoldItems.forEach(item => item.style.color = 'blue');
}

let return_normal = () => {
    allBoldItems.forEach(item => item.style.color = 'black');
}

let createListeners = () => {
    allBoldItems.forEach(item => {
        item.addEventListener('mouseover', highlight);
        item.addEventListener('mouseout', return_normal);
    })
}

let makeExercise3 = () => {
    getBold_items();
    createListeners();
}

//________________MAIN______________________

makeExercise3();

//========EXERCISE 4 IS IN ANOTHER FILE================

//=========================EXERCISE 5==========================================

makeHeader('5 : Event Listeners');

//______________VARIABLES_______________

let lorem = document.getElementById('exc5');

//_______________FUNCTIONS______________

let makeExercise5 = () => {
    lorem.addEventListener('click', makeFade);
    lorem.addEventListener('dblclick', changeHeight);
    lorem.addEventListener('mouseover', changeBgCl);
    lorem.addEventListener('mouseout', changeFontColor);
    lorem.addEventListener('mouseup', changeFontSize);

}

let makeFade = () => {
    lorem.style.opacity = '75%';
};

let changeHeight = () => {
    lorem.style.height = '40vh';
};

let randomRGB = () => {
    let r = Math.random() * 256;
    let g = Math.random() * 256;
    let b = Math.random() * 256;
    return `rgb(${r},${g},${b})`;
}

let changeBgCl = () => {
    lorem.style.backgroundColor = randomRGB();
};

let changeFontColor = () => {
    lorem.style.color = randomRGB();
};

let changeFontSize = () => {
    lorem.style.fontSize = '10rem';
}

//________________MAIN______________________

makeExercise5();