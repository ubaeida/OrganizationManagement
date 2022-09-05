package com.UserApplication.UserApplication.services;

import com.UserApplication.UserApplication.models.Permissions;
import com.UserApplication.UserApplication.models.UserType;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.stereotype.Service;

@Service
public class AuthService implements IAuthService {
    @Autowired
    Permissions permissions;

    @Override
    public boolean hasAuth(String receivedUserType, SimpleGrantedAuthority questionedPermission) {
        var authList = permissions.get(UserType.valueOf(receivedUserType));
        return authList.contains(questionedPermission);
    }
}
