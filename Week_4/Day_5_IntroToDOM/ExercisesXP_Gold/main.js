//----------------------------------Exercise 1-------------------------------------------

console.log('==================\nExercise 1 : My Book List\n==================')

//_____________________________________FUNCTIONS______________________________________________
let createBookCard = (object) => {
    let book = object;
    let title = book.title;
    let author = book.author;
    let image = book.image;
    let alreadyRead = book.alreadyRead;
    
    let imgBookCard = createImageDiv(image);
    
    let descrBookCard = createDescrDiv(title, author, alreadyRead);

    let newBookDiv = document.createElement('div');
    newBookDiv.classList.add('book-card');

    newBookDiv.appendChild(imgBookCard);
    newBookDiv.appendChild(descrBookCard);

    let bookListEl = document.querySelector('.listBooks');
    bookListEl.appendChild(newBookDiv);
    makeStyle();
}

let createImageDiv = (urlValue) => {
    let imgDiv = document.createElement('div');
    imgDiv.classList.add('book-image')
    let imgEl = document.createElement('img');
    imgEl.setAttribute('src', urlValue);
    imgDiv.appendChild(imgEl);

    return imgDiv;
} 

let createDescrDiv = (bookTitle, bookAuthor, alreadyRead) => {
    let descrDiv = document.createElement('div');
    descrDiv.classList.add('book-title')
    if (alreadyRead) {
        descrDiv.classList.add('already-read');
    }
    let descrElement = document.createElement('p');
    let description = `'${bookTitle}' was written by ${bookAuthor}`;
    let textNode = document.createTextNode(description);
    descrElement.append(textNode);
    descrDiv.appendChild(descrElement);

    return descrDiv;
} 

let makeStyle = () => {
    let bookCard = document.querySelectorAll('.book-card');
    let image = document.querySelectorAll('.book-image > img');
    let descr = document.querySelectorAll('.book-title');
    let alreadyRead = document.querySelectorAll('.already-read');
    
    bookCard.forEach(element => {
        element.style.display = 'flex'
        element.style.margin = '10px 15px'
    });
    
    image.forEach(element => element.style.width = "100px");

    descr.forEach(element => {
        element.style['align-self'] = 'center';
        element.style.margin = '0 2vw';
        element.style['font-size'] = '4vh'
    });
    
    alreadyRead.forEach(element => element.style.color = 'red');

}

//_____________________________________VARIABLES______________________________________________

let allBooks = [
    {
        title: "Call of Cthulhu",
        author: "Howard F.Lovecraft",
        image: 'https://i.thenile.io/r1000/9781500584337.jpg',
        alreadyRead: true,
    },
    {
        title: "I have no mouth & I must scream",
        author: "Harlan Ellison",
        image: 'https://www.harlanellisonbooks.com/wp-content/uploads/2018/01/Shoppe079-scaled.jpg',
        alreadyRead: true,
    },
];

//_______________________________________MAIN_________________________________________________

allBooks.forEach(createBookCard);
