let listsTasks = [];
let index = 0;

let addTask = (e) => {
    e.preventDefault();
    let inputText = document.forms[0].elements[0].value;
    let indexId = 'index'.concat(String(index));
    let pattern = /^\S+/;
    if (inputText != '' && inputText.match(pattern) != null) {
        let task = {
            id: indexId,
            text: inputText,
            done: false,
        }
        listsTasks.push(task);
        index++;
        createElements();
    } else {
        alert('Task cannot be empty.')
        return false;
    }
};

let createElements = () => {
    let div = document.querySelector('.listTasks');
    div.innerHTML = '';
    listsTasks.forEach(item => {
        let checked = item.done ? ' checked' : '';
        let cross = item.done ? ' class="redcross"' : '';
        let taskEl = `<div data-task-id='${item.id}'><i class='fa fa-ban'></i><input type='checkbox'${checked}><span${cross}>${item.text}</span></div>`
        div.innerHTML += taskEl;

        document.forms[0].elements[0].value = '';
    })
    let checkboxes = div.querySelectorAll('input');
    checkboxes.forEach((item, index) => {
        let tasksSpan = document.querySelectorAll('span');
        item.addEventListener('click', () => {
            if (item.checked) {
                listsTasks[index].done = true;
                tasksSpan[index].classList.add('redcross');
            } else {
                listsTasks[index].done = false;
                tasksSpan[index].classList.remove('redcross');
            };
        });
    })
    let tasks = document.querySelectorAll('i');
    tasks.forEach((item, index) => {
        item.addEventListener('click', () => {
            listsTasks.splice(index, 1);
            createElements();
        })
    })
};

let getTaskList = () => {
    let list = document.querySelectorAll('.listTasks > div');
    return list;
}


document.forms[0].addEventListener('submit', addTask);
