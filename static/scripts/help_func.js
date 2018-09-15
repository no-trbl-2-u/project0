// Configure & Send XMLHttpRequest to update Models
function updateModels(){

    // Create request
    let xhr = new XMLHttpRequest();

    // Configure SETTINGS of request
    xhr.open('GET', '/index/updateModels', true);
    xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded; charset=UTF-8');

    // Send the configured request
    xhr.send();

    return true;
};