*** Settings ***
Resource  resource.robot
Test Setup  Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials    test    testytest1
    Output Should Contain    New user registered

Register With Already Taken Username And Valid Password
    Input Credentials    test    testytest1
    Input Register Command
    Input Credentials    test    testytest1
    Output Should Contain    User with username test already exists

Register With Too Short Username And Valid Password
    Input Credentials    te    testytest1
    Output Should Contain    Username should be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials    test    123
    Output Should Contain    Password should be at least 8 characters long and can't contain only letters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials    test    testytester
    Output Should Contain    Password should be at least 8 characters long and can't contain only letters

