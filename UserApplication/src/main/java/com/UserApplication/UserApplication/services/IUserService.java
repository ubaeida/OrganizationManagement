package com.UserApplication.UserApplication.services;

import com.UserApplication.UserApplication.models.User;

import java.util.List;
import java.util.Optional;

public interface IUserService {

    User saveUser(User user);

    List<User> getUsers();

    User searchUser(Long id);

    void deleteUser(Long id);

    User updateUser(Long id, User user);
}
