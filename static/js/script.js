function Toggle(){
    let button = document.getElementById('toggle_button');
    let pass = document.getElementById('password');
    if(pass.type === 'password'){
        pass.type = 'text';
        button.value = 'HIDE';
    }else{
        pass.type = 'password';
        button.value = 'SHOW';
    }
}

document.getElementById('email_and_phone').onkeyup = function (){
    let email_and_phone = document.getElementById('email_and_phone');

    if(email_and_phone.value.length > 0){
        if(email_and_phone.value.match(/[a-zA-z@._-]+/) != null){
            email_and_phone.type = 'text';
        }else if (email_and_phone.type === 'text'){
            email_and_phone.type = 'tel';

        }
    }
}

function Check(){
    let email_and_phone = document.getElementById('email_and_phone');
    let pass = document.getElementById('password');

    console.log(email_and_phone.value + "\n" + pass.value)
    if(email_and_phone.value == null || email_and_phone.value === ''){
        return false;
    }
    if(pass.value == null || pass.value === ''){
        return false;
    }
    email_and_phone.value = iti.getNumber();
    return true;
}

function checkMail(mail){
    if(mail.match(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/) != null){
        return true;
    }
    return false;
}

document.getElementById('email_and_phone').onkeyup = function (ev){
    /*let email_and_phone = document.getElementById('email_and_phone');

    if(email_and_phone.value.match(/[a-zA-z@._-]+/) != null && email_and_phone.value.length >= 5){
        if(checkMail(email_and_phone.value)){
            document.getElementById('warningEmail').style.display = 'none';
        }else{
            document.getElementById('warningEmail').style.display = 'block';
        }
    }*/
}

document.getElementById('password').onkeyup = function(ev){

    let pass = document.getElementById('password');

    if(pass.value.length < 4 || pass.value.length > 60){
        document.getElementById('warningPassword').style.display = 'block';
    }else{
        document.getElementById('warningPassword').style.display = 'none';
    }
}