//=========================Exercise 1============================

let makeExercise1 = () => {
    let makeVisible = () => {
        let div = document.getElementById('banner');
        div.style.visibility = 'visible';
        document.getElementById('timer').innerHTML = '10 min!';
    };

    setTimeout(makeVisible, 5000);
};

//makeExercise1();

//=========================Exercise 1============================

let makeExercise2 = () => {
    let div = document.getElementById('banner');
    div.style.visibility = 'visible';
    let span = document.getElementById('timer');
    let timeRemains = 10;
    span.innerHTML = `${timeRemains} sec.`;

    let timer = setInterval(() => {
        span.innerHTML = `${timeRemains} sec.`
        timeRemains--;
        if (timeRemains < 0) {
            clearInterval(timer);
        }
    }, 1000);

};

makeExercise2();