let planets = [{
        name:'Sun',
        color: 'hsl(30deg 86% 55%)',
        sattelites: 0
    },
    {
        name:'Mercury',
        color: 'hsl(180deg 1% 37%)',
        sattelites: 0
    },
    {
        name:'Venus',
        color: 'hsl(28deg 88% 38%)',
        sattelites: 0
    },
    {
        name:'Earth',
        color: 'hsl(92deg 57% 47%)',
        sattelites: 1
    },
    {
        name:'Mars',
        color: 'hsl(1deg 97% 26%)',
        sattelites: 2
    },
    {
        name:'Jupiter',
        color: 'hsl(16deg 76% 38%)',
        sattelites: 80
    },
    {
        name:'Saturnus',
        color: 'hsl(281deg 28% 50%)',
        sattelites: 84
    },
    {
        name:'Neptune',
        color: 'hsl(195deg 87% 37%)',
        sattelites: 14
    },
    {
        name:'Uranus',
        color: 'hsl(187deg 88% 63%)',
        sattelites: 27
    }
]

let listPlanetsEL = document.querySelector('.listPlanets');
console.log(listPlanetsEL);

planets.forEach((item) => {
    let planetName = item.name;
    let planetColor = item.color;
    let moons = item.sattelites;
    let divEl = document.createElement('div');
    divEl.classList.add('planet', planetName);
    // if (planetName != 'Sun') {
    //     divEl.classList.add('moon');
    // }
    divEl.style.backgroundColor = planetColor;
    divEl.innerHTML = planetName;
    for (let i = 0; i < moons; i++) {
        let moonDiv = document.createElement('div');
        moonDiv.classList.add('moon');
        divEl.appendChild(moonDiv);
    }
    listPlanetsEL.appendChild(divEl);
})