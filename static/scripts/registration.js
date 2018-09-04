// TODO -> Make a better email validator w/ RegEx
// TODO -> Customize popUP alert window
// =============================================== //
// This JS file is tied to the registration page and validates all the form fields

var isValid = false

function validateForm() {

    // Create all the placeholders for all the form information
    let username = document.forms["register"]["username"];
    let password = document.forms["register"]["password"];
    let passwordConfirmation = document.forms["register"]["confirmation"];
    let email = document.forms["register"]["email"];

    let isValid = false

    // Username field empty
    if (username.value == "")
    {
        window.alert("Please enter a Username");
        username.focus();
        return false;
    };

    // Password field empty
    if (password.value == "")
    {
        window.alert("Please enter a Password");
        password.focus();
        return false;
    };

    // Password confirmation doesn't match
    if (password.value != passwordConfirmation.value)
    {
        window.alert("Passwords do not match");
        passwordConfirmation.focus();
        return false;
    };

    // Make sure email has "@"
    if (!email.value.includes("@"))
    {
        window.alert("Must enter a valid email address");
        email.focus();
        return false;
    };

    // window.alert("You have registered succesfully. Welcome to Web RPG")
    
    return false;

}

function usernameXHR(isValid){

    // To see if Username in db, make a request to server using XMLH..
    var xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function(){
        if(this.readyState == 1){
            console.log("Ready State 1")
        }

        if(this.readyState == 2){
            console.log("Ready State 2")
        }

        if(this.readyState == 3){
            console.log("Ready State 3")
        }

        if(this.readyState == 4){
            console.log(xhr.responseText)
        }
    }

    xhr.open('POST', '/register/validate', true);
    xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded; charset=UTF-8');
    
    var username = document.getElementById('username').value;
    var postVar = 'username ='+username;

    xhr.send(postVar)

    return false
}