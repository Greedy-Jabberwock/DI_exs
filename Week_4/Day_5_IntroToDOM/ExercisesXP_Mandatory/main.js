//----------------------------------Exercise 1-------------------------------------------
console.log('==================\nExercise 1:\n==================')

let oldId = 'navBar';
let newId = "socialNetworkNavigation"
let selector = `#${newId} > ul`

document.getElementById(oldId).setAttribute("id", newId);

let newLiElement = document.createElement('li');
let newTextNode = document.createTextNode('LogOut');
newLiElement.append(newTextNode);
document.querySelector(selector).appendChild(newLiElement);


console.log(document.querySelector(selector).firstElementChild.textContent);
console.log(document.querySelector(selector).lastElementChild.textContent);

//----------------------------------Exercise 2-------------------------------------------

document.querySelector('#container + .list > li:last-child').innerHTML = 'Richard';

let eachFirstLi = document.querySelectorAll('.list > li:first-child');
for (let element of eachFirstLi) {
    element.innerHTML = "Vitalii";
}


let ulLists = document.querySelectorAll('.list');
for (let elem of ulLists) {
    let newListLi = document.createElement('li');
    let listTextNode = document.createTextNode("Hey students!");
    newListLi.append(listTextNode);
    elem.append(newListLi);
}

let secondUlSelector = '.list + .list';
let saraSelector = ' > li:nth-child(2)';
let secondUlElement = document.querySelector(`${secondUlSelector}`);
let saraElement = document.querySelector(`${secondUlSelector}${saraSelector}`);
secondUlElement.removeChild(saraElement);

for (let elem of ulLists) {
    elem.classList.add('student_list');
}

secondUlElement.classList.add('university', 'attendance');

//----------------------------------Exercise 3-------------------------------------------

let anotherDivElement = document.querySelector('.another > div');
let listElement = document.querySelector('.another > ul');
let johnElement = listElement.firstElementChild;
let peteElement = listElement.lastElementChild;
let bodyStyle = document.getElementsByTagName('body')[0].style;

anotherDivElement.style.background = "lightblue";
anotherDivElement.style.padding = '25px';

johnElement.style.visibility = "hidden";

peteElement.style.border = '2px dotted green';

bodyStyle.fontSize = '7vh';

if (anotherDivElement.style.background == "lightblue") {
    let john = johnElement.textContent;
    let pete = peteElement.textContent;
    alert(`Hello, ${john} and ${pete}.`)
}