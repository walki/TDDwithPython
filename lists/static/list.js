$('input').on('keypress', function () {
  $('.has-error').hide();
  console.log($(this).text())
});
