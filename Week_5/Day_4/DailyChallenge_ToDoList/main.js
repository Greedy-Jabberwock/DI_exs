let listsTasks = [];

function addTask(e) {
    e.preventDefault();
    let value = this.elements[0].value;
    let pattern = /^\S+/
    if (value != '' && value.match(pattern) != null) {
        let id = saveElement(value);
        this.elements[0].value = '';
        createTaskElement();
    } else {
        alert('Enter something.');
        this.elements[0].value = '';
    }
};

function createTaskElement(value) {
    let div = document.querySelector('.listTasks');

    let container = document.createElement('div');
    container.classList.add('flex');

    let span = document.createElement('span');
    span.classList.add('fa', 'fa-ban');
    span.classList.add('margin');

    let checkbox = document.createElement('input');
    checkbox.setAttribute('type', 'checkbox');
    checkbox.classList.add('margin');
    checkbox.addEventListener('click', toggleStyle);

    let p = document.createElement('p');
    p.style.display = 'inline-block';
    p.classList.add('margin');
    p.innerHTML = value;

    container.append(span);
    container.append(checkbox);
    container.append(p);
    div.appendChild(container);
}

function toggleStyle() {
    this.nextSibling.classList.toggle('redcross');
};

function saveElement(value) {

}

document.forms[0].addEventListener('submit', addTask);