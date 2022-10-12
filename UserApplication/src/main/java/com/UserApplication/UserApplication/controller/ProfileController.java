package com.UserApplication.UserApplication.controller;

import com.UserApplication.UserApplication.models.User;
import com.UserApplication.UserApplication.services.ProfileService;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;

@RestController
@RequestMapping("/users/profile")
public class ProfileController {
    final ProfileService profileService;

    public ProfileController(ProfileService profileService) {
        this.profileService = profileService;
    }

    @GetMapping
    public User getById() {
        var user = (User) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
        return user;

    }

    @PutMapping()
    public User updateUser(@RequestBody @Valid User updatedUser) {
        var user = (User) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
        Long id = user.getId();
        return profileService.updateUser(id, updatedUser);
    }
}