// TODO -> Make a better email validator w/ RegEx
// TODO -> Customize popUP alert window
// =============================================== //
// This JS file is tied to the registration page and validates all the form fields



document.addEventListener("DOMContentLoaded", () =>{

    console.log("DOM Loaded...")

    // Create placeholder for username field 
    let usernameField = document.getElementById("username");

    // When user goes to next field, send request is verify username
    usernameField.addEventListener("blur", () =>{
        let isValid = isValidUsername(usernameField.value);

        console.log("Inside DOMLoaded after onblur")
        console.log("This is the return value of isValid =>" + isValid)
    })

});

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

function isValidUsername(username){

    let dataPlaceHolder = "";
    let dataPlaceHolder2 = [];

    getText = function(url, callback){
        // Initialize the request
        let request = new XMLHttpRequest();

        // onstatechange, run ->
        request.onload = function(){
            if (request.readyState == 4 && request.status == 200){

                console.log("Inside onload")

                 console.log("Callback = " + callback(JSON.parse(request.responseText))); // Another callback here

                console.log("Inside onload, after callback")

                return callback(JSON.parse(request.resposeText))
            }
        };

        // Configure the request settings 
        request.open('POST', url);
        request.setRequestHeader('content-type', 'application/x-www-form-urlencoded; charset=UTF-8');
        let postVar = 'username='+username;

        // Send the configured request
        request.send(postVar);
        console.log("Inside getText ")
    };

    function responseFunction(response, DPH1, DPH2){
        let data = response['isValid'];
        DPH1 = response;

        // DPH2.push(response['isValid']);

        console.log("Inside the callback function ->" + data)

        return data
    }

    return getText('/register/validate', responseFunction, dataPlaceHolder, dataPlaceHolder2)
    
    console.log("Inside isValidUsername, after getText")
    console.log("Inside isValidUsername, ->" + test)
}