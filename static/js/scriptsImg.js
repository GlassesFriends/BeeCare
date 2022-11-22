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
