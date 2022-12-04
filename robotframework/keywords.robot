*** Settings ***
Library           Collections
Library           RequestsLibrary



*** Keywords ***
LOGIN AND GET TOKEN
        [Arguments]    ${username}    ${password}
        ${response}=        Post  http://localhost:9191/users/auth/login  params=username=${username}&password=${password}  expected_status=200
            [Return]            ${response.content}

CREATE HEADERS
        [Arguments]    ${username}    ${password}
        ${getToken}=    LOGIN AND GET TOKEN     ${username}    ${password}
        &{headrs}=       Create Dictionary
        Set To Dictionary   ${headrs}    Authorization    Bearer ${getToken}
        Set To Dictionary   ${headrs}    Content-type     Application/JSON

            [Return]            ${headrs}