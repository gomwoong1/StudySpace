package com.gpt.servicegpt.service;

import com.gpt.servicegpt.model.RoleType;
import com.gpt.servicegpt.model.User;
import com.gpt.servicegpt.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class UserService {

    @Autowired
    UserRepository userRepository;

    @Autowired
    BCryptPasswordEncoder encoder;

    @Transactional
    public void 회원가입(User user){
        String rowPWD = user.getPassword();
        String encPWD = encoder.encode(rowPWD);

        user.setRole(RoleType.USER);
        user.setPassword(encPWD);

        userRepository.save(user);
    }
}
