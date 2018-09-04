count = 0;


// When the window loads, start the listener on the
// button. When the button is clicked
// trigger the clickHandler

window.onload=function(){
    var btn = document.getElementById("btn");
    btn.addEventListener("click", clickHandler);
}


var a = `First, you must declare element you would like to modify via an event.
            You can do this by using ________________________ 
            varName = document.getElementById("#selector")`;


var b = "String 2";
var c = "String 3";


function clickHandler() {

    textEle = document.getElementById("text");

    if(count % 3 === 0){
        textEle.innerHTML = a;
    };

    if(count % 3 === 1){
        textEle.innerHTML= b;
    };
    
    if(count % 3 === 2){
        textEle.innerHTML = c;
    };

    count += 1;
};
