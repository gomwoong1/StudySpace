package com.remake.friends.config.auth;

import com.remake.friends.model.User;
import com.remake.friends.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

@Service
public class UserDetailService implements UserDetailsService {

    @Autowired
    UserRepository userRepository;

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        User principal = userRepository.findByUsername(username)
                .orElseThrow( ()-> {
                    return new UsernameNotFoundException("해당 사용자를 찾을 수 없습니다: "+username);
                });

        return new UserDetail(principal);
    }
}
