let elements = document.querySelectorAll('ul > li:first-child'); 
for (let elem of elements) {
    elem.innerHTML = 'checked.'
}

let elems = document.getElementsByTagName('ul')[0];
for (let elem of elems) {
    elem.innerHTML = 'twice;'
}