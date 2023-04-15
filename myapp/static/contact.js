      $(document).ready(function() {
  // Preview uploaded image
  $('input[type="file"]').change(function(e){
    var file = e.target.files[0];
    var reader = new FileReader();
    reader.onload = function(e) {
      $('#image-preview').html('<img src="' + e.target.result + '">');
    }
    reader.readAsDataURL(file);
  });
});
$(document).ready(function() {
  // Change background color when color is clicked
  $('.color').click(function() {
    var color = $(this).css('background-color');
    $('#contact-form-wrapper').css('background-color', color);
  });
});
const paletteIcon = document.querySelector('#color-palette-icon');
const colorPicker = document.querySelector('#color-picker');
const colorCircles = document.querySelectorAll('.color-circle');
const submitBtn = document.querySelector('button[type="submit"]');

paletteIcon.addEventListener('click', function() {
    colorPicker.classList.toggle('show');
});

colorCircles.forEach(function(circle) {
    circle.addEventListener('click', function() {
        const color = getComputedStyle(circle).backgroundColor;
        document.body.style.backgroundColor = color;
        submitBtn.style.backgroundColor = color;
    });
});
$(document).ready(function() {
  // Change font size
  $('#font-size').change(function() {
    var fontSize = $(this).val() + 'px';
    $('#contact-form-wrapper').css('font-size', fontSize);
  });

  // Change font family
  $('#font-family').change(function() {
    var fontFamily = $(this).val();
    $('#contact-form-wrapper').css('font-family', fontFamily);
  });
});