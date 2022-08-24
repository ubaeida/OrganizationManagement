package com.UserApplication.UserApplication;

import com.UserApplication.UserApplication.models.Gender;
import com.UserApplication.UserApplication.models.User;
import com.UserApplication.UserApplication.models.UserType;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.print;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@AutoConfigureMockMvc
public class UsersTest {

    @Autowired
    private MockMvc mockMvc;
    ObjectMapper mapper = new ObjectMapper();

    @Test
    public void test_Create() throws Exception {
        User user = new User();
        user.setEmail("mail@mail.com");
        user.setGender(Gender.MALE);
        user.setName("Ahmad");
        user.setUsername("ali");
        user.setType(UserType.CASE_MANAGEMENT_OFFICER);
        mockMvc.perform(post("/users")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(mapper.writeValueAsString(user)))
                .andDo(print()).andExpect(status().isOk());
    }

}
