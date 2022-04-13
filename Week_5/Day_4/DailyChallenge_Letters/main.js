let input = document.getElementById('input');

let checkLetters = () => {
    let checkLetters = input.value.split('');
    let pattern = /[a-z]/
    let str = checkLetters.filter(element => {
        return element.toLowerCase().match(pattern) != null;
    });
    document.getElementById('input').value = str.join('');
}

input.addEventListener('input', checkLetters);