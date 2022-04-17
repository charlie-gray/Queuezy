# Queuezy - Queue Management Made Easy

## What is Queuezy
Queuezy (pronounced "queue-e-zee") is a simple queue monitoring system designed to allow end users to monitor the length of a line or to view how crowded a space is in real time.

## How Does Queuezy work?
Queuezy uses a state of the art object detection algorithm from Microsoft Azure in order to track people in a given space. In order to use Queuezy, you must acquire an API key from Microsoft. You can learn more [here](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/).

Queuezy works by using an IOT endpoint (like a Raspberry Pi) to capture image data, send the images to the Azure CV Engine, and output Azure's data to a SQL server where it can be served to an end user. 

## Getting Started
Before continuing, make sure you have an API key for Microsoft Azure's Computer Vision service. You can acquire a key [here](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/).

### Setting Up an SQL Server
Queuezy requires a SQL server to store and report queue length data. Keep in mind, multiple cameras can share the same SQL server.

You can set up a SQL server through any method of your choosing, however a prebuilt SQL Docker container is also available in the `SQL Backend` directory. 

To deploy the Docker container, first ensure that the Docker client is installed on your server. 

Next, clone the repository and navigate to the `SQL Backend` directory.

Finally, run the `startDocker.sh` file, and remember to take note of the password you set.

### Setting Up an IOT Endpoint
Your IOT endpoint is what captures images of the queue, sends those images to Azure, and relays the Azure data to our SQL server. It is recommended that you use a device like a Raspberry Pi running a Linux distro of your choice. 

The IOT Endpoint scripts are also Python based, so make sure that Python is installed on your endpoint before continuing.  

First, clone the Queuezy repo onto your endpoint and navigate to the `IOT Endpoint` directory. 

From there, modify the `CameraConfig.json` file with your camera, Azure, and SQL information.

Finally, activate the Python virtual environment.

For Linux/OSX run: `source myvenv/bin/activate`

For Windows run: `myenv\Scripts\activate.bat`

When you're ready to start your endpoint, run the `main.py` script.

### Hosting the Front-End Webapp
First, clone the contents of the `Front End Website` directory into an Apache PHP server.

Make sure to modify the `api.php` file with your SQL server information and the `script.js` file with your camera name, time multiplier, and the hostname of your Apache server.
## *Created for Latin School of Chicago's Algorithms Class*
 \
![algorithms and data structures](/assets/header.jpeg)
 
 \
*This repository and the scripts/files therein are provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. The developers, contributors, and creators of Queuezy, the Queuezy project, and this repository are not responsible for your use of the Queuezy software, the Microsoft Azure service, or any of the scripts, programs, documents, and files within this repository. Ensure you are compliant with local laws, rules, and regulations related to surveillance, privacy, etc., and remember to comply with Microsoft's [policies on customer data](https://www.microsoft.com/trustcenter/cloudservices/cognitiveservices), [Terms of Service](https://www.microsoft.com/en-us/legal/terms-of-use), and [Privacy Policy](https://privacy.microsoft.com/en-us/privacystatement).*

