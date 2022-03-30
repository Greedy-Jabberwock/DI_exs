let sentence = prompt("Enter the sentence:");
let notIndex = sentence.toLowerCase().indexOf("not");
let badIndex = sentence.toLowerCase().indexOf("bad");

if (notIndex == -1 || badIndex == -1) {
    alert(sentence);
} 
else if (notIndex < badIndex) {
    let pattern = /\w?(not)...*(bad)\w?/;
    alert(sentence.replace(pattern, "good"));
}