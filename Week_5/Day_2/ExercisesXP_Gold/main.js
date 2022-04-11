let makeHeader = (value) => {
    console.log('====================================')
    console.log(`Exercise ${value}`);
    console.log('====================================')
}

//=========================EXERCISE 1==========================================

makeHeader(' 1 : Select A Kind Of Music');

//___________________________________FUNCTIONS___________________________________


let getSelectElement = () => {
    let select = document.getElementById('genres');
    return select;
};

let printSelectedOption = (selectEl) => {
    console.log(selectEl.value);
};

let addOption = (selectElement) => {
    let genre = 'Classic';
    let text = document.createTextNode(genre);
    let option = document.createElement('option');
    option.append(text);
    option.setAttribute('value', genre.toLowerCase())
    selectElement.appendChild(option);

    return option;
};

let removeSelectedAttr = select => {
    let options = select.options;
    for (let i = 0; i < options.length; i++) {
        if (options[i].getAttribute('selected') != null) {
            options[i].removeAttribute('selected');
        }
    }
};

let makeOptionSelected = (element) => {
    element.setAttribute('selected', 'selected');
};

let makeExercise1 = () => {
    let select = getSelectElement();
    printSelectedOption(select);
    removeSelectedAttr(select);
    let newElement = addOption(select);
    makeOptionSelected(newElement);
};

//___________________________________MAIN___________________________________

makeExercise1();

//=========================EXERCISE 2==========================================

makeHeader(' 2: Delete Colors');

//___________________________________FUNCTIONS___________________________________

let getSelect = () => {
    let select = document.getElementById('colorSelect');
    return select;
};

let removeColor = () => {
    let select = getSelect();
    let options = select.options;
    console.log(options);
    let indexToRemove = null;
    if (options.length > 0 ) {
        for (let i = 0; i < options.length; i++) {
            if (options[i].textContent == select.value) {
                indexToRemove = i;
                break;
            }
        }
        select.removeChild(options[indexToRemove]);
    } else {
        alert('List of colors is empty.');
    }
};

let makeExercise2 = () => {
    let button = document.forms[0].lastElementChild;
    button.addEventListener('click', removeColor);
};

//___________________________________MAIN___________________________________

makeExercise2();

//=========================EXERCISE 3==========================================

makeHeader(' 3 : Create A Shopping List');

//___________________________________VARIABLES___________________________________

let shoppingList = [];

//___________________________________FUNCTIONS___________________________________

//create and add form to 'root' div
//create addItem function
//add 'clear all' button
//create clearAll() function
let getRoot = () => {
    let root = document.getElementById('root');
    return root;
}

let createForm = () => {
    let root = getRoot();

    let inputEl = document.createElement('input');
    inputEl.setAttribute('type', 'text');
    inputEl.setAttribute('min', '3');
    root.appendChild(inputEl);

    let addButton = document.createElement('input');
    addButton.setAttribute('type', 'button');
    addButton.setAttribute('value', 'Add Item');
    addButton.style.margin = '0px 6px';
    addButton.addEventListener('click', addItem);
    root.appendChild(addButton);

    let clearButton = document.createElement('input');
    clearButton.setAttribute('type', 'button');
    clearButton.setAttribute('value', 'Clear All');
    clearButton.addEventListener('click', clearAll);
    root.appendChild(clearButton);

    let ul = document.createElement('ul');
    root.appendChild(ul);
}

let addItem = () => {
    let userInput = getRoot().firstElementChild;
    if (userInput.value.length >= 3) {
        shoppingList.push(userInput.value);
        console.log(shoppingList);
        userInput.value = '';

        let ul = document.querySelector('#root > ul');
        let li = document.createElement('li');
        let text = shoppingList[shoppingList.length - 1];
        li.append(text);
        ul.appendChild(li);
    }
}

let clearAll = () => {
    shoppingList = [];
    console.log(shoppingList);

    let ul = document.querySelector('#root > ul');
    ul.innerHTML = '';
}


let makeExercise3 = () => {
    createForm();
    
}

//_____________________________________MAIN______________________________________

makeExercise3();
