//=====================EXERCISE 1============================================

let myMove = () => {
    let box = document.getElementById('animate');
    console.log(box)
    let start = Date.now();
    console.log(start)

    let timer = setInterval(() => {
        let passed = Date.now() - start;
        box.style.left = passed / 5.7 + 'px';

        if (passed > 2000) {
            clearInterval(timer);
        }
    }, 20)
}
