//==================================FUNCTIONS================================

let createTableCells = () => {
    let tableElement = document.createElement('table');
    let mainEl = document.querySelector('body');
    mainEl.appendChild(tableElement);

    let firstLine = true;
    for (let i = 0; i < 6; i++) {
        let trElement = document.createElement('tr');
        
        tableElement.appendChild(trElement);

        for (let x = 0; x < 7; x++) {
            if (firstLine) {
                let thElement = document.createElement('th');
                thElement.innerHTML = `x=${x}`;
                trElement.appendChild(thElement);

            } else {
                let tdElement = document.createElement('td');
                tdElement.innerHTML = `x=${x}`;
                trElement.appendChild(tdElement);
            }
        }
        firstLine = false;
    }
}

let createTableValues = (userDate) => {
    const weekday = ["SU","MO","TU","WE","TH","FR","SA"];
    let points = 0;
    let dates = [];
    let d = new Date(userDate.year, userDate.month);
    let rightDay = d.getDay();
    let isDayRight = false;

    for (let i = 1; i < 32; i++) {
        let d = new Date(userDate.year, userDate.month, i);
        
        if (rightDay != points) {
            points++;
            i--;
        } else {
            if (d.getMonth() > userDate.month) {
                break;
            }
            dates.push(d.getDate());
        }
    }

    points = '.'.repeat(points).split('');
    let resultArray = weekday.concat(points).concat(dates);
    points = '.'.repeat(42 - resultArray.length).split('');
    resultArray = resultArray.concat(points);
    
    return resultArray;
}

let fillTable = valuesArray => {
    let thElements = document.querySelectorAll('th');
    let tdElements = document.querySelectorAll('td');
    let week = valuesArray.slice(0, 7);
    let days = valuesArray.slice(7);
    console.log(week.join(','));
    console.log(days.join(','));
    console.log(thElements);
    console.log(tdElements);


    thElements.forEach(item => {
        item.style.width = '5vw';
        item.style.height = '4vh';
        item.style.border = '1px solid black';
        item.style.fontSize = '5vh';
    })
    tdElements.forEach(item => {
        item.style.width = '5vw';
        item.style.height = '2vh';
        item.style.border = '1px solid black';
        item.style.textAlign = 'center';
        item.style.fontSize = '4vh';
    })

    thElements.forEach((item, index) => item.innerHTML = week[index]);
    tdElements.forEach((item, index) => item.innerHTML = days[index]);
}

let createTable = () => {
    console.log("Invoke createTable()");
    createTableCells();
    console.log("Create values");
    let tableValues = createTableValues(userDate);
    console.log('Filling the table');
    fillTable(tableValues);
}
//==================================VARIABLES================================

let userDate = {
    year: 2022,
    month: 2,
};

createTable();
