var load_ImgBee = function(event) {
    let output = document.getElementById('previewSightingReg');
    output.src = URL.createObjectURL(event.target.files[0]);
    output.onload = function() {
      URL.revokeObjectURL(output.src) // free memory
    }
};

var load_Profile = function(event) {
  let output1 = document.getElementById('img_profile');
  output1.src = URL.createObjectURL(event.target.files[0]);
  output1.onload = function() {
    URL.revokeObjectURL(output1.src) // free memory
  }
};

function autoField_first_name(){
  let user_fname = document.getElementById("membFirstName").value;
  document.getElementById("first_name").value = user_fname;
 }
 
 function autoField_last_name(){
   let user_lname = document.getElementById("membLastName").value;
   document.getElementById("last_name").value = user_lname;
  }
 
  function autoField_mail(){
   let user_mail = document.getElementById("membEmail").value;
   document.getElementById("username").value = user_mail;
  }
 
 