var image = null;
var redimage = null;
var rainbowimage = null;
var borderimage = null;


document.getElementById("id_file").onchange = function() {
  var canvas = document.getElementById ("pic");
  var fileinput = document.getElementById ("id_file");
  image = new SimpleImage(fileinput);
  image.drawTo(canvas);
}

