package com.UserApplication.UserApplication.models;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Component
@Slf4j
public class Permissions {

    @Autowired
    ObjectMapper objectMapper;
    Map<UserType, List<? extends GrantedAuthority>> map = new HashMap<>();

    @PostConstruct
    public void init() {

        try {
            Map<String, List<String>> toMap = objectMapper.readValue(permissions, Map.class);
            for (String key : toMap.keySet()) {
                var userType = UserType.valueOf(key);
                List<SimpleGrantedAuthority> given;
                if (toMap.get(key).size() == 1 && toMap.get(key).get(0).equals("*")) {

                    given = Arrays.stream(AuthoritiesEnum.values()).map(Enum::name).map(SimpleGrantedAuthority::new).toList();
                } else {
                    given = toMap.get(key).stream().map(SimpleGrantedAuthority::new).toList();
                }
                map.put(userType, given);
            }
        } catch (JsonProcessingException e) {
            log.info("exception parsing", e);
        }
    }

    public List<? extends GrantedAuthority> get(UserType userType) {
        return map.get(userType);
    }

    final String permissions = """
                {
                    "ADMINISTRATOR": ["*"],
                    "HEAD_OFFICE":["VIEW_PROFILE", "VIEW_USERS", "VIEW_CASES"],
                    "HR": ["VIEW_PROFILE", "VIEW_USERS", "EDIT_USER", "CREATE_USER", "DELETE_USER"],
                    "CASE_MANAGEMENT_OFFICER":["VIEW_PROFILE" ,"VIEW_CASES", "CREATE_CASE", "EDIT_CASE", "DELETE_CASE", "ASSIGN_CASE", "ACCEPT_CASE", "view_approved_candidates", "APPROVE_ASSESSMENT"],
                    "CASEWORKER":["VIEW_PROFILE", "VIEW_CASES", "CREATE_CASE", "EDIT_CASE", "DELETE_CASE"],
                    "OUTREACH_OFFICER":["VIEW_PROFILE" ,"VIEW_ASSESSMENT", "CREATE_ASSESSMENT", "EDIT_ASSESSMENT", "DELETE_ASSESSMENT", "APPROVE_ASSESSMENT"],
                    "HOTLINE_ASSISTANT":["VIEW_PROFILE", "VIEW_ASSESSMENT", "CREATE_ASSESSMENT", "EDIT_ASSESSMENT", "DELETE_ASSESSMENT"],
                    "OUTREACH_ASSISTANT":["VIEW_PROFILE", "VIEW_ASSESSMENT", "CREATE_ASSESSMENT", "EDIT_ASSESSMENT", "DELETE_ASSESSMENT"]
                }
            """;

    public enum AuthoritiesEnum {
        VIEW_USERS, EDIT_USER, CREATE_USER, DELETE_USER,
        VIEW_CASES, CREATE_CASE, EDIT_CASE, ASSIGN_CASE, DELETE_CASE,
        VIEW_PROFILE,
        VIEW_ASSESSMENT, CREATE_ASSESSMENT, EDIT_ASSESSMENT, DELETE_ASSESSMENT, REFER_ASSESSMENT
    }
}