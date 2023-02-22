package com.gpt.servicegpt.service;

import com.gpt.servicegpt.model.User;
import com.gpt.servicegpt.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

@Service
public class UserService {

    @Autowired
    UserRepository userRepository;

    @Autowired
    BCryptPasswordEncoder encoder;

    public void 회원가입(User user){

    }
}
