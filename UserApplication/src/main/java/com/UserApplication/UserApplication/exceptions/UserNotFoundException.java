package com.UserApplication.UserApplication.exceptions;

public class UserNotFoundException extends RuntimeException{
    public final String username;
    public UserNotFoundException(String username) {
        this.username = username;
    }

}
