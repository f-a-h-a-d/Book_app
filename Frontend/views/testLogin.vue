<script setup>
import axios from "axios";
import { ref } from "vue";

import { useRouter } from 'vue-router';

const router = useRouter();

const userId = ref('');
const password = ref('');

const navigateToPageWithData = () => {
  router.push({ path: '/dashboard', query: { username: userId.value } });
};

const submitForm = async (e) => {
  const formData = {
    username: userId.value,
    password: password.value
  }

  axios({
    method: "post",
    url: "http://127.0.0.1:8000/api/login/",
    data: formData,
    headers: { "Content-Type": "multipart/form-data" },
  }).then((response) => {
    
      console.log(response);
      localStorage.setItem("Token", response.data.token)
      navigateToPageWithData();
      
    })
    .catch((error) => {
      // Handle error
      console.log(error);
    });

}

</script>

<template>
  <div class="login-wrapper">
    <h3>Login</h3>
    <p>Welcome Back to access your account</p>

    <form @submit.prevent="submitForm" action="">
      <div class="input-user mb-3">
        <div>
          <label for="name">User</label>
        </div>
        <div>
          <input v-model="userId" class="form-control" type="text" id="user" name="user" placeholder="User" />
        </div>
      </div>
      <div class="input-password mb-3">
        <div>
          <label for="password">Password</label>
        </div>
        <div>
          <input v-model="password" class="form-control input-password" type="password" id="password" name="password"
            placeholder="Password" />
        </div>
        <span class="password-toggle-icon"><i class="fas fa-eye"></i></span>
      </div>

      <!-- <br /> -->

      <div class="remember-forget">
        <div class="remember">
          <input type="checkbox" name="checkbox" id="remember" />
          <label for="remember">Remember me</label>
        </div>
        <div class="forget">
          <a href="#"> Forgot Password</a>
        </div>
      </div>

      <input type="submit" value="Sign in" class="submitForm" replace />

    </form>
  </div>
</template>


<style>
@import url('https://fonts.cdnfonts.com/css/avita');

* {
  box-sizing: border-box;
  font: avita;
}

.login-wrapper h3 {
  font-size: 48px;
  font-weight: 700;
}

body {
  padding: 0;
  margin: 0;
  background-color: #F5F6FA;

}

main {

  /* width:auto; */
  display: flex;
  justify-content: center;
  margin-top: 50px;
  /* margin-bottom: 50px;     */
}

.login-wrapper {
  background-color: #FFFFFF;
  width: 550px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 80px;


}

.remember-forget {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
  margin-bottom: 20px;
}

.sign-in input {
  background-color: #F04A00;
  color: white;
}

.input-password {
  position: relative;
}

.password-toggle-icon {
  position: absolute;
  right: 10px;
  top: 37px;
  cursor: pointer;
  /* top:68%;
    transform: translateY(-50%);
     */
}

.password-toggle-icon i {
  font-size: 18px;
  line-height: 1;
  color: #333;
  transition: color 0.3s ease-in-out;

}

.password-toggle-icon i:hover {
  color: #000;
}

.forget a {
  text-decoration: none;
  color: #002366;
}

.remember input {
  color: #555555;
}

label {
  color: #555555;
  margin-bottom: 4px;
  ;
}

img {
  padding: 0;
}

.captcha img {
  margin-bottom: 2px;
  width: 100%;
  height: 77px;
  border-radius: 8px;
}

.input-password input {
  padding-right: 35px;
}

.input-user input::placeholder {
  font-weight: 100;
  font-size: 12px;
}

.input-password input::placeholder {
  font-weight: 100;
  font-size: 12px;
}
</style>