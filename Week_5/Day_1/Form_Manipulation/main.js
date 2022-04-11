//===============================Exercise 1====================================

let form1 = document.forms[0];

let firstName = form1[0].value;
let lastName = form1[1].value;

console.log(firstName);
console.log(lastName);

//===============================Exercise 2====================================

let dropdown = document.getElementById('select1');
let active;

let makeChanges = (selectElement) => {
    let second = selectElement.options[1].value;

    let workOption = makeOption('Work');
    
    selectElement.appendChild(workOption);
    
    let primaryOption = makeOption('Primary School');
    selectElement.add(primaryOption,selectElement.options[0]);

    selectElement.options[3].selected = true;
    selectElement.value = 'banana';
    selectElement.selectedIndex = 3;

}

let makeOption = (value) => {
    let option = document.createElement('option');
    option.value = value.toLowerCase();
    option.innerHTML = value;

    return option;
}


let findActice = () => {
    for (let i = 0; i < dropdown.options.length; i++) {
        if (dropdown.options[i].selected == true) {
            active = dropdown.options[i].textContent;
        }
    }
}

let alertSelect = () => {
    findActice();
    alert(active + ' is chosen.');
}

makeChanges(dropdown);