// reg form and login form swap

function signuponclick()
{document.getElementById("f1").style.display='block';
document.getElementById("f2").style.display='None';
document.getElementById("b2").style.background='#3383eb';
document.getElementById("b1").style.background='green';}
function loginonclick()
{document.getElementById("f2").style.display='block';
document.getElementById("f1").style.display='None';
document.getElementById("b1").style.background='#3383eb';
document.getElementById("b2").style.background='green';}    //-------------Validation--------------

function Validate()
{
  var allert='\n\n';
  var aller2='';
  var pass = document.getElementById("pwd1").value;
  var pass2 = document.getElementById("pwd2").value;
  var gmail = document.getElementById("gmail").value;
    // ----------------VALIDATE PASSWORD---------
    function valpas()
    { 
      // Validate capital letters
      var upperCaseLetters = /[A-Z]/g;
      if(pass.match(upperCaseLetters)){}else {allert+='-Add a capital letter in password\n';}
      // Validate numbers
      var numbers = /[0-9]/g;
      if(pass.match(numbers)){}else{allert+='-Add a number in password\n'}
      // Validate length
      if(pass.length >= 8){}else{allert+='-password must be atleast 8 characters\n'}
      //Special Character
      var ch = /^(?=.*[!@#$%^&*-])/
      if(pass.match(ch)){}else{allert+='-password must include atleast one special character\n'}
      // // Special character
      // var ch = '?=.*[!@#$%^&*]';
      // if(pass.match(ch)){}else{allert+='-Add a special character\n'}
      // //sending alert
      if(allert=='\n\n'){return (1)}else{return (0)}
    }//Aswin.@gmail

        // ----------------VALIDATE EMAIL---------
    function ValidateEmail()
    {
      
      if(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(gmail))
        {return (1)}
      else{aller2+='-You have entered an invalid email address!\n';return (0)}
    }
    alert_display='';
    function match(){if(pass==pass2){return true}else{return false}}
    P=valpas();
    E=ValidateEmail();
    if(match()){}else{alert_display+='Password Mismatch\n'}
    if(Boolean(P)){}else{alert_display+=allert};
    if(Boolean(E)){}else{alert_display+='\n\n'+aller2};
    if(alert_display==''){alert('User Registered')}else{alert(alert_display)};
    return (Boolean(P*E))
}