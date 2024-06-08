random_background_color_id = Math.floor(Math.random() * 10);
const background_colors = ["aquamarine", "lightblue", "orange", "yellowgreen", "greenyellow","blue", "pink", "black", "purple"];
var body = document.getElementById("body")
body.style = "background-color:"+background_colors[random_background_color_id]+";"