*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Start And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  aapeli
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  e
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Registration
    Registation Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  erkki
    Set Password  e123
    Set Password Confirmation  e123
    Submit Registration
    Registation Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  erkki
    Set Password  salasana123
    Set Password Confirmation  salasana12
    Submit Registration
    Registation Should Fail With Message  Passwords do not match

*** Keywords ***
Start And Go To Register Page
    Go To Register Page
    Register Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Registration
    Click Button  Register

Registration Should Succeed
    Welcome Page Should Be Open

Registation Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}