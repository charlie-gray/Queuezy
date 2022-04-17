<?php
// Access-Control-Allow-Origin header with wildcard. Allows for GET requests
header('Access-Control-Allow-Origin: *');

try{
  // Server settings: UPDATE WITH YOUR INFO
  $servername = "UPDATE W SQL SERVER NAME";
  $username = "SQL SERVER USERNAME";
  $password = "SQL SERVER PASS";

  // Create connection
  $conn = new mysqli($servername, $username, $password);

  // Check connection
  if ($conn->connect_error) {
    echo json_encode($conn->connect_error);
    die();
  }

  // Select database
  $conn -> query("USE LineCounter;");

  // Query based on http header
  if (isset($_REQUEST['device-name'])) {
    $cameraName = $_REQUEST['device-name'];
    $cameraName = urldecode($cameraName);
    $sql = "SELECT * FROM Cameras WHERE cameraName = '{$cameraName}';";

  }
  else {
    $sql = "SELECT * FROM Cameras;";
  }

  $result = $conn->query($sql);


  // Return encoded json
  echo json_encode($result->fetch_object());

  $conn->close();
}
catch(Exception $e) {
  echo json_encode(array(
    'error' => array(
        'msg' => $e->getMessage(),
        'code' => $e->getCode(),
    ),
  ));
}
?>