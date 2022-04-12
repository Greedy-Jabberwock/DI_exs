let makeHeader = (value) => {
    console.log('====================================')
    console.log(`Exercise ${value}`);
    console.log('====================================')
}

//=========================EXERCISE 1==========================================

makeHeader('1 : Calculate The Tip');

//___________________________________FUCNTIONS_________________________________________

let getBillAmount = () => {
    let billAmount = document.getElementById('billamt').value;
    return billAmount;
};

let getQualityService = () => {
    let quality = document.getElementById('serviceQual').value;
    return quality;
};

let getPeopleNumber = () => {
    let peopleNumber = document.getElementById("peopleamt").value;
    return peopleNumber;
};

let checkBillAndQuality = (bill, quality) => {
    let billCondition = Number(bill) <= 0 || bill == '';
    let qualityCondition = quality === '0';

    if (billCondition || qualityCondition) {
        alert('Enter correct values!');
        return false;
    } else {
        return true;
    }
};

let checkPeopleNumber = (people) => {
    let peopleEl = document.getElementById('peopleamt');
    let peopleCondition = isNaN(Number(people)) || Number(people) <= 1 || people == '';
    if (peopleCondition) {
        people = 1;
        document.getElementById('each').style.display = 'none';
    } 
    people = Number(people).toFixed(0);
    peopleEl.value = people;
    return people;
}

let displayTip = total => {
    let div = document.getElementById('totalTip');
    div.style.display = 'block';

    let span = document.getElementById('tip');
    span.innerHTML = total;
};

let calculateTips = () => {
    let billAmount = getBillAmount();
    let serviceQuality = getQualityService();
    let peopleNumber = getPeopleNumber(); 

    if (checkBillAndQuality(billAmount, serviceQuality)) {
        peopleNumber = checkPeopleNumber(peopleNumber);
        let total = ((billAmount * serviceQuality) / peopleNumber).toFixed(2);
        displayTip(total);
    }
};

let makeExercise1 = () => {
    document.getElementById('totalTip').style.display = 'none';
    let button = document.getElementById('calculate');
    button.addEventListener('click', calculateTips);
};

//_______________________________________MAIN____________________________________________

makeExercise1();

//=========================EXERCISE 2==========================================

makeHeader('2 : Validate The Email');

//___________________________________FUCNTIONS_________________________________________

let createForm = () => {
    let body = document.querySelector('body');
    let form = document.createElement('form');
    let br = document.querySelector('#here');
    form.innerHTML = `<input type="email" id="mail" placeholder="Enter your email">
    <input type="submit" value="Submit" id="sub">
    <p id="result"></p>`;
    body.insertBefore(form, br);

    return form;
};

let validateRegEx = (e) => {
    let pattern = /^(\w+[.]?\w+)+[@]{1}[a-z]+[.]{1}[a-z]+/
    let mail = document.getElementById('mail').value;
    let result = document.getElementById('result');
    if (mail.match(pattern)) {
        result.innerText = `'${mail}' is valid!`
    } else {
        result.innerText = `'${mail}' is invalid!`
    }
    e.preventDefault();
};

let validateWithoutRegEx = (e) => {
    let mail = document.getElementById('mail').value;
    let letters = 'abcdefghijklmnopqrstuvwxyz';
    let numbers = '0123456789';
    let special1 = '@';
    let special2 = '.';
    let specials = special1 + special2;
    let all = letters + numbers + specials;
    let marker = 0;
    let specCounter = 0;
    let result = '';
    let isAfterA = false;
    for (let i = 0; i < mail.length - 1; i++) {
            let current = mail[i].toLowerCase();
            let next = mail[i + 1].toLowerCase();

            if (current == '@') {
                isAfterA = true;
            }

            

            if (!isAfterA) {
                if ((specials.includes(current) && specials.includes(next))) {
                    marker++;
                };
                if (!(all.includes(current)) || !(all.includes(next))) {
                    marker++;
                }
            } else {
                if ((specials.includes(current) && specials.includes(next))) {
                    marker++;
                }
                // if (!(letters.includes(next)) || !(special2.includes(next))) {
                //     marker++;
                // }
                if (specials.includes(next)) {
                    specCounter++;
                }
                if (specCounter > 1) {
                    marker++;
                }
            }

            console.log(`Current: ${current}\nNext: ${next}\nAfter @: ${isAfterA}\nCounter: ${marker}\nSpecial counter: ${specCounter}`);
        }        
    result = marker > 0 ? 'forbidden' : 'valid';

    let res = document.getElementById('result');
    res.innerHTML = `'${mail}' is ${result}`;
    document.getElementById('mail').value = '';
    e.preventDefault();
};

let makeExercise2 = () => {
    let form = createForm();
    form.addEventListener('submit', validateRegEx);
    //form.addEventListener('submit', validateWithoutRegEx);
}

//_______________________________________MAIN____________________________________________

makeExercise2();

//=========================EXERCISE 3==========================================

makeHeader('3 : Get The User"s Geolocation Coordinates');

let showPosition = () => {
    if(navigator.geolocation) {
        navigator.geolocation.getCurrentPosition((position) => {
            let positionInfo = "Your current position is (" + "Latitude: " + position.coords.latitude + ", " + "Longitude: " + position.coords.longitude + ")";
            document.getElementById("position").innerHTML = positionInfo;
        });
    } else {
        alert("Something goes wrong.");
    }
}
