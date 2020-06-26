function myFunction() {
  var copyText = document.getElementById("myUrl");
  co
  copyText.select();
  document.execCommand("copy");
}
jQuery(document).ready(function($){
var url = document.location.href;
new Clipboard('.copy_link', {text: function(){ return url;}});
$('.copy_link').click(function(){alert('Cсылка успешно скопирована в буфер обмена.');});
});