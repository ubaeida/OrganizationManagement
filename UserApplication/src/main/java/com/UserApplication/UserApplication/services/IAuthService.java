package com.UserApplication.UserApplication.services;

public interface IAuthService {
    boolean hasAuth(String receivedUserType, String questionedPermission);
}
