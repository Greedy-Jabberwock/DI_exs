const rows = 10;
const columns = 19;
const gridSqr = rows * columns;


let createGrid = () => {
    let container = document.createElement('div');
    container.classList.add('container');
    container.style.margin = '10vh 40vw';
    container.style.display = 'grid';
    container.style.gridTemplateRows = `repeat(${rows}, auto)`;
    container.style.gridTemplateColumns = `repeat(${columns}, auto)`;
    container.style.width = '15vw';
    container.style.height = '40vh';
    document.querySelector('body').appendChild(container);


    for (let i = 0; i < gridSqr; i++) {
        let div = document.createElement('div');
        div.style.height = '4vh';
        div.style.width = '1vw';
        div.style.alignSelf = 'center';
        div.style.backgroundColor = 'aquamarine';
        container.appendChild(div);
    }
}

let makeA = () => {
        let cells = document.querySelectorAll('.container > div');
        let currentCellIndex = 0;
        let edgeArray;
        let middleArray;
        let endArray;
        let line;
        for (let r = 0; r < rows; r++) {
            switch(r) {
                case 0:
                    edgeArray = (' '.repeat((columns-1)/2)).split('');
                    middleArray = ['*'];
                    endArray = (' '.repeat((columns-1)/2)).split('');
                    break;
                case 1:
                    let swap = middleArray[0];
                    edgeArray[edgeArray.length - 1] = swap;
                    endArray[0] = swap;
                    middleArray[0] = edgeArray[0];
                    break;
                case 5:
                    middleArray.push(edgeArray.shift());
                    middleArray.push(endArray.pop());
                    for (let i = 0; i < middleArray.length; i++) {
                        middleArray[i] = '*';
                    }
                    break;
                default:
                    middleArray.push(edgeArray.shift());
                    middleArray.push(endArray.pop());
                    for (let i = 0; i < middleArray.length; i++) {
                        middleArray[i] = ' ';
                    }
            }
            
            line = edgeArray.concat(middleArray).concat(endArray);
            console.log(`R: ${r}\nLine: ${line.toString()}`)
            for (let c = 0; c < columns; c++) {
                cells[currentCellIndex].innerHTML = line[c];
                currentCellIndex++;
            }
        }
    }   

createGrid();
makeA();