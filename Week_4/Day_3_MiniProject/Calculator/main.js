let resultString = '';
let htmlElement = document.getElementById("value_text");
let isEval = false;
let pointMarker = 0;
let previousActions = [];

let number = value => {
    if (!isEval) {
        previousActions.push(resultString);
        resultString += value;
        setHTMLValue(resultString);
        
    } else {
        isEval = false;
        clearFunc();
        resultString += value;
        setHTMLValue(resultString);
    }   
}

let operator = (sign) => {
    let pattern = /[^-,*,\/,+]$/;
    if (resultString.length == 0 && sign == '-') {
        previousActions.push(resultString);
        isEval = false;
        resultString += sign;
        setHTMLValue(resultString);
    } else if (resultString.match(pattern) != null) {  
        previousActions.push(resultString);
        isEval = false;
        resultString += sign;
        setHTMLValue(resultString);
    }
}

let equal = () => {
    previousActions = [];
    resultString = String(eval(resultString).toFixed(2));
    isEval = true;
    setHTMLValue(resultString);
}

let toPoint = () => {
    let pattern = /[^.]\d+[.]\d+$/;
    if (resultString.match(pattern) == null && resultString.length != 0) {
        resultString += '.';
        isEval = false;
        setHTMLValue(resultString);
    }
}

let clearFunc = () => {
    previousActions = [];
    resultString = '';
    setHTMLValue('');
}

let resetFunc = () => {
    if (previousActions.length == 0) {
        isEval = false;
        clearFunc();
    } else {
        resultString = previousActions.pop();
        setHTMLValue(resultString);
    }
}

let setHTMLValue = (resultString) => {
    htmlElement.innerHTML = resultString;
}