*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  aapeli  aapeli123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  salasana123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ex  salasana123
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  aapeli  aapeli1
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  aapeli  aapelionepeli
    Output Should Contain  Password cannot contain only letters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123