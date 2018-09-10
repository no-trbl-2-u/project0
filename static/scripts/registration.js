// TODO -> Make a better email validator w/ RegEx
// TODO -> Customize popUP alert window
// TODO -> FIX SCRIPT TO BE ASYNC
// TODO -> 
// =============================================== //
// This JS file is tied to the registration page and validates all the form fields

// Main Logic -> Event Listeners
document.addEventListener("DOMContentLoaded", () =>{

    // Placeholders for common elements among events
    let button = document.getElementById("submit");
    let usernameField = document.getElementById("username");


    // When user goes to next field, send request to verify username
    usernameField.addEventListener("blur", () =>{

        // Send AJAX request to get the value for isValid
        let isValid = isValidUsername();

        // Response Handler
        (isValid) ?
            usernameGood(button, usernameField)
            : usernameBad(button, usernameField);
    });


    // Validate fields, resend isValid AJAX, submit form
    button.addEventListener("click", (event) =>{

        // Create placeholders for results of validation calls
        let fullFormValidation = validateForm();
        let databaseValidation = isValidUsername();

        // Logic to either submit form or stop it
        if(fullFormValidation === true && databaseValidation === true){
            window.alert("Thank you for registering!");
            return true
        };
        if(databaseValidation === false){
            window.alert("Username already in use")
            event.preventDefault();
        }else{
            event.preventDefault();
        };
    });
});

// Make sure form isn't empty
function validateForm() {

    // Create all the placeholders for all the form information
    let username = document.forms["register"]["username"];
    let password = document.forms["register"]["password"];
    let passwordConfirmation = document.forms["register"]["confirmation"];
    let email = document.forms["register"]["email"];

    // Username field empty
    if (username.value == "")
    {
        window.alert("Please enter a Username");
        username.focus();
        event.preventDefault();
        return false;
    };

    // Password field empty
    if (password.value == "")
    {
        window.alert("Please enter a Password");
        password.focus();
        event.preventDefault();
        return false;
    };

    // Password confirmation doesn't match
    if (password.value != passwordConfirmation.value)
    {
        window.alert("Passwords do not match");
        passwordConfirmation.focus();
        event.preventDefault();
        return false;
    };

    // Make sure email has "@"
    if (!email.value.includes("@"))
    {
        window.alert("Must enter a valid email address");
        email.focus();
        event.preventDefault();
        return false;
    };

    return true;
}

// Configure & Send XMLHttpRequest
function isValidUsername(){

    // Create request
    let xhr = new XMLHttpRequest();

    // Configure SETTINGS of request (ASYNC FALSE BECAUSE YOU SUCK!)
    xhr.open('POST', '/register/validate', false);
    xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded; charset=UTF-8');
    
    // Configure CONTENTS of request
    let username = document.getElementById('username').value;
    let postVar = 'username='+username;

    console.log("in isValidUsername -> postVar: " + postVar)

    // Send the configured request
    xhr.send(postVar)

    // Since it's not async, the response can be used here
    let response = JSON.parse(xhr.responseText)
    console.log("in isValidUsername -> response: " + response['isValid']);

    return response['isValid']
}

// Callback function for successful blur event
function usernameGood(button, usernameField){
    console.log("Finishline")
    button.disabled = false;
}

// Callback function for failed blur event
function usernameBad(button, usernameField){
    window.alert("Username already in use")
    button.disabled = true;
}