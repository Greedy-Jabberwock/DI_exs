const defaultStyle = "white";
let pickedStyle = '';
let colorBoxes = document.querySelectorAll('#colors > .color');
let cells = document.querySelectorAll('#cells > div');


colorBoxes.forEach(item => {
    item.addEventListener('click', (e) => {
        e.preventDefault();
        // console.log(item);
        pickedStyle = item.getAttribute('style');
    });
});

let clearAll = () => {
    cells.forEach(item => {
        item.style.backgroundColor = defaultStyle;
    })
}

let addColor = target => {
    if (pickedStyle != '') {
        let style = pickedStyle.split(':')[1];
        console.log(style)
        console.log(target)
        target.style.backgroundColor = style;
    } else {
        console.log('style is empty')
    }
}

let mouseOver = e => {
    e.preventDefault();
    addColor(e.target);
}

let mouseDown = e => {
    e.preventDefault();
    this.addEventListener('mouseover', mouseOver);
    addColor(e.target);
}

let mouseUp = e => {
    e.preventDefault();
    this.removeEventListener('mousedown', mouseDown)
    this.removeEventListener('mouseover', mouseOver)
}

cells.forEach(item => {
    item.addEventListener('mousedown', mouseDown);
    item.addEventListener('mouseup', mouseUp);
})
