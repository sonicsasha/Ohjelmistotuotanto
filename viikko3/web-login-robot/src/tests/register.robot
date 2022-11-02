*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup    Go To Register Page
Test Teardown    Reset Application

*** Test Cases ***
Register With Valid Username And Password
    Register User    test    testytest1    testytest1
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Register User    te    testytest1    testytest1
    Register Should Fail With Error    Username should be at least 3 characters long and only include letters

Register With Valid Username And Too Short Password
    Register User    test    testy   testy
    Register Should Fail With Error    Password should be at least 8 characters long and include something besides letters

Register With Nonmatching Password And Password Confirmation
    Register User    test    testytest1    testytest23
    Register Should Fail With Error      Password inputs do not match

Login After Successful Registration
    Register User    test    testytest1    testytest1
    Welcome Page Should Be Open
    Login User    test    testytest1
    Main Page Should Be Open


Login After Failed Registration
    Register User    tester    testytest1    testytest23
    Register Page Should Be Open
    Login User    tester    testytest1
    Login Page Should Be Open

*** Keywords ***

Register Should Fail With Error
    [Arguments]    ${error}
    Register Page Should Be Open
    Page Should Contain    ${error}