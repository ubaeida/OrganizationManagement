*** Settings ***
Library           RequestsLibrary
Resource          keywords.robot


*** Variables ***
${candidate_id}



*** test cases ***
Add outreach_assistant
    ${headers}=         CREATE HEADERS          admin       test
    &{body}=            Create Dictionary              username=outreach_assistant     name=outreach_assistant     email=test@test.com     gender=MALE     type=OUTREACH_ASSISTANT     password=test
    ${resp}=            POST    http://localhost:9191/users      headers=${headers}       json=${body}      expected_status=200
#

Add new candidate
    ${headers}=         CREATE HEADERS          outreach_assistant    test
    &{body}=            Create Dictionary               fullname=First_candidate    gender=FEMALE   status=nominated
    ${response}=            POST    http://localhost:9191/tickets/candidates        headers=${headers}      json=${body}        expected_status=200
    ${candidate_id}=       Set Variable         ${response.json()}[id]
    Set Global Variable     ${candidate_id}
                            Log To Console    ${candidate_id}

Add outreach_officer
    ${headers}=         CREATE HEADERS          admin       test
    &{body}=            Create Dictionary              username=outreach_officer     name=outreach_officer     email=test@test.com     gender=FEMALE     type=OUTREACH_OFFICER     password=test
    ${resp}=            POST    http://localhost:9191/users      headers=${headers}       json=${body}      expected_status=200

Approve candidate_by_outreach_officer
    ${headers}=         CREATE HEADERS          outreach_officer       test
    ${body}=            Create Dictionary       status=approved
    ${response}=        PATCH   http://localhost:9191/tickets/candidates/${candidate_id}        headers=${headers}  json=${body}    expected_status=200
                        Log To Console    ${response.content}
