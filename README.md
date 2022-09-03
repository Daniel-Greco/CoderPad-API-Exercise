# CoderPad-API-Exercise

Exercise provided by CoderPad: https://coderpad.io/resources/docs/question-bank/example-questions/#http-api-calls

This is one solution to the practice exercise provided by CoderPad. Description of the exercise provided by CoderPad:
```
Your task is to create a function that makes an API call to request an HTML page, and parse through the HTML to retrieve a soccer team's logo.

This function should work for every single team page from https://www.premierleague.com link. In the case the URL is not valid - you should return an error message.

An example:
Request: "https://www.premierleague.com/clubs/10/Liverpool/overview"
Response: "https://resources.premierleague.com/premierleague/badges/t14.png"

You can use C++, Java, JavaScript, Python or Ruby. Some of these languages have request libraries. 
Others you will have to use the language's default HTTP methods. 
To see the available packages/libraries for the language you choose, simply click on the info button located next to the language.

We have included test cases that will allow you to see if your code will pass or fail. 
The string must match exactly to pass. In the case of no image in the page, please return the message "No image found!". 
To view the test cases, you can view the test case tab, or when you run the code, you will see each test in the console and whether it failed or passed. 
You can log your output in the console at any time as well.

Good luck!
```


## Features

* Make an api call to the club page of the premier league website to search for the team logo. 
* If the team has a logo, return the logo image path.
* If no logo is found, the phrase 'no image found!' should be returned. 


## Current state

> Complete - all features implemented. 


## Usage

Flags are used to add optional features:
* URL  : The premier league team page to search for the logo. 

To run the base application from command line:
```bash
CoderPad_API_Call.py [URL]
```


## How It Works

The application takes in the url provided and makes an API get request to the page. The page is returned and then is searched for the HTML tag 'clubBadgeFallback' as this tag provides the link to the team logo. The application confirms there is a .png file in the tag and then returns the string formatted as a link to the command line. In the case the URL provided does not contain the image, the phrase 'no image found!' is returned.
