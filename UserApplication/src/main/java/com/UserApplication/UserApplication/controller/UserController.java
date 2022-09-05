package com.UserApplication.UserApplication.controller;

import com.UserApplication.UserApplication.models.User;
import com.UserApplication.UserApplication.services.UserService;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.Optional;

@RestController
@RequestMapping("/users")
public class UserController {
    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @PostMapping
    public User addNewUser(@RequestBody @Valid User user) {
        return userService.saveUser(user);
    }

    @GetMapping
    Iterable<User> getAllUsers() {
        return userService.getUsers();
    }

    @GetMapping("{id}")
    User getUser(@PathVariable Long id) {
        return userService.searchUser(id);
    }

    @DeleteMapping("{id}")
    public void deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
    }

    @PutMapping("{id}")
    public User updateUser(@PathVariable Long id, @RequestBody @Valid User user) {
        return userService.updateUser(id, user);
    }
}