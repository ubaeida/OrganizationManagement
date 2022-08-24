package com.UserApplication.UserApplication.services;

import com.UserApplication.UserApplication.models.User;

import java.util.Optional;

public interface IProfileService {

    Optional<User> getUserById(Long id);

    User updateUser(Long id, User user);
}
