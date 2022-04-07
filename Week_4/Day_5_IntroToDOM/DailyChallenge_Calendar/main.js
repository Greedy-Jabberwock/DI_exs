const weekday = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];

let userDate = {
    year: 2012,
    month: 9,
    day: 1,
    newMonth: false
};

let _date = userDate;
let daysInMonth = 0;
let searchDate = new Date(_date.year, _date.month, _date.day);

while (!_date.newMonth && daysInMonth < 35) {
    searchDate = new Date(_date.year, _date.month, _date.day);
    let currentWeekday = weekday[searchDate.getDay()];
    console.log(`Month: ${_date.month}\nDate: ${_date.day}\nWeekday: ${currentWeekday}`)
    console.log(`Month: ${searchDate.getMonth()}\nDate: ${searchDate.getDate()}\nWeekday: ${searchDate.getDay()}`)
    daysInMonth++;
    _date.day++;
    
    if (_date.day == 32)
    {
        _date.newMonth = true;
    }
} 

console.log(daysInMonth)
