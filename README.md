# Guessing Game

(Developer: Morgan Asare)

[Link to the website](https://worldguessinggame-6a1c3a2b64fc.herokuapp.com/)

![An image previewing all devices](/assets/screenshots/preview.png)

## Table of Content

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requrements-and-expectations)
3. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks & Tools](#frameworks-&-tools)
4. [Features](#features)
5. [Testing](#validation)
    1. [Application Testing](#performing-tests-on-various-devices)
6. [Bugs](#Bugs)
7. [Deployment](#deployment)
8. [Credits](#credits)
9. [Acknowledgements](#acknowledgements)

## Project Goals
### User Stories

- Be able to sign up as new user
- Be able to login as existing user
- Be able read the rules of the game
- Be able to play a simple game of country guessing game

### Site Owner Goals
- Ensure user is able to create a user account
- Ensure user is able to enter username, email and password
- Ensure user is able to Login with username password already created
- Ensure user can read the instructions before playing the game
- Ensure the game is intuitive
- Ensure user is able to restart the game


## User Experience
### Target Audience

- User is able to create an account 
- User is able to login to the account
- User is able to find the instructions
- User is able to play the game easily

## Technologies Used

## Technical Design 
### Flowchart

- [Lucidchart](https://www.lucidchart.com) was used to build flowchart

<details>
    <summary>Flowchart</summary>
    <p>GuessGame Game Flowchart</p>
    <img src = "assets/screenshots/flowchart.png" alt = "A screenshot of flowchart">
</details>

## Language Used
 - Python

## Libraries Used
- os - used to clear terminal
- random - used to choose random words
- re used for regex

### 3rd Party Python Libraries used
- Google sheets API was used to store and check the user input and authorise the user identity
- Google OAuth was used to connect the project with google account

### Other websites/tools used

- [GitHub](https://github.com/) was used for saving and storing files.
- [Heroku](https://www.heroku.com/) was used as the deploying platform for this site.

<details>
    <summary>Hosted App on Heroku</summary>
    <img src="assets/screenshots/logout.png" alt="Game load page">
</details> 

## Features

## Login and SignUp
 - The first page welcomes the user to the game
 - Then User is asked if they already have an account or not
 - User gets a yes or no prompt for the program to proceed

 <details>
    <summary>Home Page screenshot</summary>
    <img src="assets/screenshots/main_screen.png" alt="Game load page">
</details> 

- If user has no account, the no answer takes them to the signup page
- User provides username, email and password
- email is in the format example@address.com

## Game page

- Game page loads once the user username and passwords are validated

 <details>
    <summary>Game Page screenshot</summary>
    <img src="assets/screenshots/game_page.png" alt="Game load page">
</details> 

## Game starts

- User starts by guessing random letters that might form a country word
- User has 10 tries to guess the correct country

<details>
    <summary>Game Start Page screenshot</summary>
    <img src="assets/screenshots/game_starts.png" alt="Game load page">
</details> 

## Restart Game

- When User finish playin and wins there is a congratulation message
- User is asked if they want to play again

<details>
    <summary>Finish Page screenshot</summary>
    <img src="assets/screenshots/finish_game.png" alt="Game load page">
</details> 

- If they selected yes for restart the game starts 

<details>
    <summary>Restart Page screenshot</summary>
    <img src="assets/screenshots/restart.png" alt="Game load page">
</details> 

- If user decides to end the game by selecting no
- A goodbye message is displayed and prompted the application is logging out

<details>
    <summary>Logout Page screenshot</summary>
    <img src="assets/screenshots/logout.png" alt="Game load page">
</details> 


## Testing

- Manual testing of user stories
- Testing on Browsers
- Tested Devices with Browsers
- Validator Testing

### Manual Testing
<details><summary>See user stories testing</summary>

1. I want to be able to have an option as existing user or new user

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Are you an existing user | Type Y/N | Y: Open login area / N: SignUp Area | Works as expected
<details>
    <summary>Screenshots</summary>
    <p>Sign Up</p>
    <img src="assets/screenshots/welcome.png" alt="Sign up area">
    <p>Log In</p>
    <img src="assets/screenshots/login.png" alt="Login area">
</details> 

2. I want to able to signup as new user

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Sign Up Here | Enter New Username/ Enter New Password | Sign Up Complete : Login Page opens | Works as expected
<details>
    <summary>Screenshots</summary>
    <p>Sign Up Area</p>
    <img src="assets/screenshots/signup_checks.png" alt="Sign up area">
    <p>Login area opens after sign up is confirmed</p>
    <img src="assets/screenshots/signup.png" alt="Login area">
</details> 

3. I want to be able to choose difficulty levels

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Choose difficulty level | Select E for Easy or A for Advanced | Login Successful : Opens level | Works as expected

<details>
    <summary>Screenshots</summary>
    <p>Choose Level</p>
    <img src="assets/screenshots/easy_level.png" alt="Easy Level">   
    <p>Open rules is prompted after login is successful</p>
    <img src="assets/screenshots/adv_level.png" alt="Advanced Level">
</details> 


4. I want to be able to log-in if I return to the game

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Login To Play GuessGame | Username/ Password | Login Successful : Open rules | Works as expected

<details>
    <summary>Screenshots</summary>
    <p>Log In Area</p>
    <img src="assets/screenshots/restart_quest.png" alt="Login area">   
    <p>Open rules is prompted after login is successful</p>
    <img src="assets/screenshots/rules.png" alt="Open rules">
</details> 

5. I want to be able to read the rules of the game

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Open Rules  | : Open rules Starts Game | Works as expected

<details>
    <summary>Screenshots</summary>   
    <p>Open rules is prompted</p>
    <img src="assets/screenshots/rules.png" alt="Open rules">
    

6. I want to be able to restart game when I'm logged in

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Restart Game  | Type Y/N| Y: Game restarts/ N: Game ends, User logged out | Works as expected

<details>
    <summary>Screenshots</summary>   
    <p>Restart is prompted</p>
    <img src="assets/screenshots/restart.png" alt="Restart Question">
    <p>If user input is "Y"</p>
    <img src="assets/screenshots/restart.png" alt="Game restarts">
    
</details>

7. I want user name and password to be saved to Google Spreadsheet

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Sign-Up | Users input their name and password which has not been previously registered  | Username and password are saved to Google Spreadsheet| Works as expected |

<details>
    <summary>Screenshots</summary>
    <p>Google Spread Worksheet</p>
    <img src="assets/screenshots/spreadsheet.png" alt="Worksheet">      
</details> 

8. I want the user to get errors displayed in case of wrong input

 **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Across all screen | User inputs invalid input when questions are prompted. User inputs invalid value during log-in or sign-up | Feedback message displayed to the user | Works as expected |



9. I want data entry to be validated, to guide the user on how to correctly format the input

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Across all screen | User inputs invalid data | Feedback message with instructions diplayed to the user | Works as expected |



10. I want user to see their name once they login

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Welcome (Username) | After successful login | Users are asked to input their username and password, and once validated, a greeting message with their name is displayed. | Works as expected |

<details>
    <summary>Screenshots</summary>
    <img src="assets/screenshots/name_login.png" alt="Welcome message">
</details>

</details>

### Testing on Browsers
- I tested that this game works in different browsers - Chrome and Safari and was able to deploy successfully

### Tested Devices with Browsers
- iPhone 12
    - Safari
- Samsung S22 Ultra
    - Chrome
- Macbook Pro 2019 16-inch
    - Chrome
    - Safari
 
## Validator Testing
### [PEP8 Python Validator] was used to validate the code

- This validator was provided by Code institute
- - no significant errors were found
 
<details>
    <summary>authentication.py</summary>
    <img src="assets/screenshots/auth.png" alt="Authentication file screenshot">
</details> 


<details>
    <summary>game.py</summary>
    <img src="assets/screenshots/game.png" alt="Game file screenshot">
</details> 


<details>
    <summary>run.py</summary>
    <img src="assets/screenshots/run.png" alt="Run file screenshot">
</details> 

### Bugs and Fixes

| **Bugs** | **Fixes** |
| ------- | ------- |
| Users were able to sign up multiple times with same username | Add signup_check function which will prompt again if user exist or not|
| Users could sign up with blank username | Add validation to check if user did not input a name|
| regex error sometimes when the game starts | Included 'r' string which enabled backslash to escape some characters |


### Unfixed Bugs

- A function was created to update a different sheet of scores and players to create a leaderboard
- However an unexpected result was encounted when the game starts so this part had to be taken 
- out of the game.

## Deployment

### Deploying the website in Heroku:
- The website was deployed to Heroku using the following steps:
#### Login or create an account at Heroku
- Create a student account on Heroko and login

<details>
    <summary>Heroko Login Page</summary>
    <img src="assets/heroku/heroku_login.png" alt="Heroko login page">
</details>

#### Creating an app
  - Create new app in the top right of the screen and add an app name.
  - Select region
  - Then click "create app".

<details>
    <summary>Create App</summary>
    <img src="assets/heroku/heroku_app.png" alt="Heroko create app screenshot">
</details>

#### Open settings Tab
  ##### Click on config var
  - Store CREDS file from gitpod in key and add the values
  - Store PORT in key and value

<details>
    <summary>Config var</summary>
    <img src="assets/heroku/config_vars.png" alt="Config var screenshot">
</details>

  ##### Add Buildpacks
  - Add python buildpack first
  - Add Nodejs buildpack after that

<details>
    <summary>Buildpacks</summary>
    <img src="assets/heroku/build_pack.png" alt="Buildpacks screenshot">
</details>

 #### Open Deploy Tab
   ##### Choose deployment method
  - Connect GITHUB
  - Login if prompted

<details>
    <summary>Deployment method</summary>
    <img src="assets/heroku/deploy_method.png" alt="Deployment method screenshot">
</details>

   ##### Connect to Github
  - Choose repositories you want to connect
  - Click "Connect"

<details>
    <summary> Repo Connect</summary>
    <img src="assets/heroku/connect_github.png" alt="Repo connect screenshot">
</details>

  ##### Automatic and Manual deploy
  - Choose a method to deploy
  - After Deploy is clicked it will install various file

<details>
    <summary> Deploy methods</summary>
    <img src="assets/heroku/auto_deploy.png" alt="deploy method screenshot">
</details>

  ##### Final Deployment
  - A view button will display
  - Once clicked the website will open

<details>
    <summary> Deploy</summary>
    <img src="assets/heroku/final_view.png" alt="view screenshot">
</details>

## Credits

- The Idea was from Geeks for Geeks [Geeks for Geeks](https://www.geeksforgeeks.org/python-program-for-word-guessing-game/)
- Some of the code was borrowed from [hangman-pp3](https://github.com/Sinha5714/hangman-pp3)
- Also, regex for validating passwords was borrowed from [Tutorialspoint](https://www.tutorialspoint.com/password-validation-in-python)
### Content
- The idea of Guessing Game was taken from other word guessing games played around the world

### Code
#### The following ideas were borrowed from [Love Sandwiches](https://github.com/Sinha5714/Love_Sandwiches)
####

-  validate_user_details function
-  How to import gspread
-  How to import Credentials from google.oauth
- [W3 Schools](https://validator.w3.org/nu/)
- [Stack Overflow](https://validator.w3.org/nu/)
- [hangman-pp3](https://github.com/Sinha5714/hangman-pp3)


## Acknowledgement
- to my mentor Mo Shami for supporting me with his feedback through the entire project
- Special thanks to my friend Amoafo who is always ready to support me on the journey
- Also to my dear wife for beign there for me eventhough I have to abandon some family duties
