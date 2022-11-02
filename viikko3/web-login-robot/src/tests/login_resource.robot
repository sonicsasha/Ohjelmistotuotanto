*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py
Resource    resource.robot

*** Keywords ***

Login User
    [Arguments]     ${username}  ${password} 
    Go To Login Page
    Set Username    ${username}
    Set Password    ${password}
    Submit Login

Register User 
    [Arguments]     ${username}  ${password}  ${password_check}
    Go To Register Page
    Set Username    ${username}
    Set Password    ${password}
    Set Password Check    ${password_check}
    Submit Register


Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Check
    [Arguments]     ${password}
    Input Password    password_confirmation    ${password}

Submit Register
    Click Button    Register

Submit Login
    Click Button    Login