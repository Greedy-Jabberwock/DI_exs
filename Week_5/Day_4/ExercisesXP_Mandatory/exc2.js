//=============================Exercise 2==================================

const fill = document.querySelector('.fill');
const emptyEls = document.querySelectorAll('.empty');

fill.addEventListener('dragstart', dragStart);
fill.addEventListener('dragend', dragEnd);

for (const item of emptyEls) {
    item.addEventListener('dragover', dragOver);
    item.addEventListener('dragenter', dragEnter);
    item.addEventListener('dragleave', dragLeave);
    item.addEventListener('drop', dragDrop);
}

function dragStart() {
    this.className += ' hold';
    setTimeout(() => this.className = 'invisible', 0);
};

function dragEnd() {
    this.className = 'fill';
};

function dragOver(e) {
    e.preventDefault();
}; 

function dragEnter(e) {
    e.preventDefault();
    this.className += ' hovered';
};

function dragLeave() {
    this.className = 'empty';
};

function dragDrop() {
    this.className = 'empty';
    this.append(fill);
};