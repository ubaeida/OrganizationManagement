package com.UserApplication.UserApplication.services;

import com.UserApplication.UserApplication.models.Permissions;
import com.UserApplication.UserApplication.models.UserType;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.stereotype.Service;

import java.util.Arrays;
import java.util.stream.Collectors;

@Service
public class AuthService implements IAuthService {
    @Autowired
    Permissions permissions;

    @Override
    public boolean hasAuth(String receivedUserType, String questionedPermission) {
        var requestedAuths = Arrays.stream(questionedPermission.split(","))
                .map(SimpleGrantedAuthority::new)
                .collect(Collectors.toSet());
        var authList = permissions.get(UserType.valueOf(receivedUserType));
        return requestedAuths.stream().anyMatch(authList::contains);
    }
}
