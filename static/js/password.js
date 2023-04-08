
function ShowMePassword() {
  var passwordInput = document.querySelector("input[name='password']");
  var showPasswordButton = document.getElementById("show_password");
  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    showPasswordButton.innerHTML = '<span class="fa fa-eye icon"></span>';
  } else {
    passwordInput.type = "password";
    showPasswordButton.innerHTML = '<span class="fa fa-eye-slash icon"></span>';
  }
}

function ShowMePassword1() {
    var passwordInput = document.querySelector("input[name='password1']");
    var showPasswordButton = document.getElementById("show_password1");
    if (passwordInput.type === "password") {
      passwordInput.type = "text";
      showPasswordButton.innerHTML = '<span class="fa fa-eye icon"></span>';
    } else {
      passwordInput.type = "password";
      showPasswordButton.innerHTML = '<span class="fa fa-eye-slash icon"></span>';
    }
  }

  function ShowMePassword2() {
    var passwordInput = document.querySelector("input[name='password2']");
    var showPasswordButton = document.getElementById("show_password2");
    if (passwordInput.type === "password") {
      passwordInput.type = "text";
      showPasswordButton.innerHTML = '<span class="fa fa-eye icon"></span>';
    } else {
      passwordInput.type = "password";
      showPasswordButton.innerHTML = '<span class="fa fa-eye-slash icon"></span>';
    }
  }