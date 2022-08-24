package com.UserApplication.UserApplication.services;

import com.UserApplication.UserApplication.models.User;
import com.UserApplication.UserApplication.persistance.UserRepository;
import org.springframework.stereotype.Service;

import java.util.Optional;
@Service
public class ProfileService implements IProfileService{
    final UserRepository userRepository;

    public ProfileService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Override
    public Optional<User> getUserById(Long id) {
        return userRepository.findById(id);
    }

    @Override
    public User updateUser(Long id, User user) {
        Optional<User> userOptional = userRepository.findById(id);
        User dbUser = userOptional.orElseThrow();
        user.setId(dbUser.getId());
        return userRepository.save(user);
    }
}