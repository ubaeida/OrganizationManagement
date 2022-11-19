*** Settings ***
Library     RequestsLibrary


*** Variables ***
${username}     firas
${password}     test


*** test cases ***
Login User
    ${response}=        Post  http://localhost:9191/users/auth/login  params=username=${username}&password=${password}  expected_status=200
