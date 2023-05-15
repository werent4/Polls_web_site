// Wait for the DOM to be fully loaded before executing the code
document.addEventListener("DOMContentLoaded", function() {
      // Get the user's browser name and version
      function displayBrowserInfo() {
        var browserName = navigator.appName;
        var browserVersion = navigator.appVersion;

        // Display the information to the user
        alert("You are using " + browserName + " version " + browserVersion
        + "requierments are:\n "
        + " version - " + browserVersion );

      }

      // Add event listener to button
      var myButton = document.getElementById("Check-browser");
      myButton.addEventListener("click", displayBrowserInfo);
    });





