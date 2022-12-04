*** Settings ***
Library           RequestsLibrary
Resource          keywords.robot


*** Variables ***
${body}=           username=outreach_assistant     name=outreach_assistant     email=test@test.com     gender=male     type=outreach_assistant     password=test


*** test cases ***
Add new user
    ${headers}=         CREATE HEADERS          admin       test
    &{body}=            Create Dictionary              username=outreach_assistant     name=outreach_assistant     email=test@test.com     gender=male     type=outreach_assistant     password=test
    ${resp}=      POST  http://localhost:9191/users      headers=${headers}       json=${body}
                        Log    'this response'  ${resp.content}
