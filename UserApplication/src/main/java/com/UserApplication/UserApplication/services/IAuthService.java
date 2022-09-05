package com.UserApplication.UserApplication.services;

import org.springframework.security.core.authority.SimpleGrantedAuthority;

public interface IAuthService {
    boolean hasAuth(String receivedUserType, SimpleGrantedAuthority questionedPermission);
}
