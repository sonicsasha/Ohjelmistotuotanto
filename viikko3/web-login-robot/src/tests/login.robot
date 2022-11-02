*** Settings ***
Resource  resource.robot
Resource     login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page
Test Teardown  Reset Application

*** Test Cases ***
Login With Correct Credentials
    Login User    kalle    kalle123
    Login Should Succeed

Login With Incorrect Password
    Login User    kalle    kalle456
    Login Should Fail With Message  Invalid username or password

Login With Nonexistent Username
    Login User    test    kalle123
    Login Should Fail With Message    Invalid username or password
*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login



Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open
