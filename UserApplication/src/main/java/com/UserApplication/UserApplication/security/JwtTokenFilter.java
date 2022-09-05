package com.UserApplication.UserApplication.security;

import com.UserApplication.UserApplication.models.Permissions;
import com.UserApplication.UserApplication.models.User;
import com.UserApplication.UserApplication.services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpHeaders;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@Component
public class JwtTokenFilter extends OncePerRequestFilter {
    @Autowired
    TokenUtil tokenUtil;
    @Autowired
    UserService userService;
    @Autowired
    Permissions permissions;


    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
        var authHeader = request.getHeader(HttpHeaders.AUTHORIZATION);
        if (authHeader != null && authHeader.startsWith("Bearer ")) {
            var jwt = authHeader.replace("Bearer ", "");
            tokenUtil.validate(jwt);
            var username = tokenUtil.extractUsername(jwt);
            UserDetails userDetails = userService.loadUserByUsername(username);
            User asUser = (User) userDetails;
            var authentication = new UsernamePasswordAuthenticationToken(userDetails, null,
                    permissions.get(asUser.getType()));
            SecurityContextHolder.getContext().setAuthentication(authentication);
        }
        filterChain.doFilter(request, response);
    }
}