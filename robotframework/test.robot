*** Settings ***
Library           RequestsLibrary
Resource          keywords.robot


*** Variables ***


*** test cases ***
Add outreach_assistant
    ${headers}=         CREATE HEADERS          admin       test
    &{body}=            Create Dictionary              username=outreach_assistant     name=outreach_assistant     email=test@test.com     gender=MALE     type=OUTREACH_ASSISTANT     password=test
    ${resp}=            POST    http://localhost:9191/users      headers=${headers}       json=${body}      expected_status=200
                        Log To Console   'this response'  ${resp.content}


Add new candidate
    ${headers}=         CREATE HEADERS          outreach_assistant    test
    &{body}=            Create Dictionary               fullname=First_candidate    gender=FEMALE   nominator_id=22    status=test status    updater_id=22
                                                                                                    # ID should be taken automatekley from the JWT (updater_id, nominator_id)
    @{response}=            POST    http://localhost:9191/tickets/candidates        headers=${headers}      json=${body}        expected_status=200


