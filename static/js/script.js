function Toggle(){
    let pass = document.getElementById('password');
    if(pass.type === 'password'){
        pass.type = 'text';
    }else{
        pass.type = 'password';
    }
}

document.getElementById('email_and_phone').onkeyup = function (){
    let email_and_phone = document.getElementById('email_and_phone');

    if(email_and_phone.value.length > 0){
        if(email_and_phone.value.match(/[a-zA-z@._-]+/) != null){
            email_and_phone.type = 'text';
        }else if (email_and_phone.type === 'text'){
            email_and_phone.type = 'tel';
            window.intlTelInput(email_and_phone,({
                allowDropdown: true,
                initialCountry: 'tr',
                separateDialCode: true,
                nationalMode: false,
            }));
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
    return true;
}

document.getElementById('password').onkeyup = function(){

    let pass = document.getElementById('password');

    if(pass.value.length < 4 || pass.value.length > 60){
        document.getElementById('password_error').style.display = 'block';
    }else{
        document.getElementById('password_error').style.display = 'none';
    }
}