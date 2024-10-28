<script setup>
import axios from "axios";
const name = 'Header';

import { useRouter } from 'vue-router';

const router = useRouter();

const userToken = localStorage.getItem("Token");

function loggingOut() {
    axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/logout/",
        data: { },
        headers: { "Content-Type": "multipart/form-data", "Authorization": `Token ${userToken}` },
    }).then((response) => {
        console.log(response);
        localStorage.removeItem('Token');
        router.push({ path: '/login' });

    })
        .catch((error) => {

            console.log(error);
        });
};


</script>


<template>
    <header id="header" class="header fixed-top d-flex align-items-center">

        <div class="d-flex align-items-center justify-content-between">
            <a href="index.html" class="logo d-flex align-items-center">
                <img src="../../../assets/img/apple-touch-icon.png" alt="">
                <span class="d-none d-lg-block">NiceAdmin</span>
            </a>
            <i class="bi bi-list toggle-sidebar-btn"></i>
        </div><!-- End Logo -->

        <div class="search-bar">
            <form class="search-form d-flex align-items-center" method="POST" action="#">
                <input type="text" name="query" placeholder="Search" title="Enter search keyword">
                <button type="submit" title="Search"><i class="bi bi-search"></i></button>
            </form>
        </div><!-- End Search Bar -->

        <nav class="header-nav ms-auto">
            <ul class="d-flex align-items-center">

                <li class="nav-item d-block d-lg-none">
                    <a class="nav-link nav-icon search-bar-toggle " href="#">
                        <i class="bi bi-search"></i>
                    </a>
                </li><!-- End Search Icon-->

            </ul>


        </nav><!-- End Icons Navigation -->
        <div class="dropdown">
            <button class="dropdown-button">Dropdown</button>
            <div class="dropdown-content">
                <a @click="loggingOut()" href="#">Log Out</a>
            </div>
        </div>

    </header><!-- End Header -->

</template>


<style>
.dropdown {
    position: relative;
    display: inline-block;
}

.dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 160px;
    box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
    z-index: 1;
}

.dropdown-content a {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
}

.dropdown-content a:hover {
    background-color: #f1f1f1;
}

.dropdown:hover .dropdown-content {
    display: block;
}

/* Optional: Style the dropdown button */
.dropdown-button {
    background-color: lightseagreen;
    color: white;
    padding: 16px;
    font-size: 16px;
    border: none;
    cursor: pointer;
}

.dropdown-button:hover {
    background-color: #3e8e41;
}
</style>