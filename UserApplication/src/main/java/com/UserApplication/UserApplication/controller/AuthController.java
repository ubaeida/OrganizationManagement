package com.UserApplication.UserApplication.controller;

import com.UserApplication.UserApplication.security.TokenUtil;
import com.UserApplication.UserApplication.services.AuthService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/users/auth")
public class AuthController {

    @Autowired
    AuthService authService;

    public AuthController(AuthService authService) {
        this.authService = authService;
    }

    @Autowired
    AuthenticationManager authenticationManager;

    @Autowired
    TokenUtil tokenUtil;

    @PostMapping("/login")
    public String login(String username, String password) {
        System.out.printf("%s", username);
        System.out.printf("%s", password);
        var authentication = new UsernamePasswordAuthenticationToken(username, password);
        var user = authenticationManager.authenticate(authentication);
        return tokenUtil.generateToken((UserDetails) user.getPrincipal());
    }

    @GetMapping("/hasAuthority")
    public boolean hasAuthority(@RequestParam String receivedUserType, @RequestParam String questionedPermission) {
        return authService.hasAuth(receivedUserType, questionedPermission);
    }
}
