// Update your info here
var cameraName = "UPDATE WITH NAME"
var secondsPerPerson = 15; // Time multiplier for each person. Measured in seconds
var hostname = "HOSTNAME.com";


// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest();

// Open a new connection, using the GET request on the URL endpoint
//Substitute your endpoint here
request.open('GET', "http://" + hostname + '/api.php?device-name=' + cameraName, true);

request.onload = function () {
  //get data from api
  let data = JSON.parse(this.response);

  //Calculate line length
  lineTime = parseInt((parseInt(data.peopleCount) * secondsPerPerson) / 60)

  if (lineTime < 1){
    lineTime = "< 1 Minute";
  }
  else if (lineTime < 60){
    lineTime = String(lineTime) + " minutes";
  }
  else {
    lineTime = String(lineTime / 60) + " hours";
  }
  
  // Update webpage
  document.getElementById("time-data").innerHTML = lineTime;
  document.getElementById("camera-label").innerHTML = "For " + cameraName;

  document.getElementById("last-updated").innerHTML = "Last updated: " + data.lastUpdated.split(".")[0];
 }

 // Update time + page name
let currentDate = new Date();

if (currentDate.getHours() > 12){
  document.getElementById("greet-txt").innerHTML = "Good Afternoon";
}

document.title = cameraName;

// Send request
request.send();
