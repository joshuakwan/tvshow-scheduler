function getTime() {
  var today = new Date();
  var h = today.getHours();
  var m = today.getMinutes();
  var s = today.getSeconds();

  m = checkTime(m);
  s = checkTime(s);

  return h + ":" + m + ":" + s;
}

function checkTime(i) {
  if (i < 10) {
    i = "0" + i;
  }
  return i;
}
