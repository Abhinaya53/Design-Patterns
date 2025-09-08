# Problem:
Suppose we are developing a Data Analysis Application which works with CSV data files and parses the data from it and analyses the parsed data to produce colourful charts and report files. Now we decide to integrate a 3rd party analytics library to improve the app. But the third party library only works with data JSON data format.

# Naive Approach:
Naive way of handling this would be changing the library code to work with CSV files. Which might potentially break the library's code. But if we don't have access to the library's code. In this case the client will have to convert the JSON files to CSV before passing it to our application. 
The problems with this approach are:
- OCP is violated because any new data provider forces changes in the client.
- DIP violated as client depends directly on a concrete external API.
- Conversion logic gets a mixed with business logic. Which violates SRP.

# Solution: Adapter Pattern
To solve this problem we can use the Adapter Pattern. 
- We can create an adapter class which implements the CSV data provider interface. 
- This adapter class will internally use the JSON data provider to fetch the data and convert it to CSV format. 
- This way we can keep the client code unchanged and also adhere to OCP, DIP and SRP principles.