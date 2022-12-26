*** Settings ***
Library           RequestsLibrary
Resource          keywords.robot

*** Variables ***
${candidate_id}
${action}

*** test cases ***
Add new candidate
    ${user}=            CREATE USER             username=outreach_assistant     name=outreach_assistant     email=test@test.com     gender=MALE     type=OUTREACH_ASSISTANT     password=test
    ${headers}=         CREATE HEADERS          outreach_assistant    test
    &{body}=            Create Dictionary               fullname=First_candidate    gender=FEMALE   status=nominated
    ${response}=            POST    http://localhost:9191/tickets/candidates        headers=${headers}      json=${body}        expected_status=200
    ${candidate_id}=       Set Variable         ${response.json()}[id]
    Set Global Variable     ${candidate_id}
                            Log To Console    ${candidate_id}
update candidate
    ${headers}=         CREATE HEADERS          outreach_assistant    test
    &{body}=            Create Dictionary               fullname=First_candidate    gender=MALE   status=nominated
    ${response}=            PUT    http://localhost:9191/tickets/candidates/${candidate_id}        headers=${headers}      json=${body}        expected_status=200

Approve candidate_by_outreach_officer
    ${user}=            CREATE USER             username=outreach_officer     name=outreach_officer     email=test@test.com     gender=FEMALE     type=OUTREACH_OFFICER     password=test
    ${headers}=         CREATE HEADERS          outreach_officer       test
    ${body}=            Create Dictionary       status=approved
    ${response}=        PATCH   http://localhost:9191/tickets/candidates/${candidate_id}        headers=${headers}  json=${body}    expected_status=200
                        Log To Console    ${response.content}

accept candidate_by_outreach_officer
    ${user}=            CREATE USER             username=CASE_MANAGEMENT_OFFICER     name=CASE_MANAGEMENT_OFFICER     email=test@test.com     gender=MALE     type=CASE_MANAGEMENT_OFFICER     password=test
    ${headers}=         CREATE HEADERS          CASE_MANAGEMENT_OFFICER       test
    ${body}=            Create Dictionary       status=accepted
    ${response}=        PATCH   http://localhost:9191/tickets/candidates/${candidate_id}        headers=${headers}  json=${body}    expected_status=200
                        Log To Console    ${response.content}