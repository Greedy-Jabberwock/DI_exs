let element = document.getElementById("dI");

for (let attr of element.attributes) {
    console.log(attr.name + ' = ' + attr.value);
}