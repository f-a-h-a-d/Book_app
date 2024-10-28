<script setup>

import { useRouter } from 'vue-router';

const router = useRouter();

const moveToDash = () => {
    console.log('Check')
    router.push('/dashboard');
};

const moveToforms = () => {
    router.push('/form')
}
const moveToShowBooks = () => {
    router.push('/showbooks')
}
const moveToaddBook = ()=>{
    router.push('/addBook')
}
const moveToaddAuthor = ()=>{
    router.push('/addAuthor')
}

</script>

<template>
    <!-- ======= Sidebar ======= -->
    <aside id="sidebar" class="sidebar">

        <ul class="sidebar-nav" id="sidebar-nav">

            <li class="nav-item">
                <a @click="moveToDash" class="nav-link ">
                    <i class="bi bi-grid"></i>
                    <span>Dashboard</span>
                </a>
            </li><!-- End Dashboard Nav -->

            <li>
                <div class="dropdown">
                    <button class="dropdown-button">Dropdown</button>
                    <div class="dropdown-content">
                        <a @click="moveToaddBook" href="#">Add Book</a>
                        <a @click="moveToaddAuthor" href="#">Add Author</a>
                    </div>
                </div>
            </li>


            <li class="nav-item">
                <a @click="moveToShowBooks" class="nav-link collapsed" data-bs-target="#tables-nav"
                    data-bs-toggle="collapse" href="#">
                    <i class="bi bi-layout-text-window-reverse"></i><span>Show Book</span><i
                        class="bi bi-chevron-down ms-auto"></i>
                </a>

            </li><!-- End Tables Nav -->

        </ul>

    </aside><!-- End Sidebar-->
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
    background-color:white;
    color:blue;
    padding: 16px;
    font-size: 16px;
    border: none;
    cursor: pointer;
}

.dropdown-button:hover {
    background-color: #3e8e41;
}
</style>
