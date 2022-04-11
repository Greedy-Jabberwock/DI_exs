//=========================EXERCISE_1==================================

let rowNum = 3;

let insertRow = () => {
    let parent = document.getElementById('sampleTable');    
    let newTr = document.createElement('tr');

    for (let i = 1; i < 3; i++) {
        let innerText = `Row${rowNum} cell${i}`;
        let newTd = document.createElement('td');
        newTd.innerText = innerText;
        newTr.append(newTd);
    }

    rowNum++;
    parent.append(newTr);
}

//=========================EXERCISE_2==================================

let button = document.getElementById('jsstyle');
let _style = button.style;

_style.width='20vw';

button.addEventListener('mouseout', () => _style.borderRadius = '8px');
button.addEventListener('mousedown', () => {_style.fontSize = '20vw';
                                            _style.width='50vw'});
button.addEventListener('click', ()=> _style.backgroundColor = 'green');
button.addEventListener('dblclick', ()=> _style.backgroundColor = 'cadetblue');
button.addEventListener('mouseover', () => _style.color = 'yellow');

//=========================EXERCISE_3==================================

let div = document.getElementById('divListen');
button = document.getElementById('jsstyle2');

div.addEventListener('click', divStyle);
button.addEventListener('click', buttonStyle1);
button.addEventListener('mouseover', buttonStyle2);

function divStyle(e) {
    div.style.backgroundColor = 'gold';
} 

function buttonStyle1(e) {
    
    e.stopPropagation();
    button.style.fontSize = '2rem';
} 

function buttonStyle2(e) {
    button.style.backgroundColor = 'purple';
} 