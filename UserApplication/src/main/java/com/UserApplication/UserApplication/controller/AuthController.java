package com.UserApplication.UserApplication.controller;

import com.UserApplication.UserApplication.security.TokenUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/auth")
public class AuthController {

    @Autowired
    AuthenticationManager authenticationManager;

    @Autowired
    TokenUtil tokenUtil;

    @PostMapping("/login")
    public String login(String username, String password) {
        var authentication = new UsernamePasswordAuthenticationToken(username, password);
        var user = authenticationManager.authenticate(authentication);
        return tokenUtil.generateToken((UserDetails) user.getPrincipal());
    }
}
