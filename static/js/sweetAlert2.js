function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min + 1) ) + min;
  }
  function WorkerLogOut(url) {
    Swal.fire({
        title: 'Are you sure?',
        text: "Would you like to finish your sesion?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#e74a3b',
        cancelButtonColor: '#4e73df',
        confirmButtonText: 'Log out!'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = url
        }
    })
}
function MessageConfirm(tittle, text, ur){
    dog = getRndInteger(0,5)
    Swal.fire({
        title: tittle,
        html: 
            '<img class="rounded-circle mb-3 mt-4"src="../' + '../static/img/worker/worker_worker_image' + dog + '.png' + '" width="160" height="160">'+
        '<h2>' + text + '</h2>',
        text: text,
        imageWidth: 400,
        cancelButtonText: 'Stay at register',
        imageHeight: 200,
        imageAlt: 'Custom image',
      })
}
function WorkerSignUpSuccess(url) {
  Swal.fire({
      title: 'Welcome',
      text: "Would you like to sign in now?",
      icon: 'Success',
      showCancelButton: true,
      cancelButtonText: 'Stay here',
      confirmButtonColor: '#e74a3b',
      cancelButtonColor: '#4e73df',
      confirmButtonText: 'Sign in!'
  }).then((result) => {
      if (result.isConfirmed) {
          window.location.href = url
      }
  })
}
function LoginError(text){
    Swal.fire({
            "title":'Your user or password is not correct',
            "text":text,
            "icon":"warning",
            "confirmButtonText":"Ok",
            "confirmButtonColor":"#dc3545",
        })
    }