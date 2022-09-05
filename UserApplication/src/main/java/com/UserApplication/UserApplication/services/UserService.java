package com.UserApplication.UserApplication.services;

import com.UserApplication.UserApplication.models.User;
import com.UserApplication.UserApplication.persistance.UserRepository;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Optional;


@Service
public class UserService implements IUserService, UserDetailsService {

    final UserRepository userRepository;
    final PasswordEncoder passwordEncoder;

    public UserService(UserRepository userRepository, PasswordEncoder passwordEncoder) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
    }


    @Override
    public User saveUser(User user) {
        user.setPassword(passwordEncoder.encode(user.getPassword()));
        return userRepository.save(user);
    }

    @Override
    public List<User> getUsers() {
        Iterable<User> users = userRepository.findAll();
        List<User> listOfUsers = new ArrayList<>();
        for (User user : users) {
            listOfUsers.add(user);
        }
        return listOfUsers;
    }

    @Override
//    Return if null need to be better
    public User searchUser(Long id) {
        Optional<User> optionalUser = userRepository.findById(id);
        if (optionalUser.isPresent()) {
            User user = optionalUser.get();
            return user;
        } else {
            return null;
        }
    }

    @Override
    public void deleteUser(Long id) {
        if (userRepository.existsById(id)) {
            userRepository.deleteById(id);
        }
    }

    @Override
    public User updateUser(Long id, User user) {
        Optional<User> userOptional = userRepository.findById(id);
        User dbUser = userOptional.orElseThrow();
        user.setId(dbUser.getId());
        return userRepository.save(user);
    }

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        var userDetails = userRepository.findByUsername(username).orElseThrow();
        userDetails.getAuthorities();
        return userDetails;
    }
}