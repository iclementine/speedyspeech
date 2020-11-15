function synt(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     console.log(this.responseText);
    }
  };
  let route = "synthesize/" + $('#textInput').val();
  xhttp.open("POST", route, true);
  xhttp.send();
}
