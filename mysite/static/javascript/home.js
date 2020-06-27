function copyTextToClipboard() {
  var root = location.protocol + '//' + location.host;
  const el = document.createElement('textarea');
  el.value =root + document.getElementById("myUrl").text;
  document.body.appendChild(el);
  el.select();
  document.execCommand('copy');
  document.body.removeChild(el);
}