package com.gpt.servicegpt.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.method.configuration.EnableGlobalMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@EnableWebSecurity
@EnableGlobalMethodSecurity(prePostEnabled = true)
public class SecurityConfig {

    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {

        http
                .csrf().disable()
                .authorizeRequests()
                .antMatchers("/", "/auth/**", "/images/**", "/js/**", "/css/**")
                .permitAll()
                .anyRequest()
                .authenticated()
        .and()
                .formLogin()
                .loginPage("/auth/login")
                .loginProcessingUrl("/auth/ProcLogin")
                .defaultSuccessUrl("/");

        return http.build();
    }
}
