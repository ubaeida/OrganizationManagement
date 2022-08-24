package com.UserApplication.UserApplication.security;

import io.jsonwebtoken.JwtException;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Component;

import java.util.Date;
import java.util.Map;

@Component
public class TokenUtil {
    private static final String CLAIMS_SUBJECT = "sub";
    private static final String CLAIMS_CREATED = "created";

    @Value("${jwt.secret}")
    String jwtSignSecret;

    public String generateToken(UserDetails userDetails) {
        Map<String, Object> claims = Map.of(CLAIMS_SUBJECT, userDetails.getUsername(), CLAIMS_CREATED, new Date());

        return Jwts.builder()
                .setClaims(claims)
                .signWith(SignatureAlgorithm.HS256, jwtSignSecret)
                .compact();
    }

    public boolean validate(String jwt) {
        try {
            Jwts.parser().setSigningKey(jwtSignSecret).parseClaimsJws(jwt).getBody().getSubject();
            return true;
        } catch (JwtException jwtException) {
            throw jwtException;
        }
    }

    public String extractUsername(String jwt) {
        var headerClaimsJwt = Jwts.parser().setSigningKey(jwtSignSecret).parseClaimsJws(jwt);
        return headerClaimsJwt.getBody().getSubject();
    }
}
