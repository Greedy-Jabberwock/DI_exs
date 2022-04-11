//=========================EXERCISE 4==========================================

//_______________FUNCTIONS______________

let getForm = () => {
    let form = document.getElementById('MyForm');
    return form;
};

let calculate = e => {
    const PI = 3.14;
    
    let r = Number(this.radius.value);
    let result = 0;

    if (r != 'NaN') {
        result = ((4 / 3) * (PI * Math.pow(r, 3))).toFixed(20);
    } else {
        alert('Not a number!');
        return 0;
    }

    this.volume.value = result;

    e.preventDefault();
};

let makeExercise4 = () => {
    const form = getForm();
    form.addEventListener('submit', calculate);
};

//________________MAIN______________________

makeExercise4();