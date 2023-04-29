$(function () {
  $(".showHidePw").each(function () {
    $(this).click(function () {
      console.log($(this).siblings()[0].type);
      if ($(this).siblings()[0].type == "text") {
        $(this).siblings()[0].type = "password";
        $(this)[0].classList.replace("uil-eye", "uil-eye-slash");
      } else {
        $(this).siblings()[0].type = "text";
        $(this)[0].classList.replace("uil-eye-slash", "uil-eye");
      }
    });
  });
});
