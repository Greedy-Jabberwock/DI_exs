//--------------------EXERCISE 1:--------------------

let userAge = Number(prompt("Enter your age:"));
if (userAge < 18) {
    alert("Sorry, you are too young to drive this car. Powering off.");
} 
else if (userAge == 18) {
    alert("Congratulations on your first year of driving. Enjoy the ride!");
}
else if (userAge > 18) {
    alert("Powering On. Enjoy the ride!");
}

//--------------------EXERCISE 2:--------------------

let a = 2 + 2; // assigned to the "a" variable the result of addition (4)

switch (a) {   // variable "a" is transmitting into a switch block
  case 3:                   // this case will work, if "a" = 3. It will be skipped.
    alert( 'Too small' );
    break;
  case 4:                   // this case will work, if "a" = 4. It will be executed.
    alert( 'Exactly!' );    // this line will create the alert message to show the user string "Exactly!"
    break;                  // "break" is a commant to stop execution og this block of code. All next lines before "}" will be not executed.
  case 5:
    alert( 'Too large' );
    break;
  default:                  //This part of code will be executed, if "b" value will not have any coinciedences with other cases.
    alert( "I don't know such values" );
}

//--------------------EXERCISE 2:--------------------

let b = 2 + 2;      // assigned to the "b" variable the result of addition (4)

switch (b) {                // variable "b" is transmitting into a switch block
  case 4:                   // this case will work, if "b" = 4. It will be executed.
    alert('Right!');        // this line will create the alert message to show the user string "Right!"
    break;                  // "break" is a commant to stop execution og this block of code. All next lines before "}" will be not executed.

  case 3:                   // (*) grouped two cases
  case 5:                   // In case when "b" = 5 OR "b" = 3, this piece of code will be executed till before the iterator(?) will find "break" keyword.
    alert('Wrong!');
    alert("Why don't you take a math class?");
    break;

  default:                  //This part of code will be executed, if "b" value will not have any coinciedences with other cases.
    alert('The result is strange. Really.');
}