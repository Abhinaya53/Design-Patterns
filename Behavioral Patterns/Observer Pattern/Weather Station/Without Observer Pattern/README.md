Even though this method works and the device is notified of current temperature 
whenever there is a change, this is not ideal because:
- The classes Device and WeatherStation are tightly coupled. Which means if we 
  want to add or remove device we would have to update the code in WeatherStation.
  This leads to poor scalability and flexibility.
