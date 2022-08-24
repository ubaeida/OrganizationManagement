package com.UserApplication.UserApplication.models;

public enum UserType {
    CASE_MANAGEMENT_OFFICER("CASE_MANAGEMENT_OFFICER"),
    OUTREACH_OFFICER("OUTREACH_OFFICER"),
    HEAD_OFFICE("HEAD_OFFICE"),
    CASEWORKER("CASEWORKER"),
    HOTLINE_ASSISTANT("HOTLINE_ASSISTANT"),
    OUTREACH_ASSISTANT("OUTREACH_ASSISTANT"),
    ADMINISTRATOR("ADMINISTRATOR"),
    HR("HR")
    ;

    String UserType;

    UserType(String UserType) {
        this.UserType = UserType;
    }

    @Override
    public String toString() {
        return "UserType{"+ "UserType"+ UserType +'\'' + '}';
    }
}
