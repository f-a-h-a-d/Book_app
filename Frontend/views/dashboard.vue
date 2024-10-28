<script>

import Layout from '../components/layouts/layout.vue'
import { useRouter } from 'vue-router';
import {ref} from 'vue';

const router = useRouter();
const name = ref('');

export default {
  components: {
    Layout
  },

}

</script>

<template>
  
  <Layout>
      <h2>Welcome To Dashboard {{ $route.query.username}}</h2>
      
  </Layout>

</template>

<style>
@import url(https://befonts.com/avita-font.html);


@font-face {
  font-family: "Avita";
  src: url("./Avita-Typeface/Avita-Regular.otf");
  font-weight: normal;

}

body * {
  padding: 0;
  margin: 0;

}

aside {
  position: sticky;

  background-color: white;
  border: 1px solid #E5E7EB;
  font-family: "Avita";
}

.sidebar-inner-wrap {
  height: 100vh;
}

aside nav ul li:hover,
aside nav ul li.selected {
  background-color: #002366
}

aside nav ul li a svg path {
  stroke: black;
}

aside nav ul li a {
  color: black;
}

aside nav ul li:hover a {
  color: #ffffff
}

aside nav ul li:hover a svg path {
  stroke: #ddd;
}

main {
  width: 100%;
}

h1 {
  display: inline;
}

.icon {

  background-color: white;
  border: none;
  position: absolute;
  right: -15px;
  top: 13px;
}

.nav-main {
  /* height: 896px; */
  padding-top: 8px;
  padding-left: 16px;
}

ul {
  list-style-type: none;
  padding: 0px !important;

}

li {
  border-radius: 8px;
  padding-top: 12px;
  padding-bottom: 12px;

}

li a,
.settings a {
  color: black;
  text-decoration: none;
}

.settings {
  bottom: 10px;
  position: absolute;
}

li a,
h1,
.settings {
  padding-left: 16px;
}

li a img,
.settings a img {
  padding-right: 8px;
}


main {
  padding-left: 0 !important;
  margin-left: 0 !important;
  display: flex;
  flex-direction: column;
}

main .top {
  background-color: white;

}

main .top span {
  float: right;
  padding: 16px;
}

.dropdown-toggle {
  background-color: white;
  border: none;
  position: relative;
}

.user-dropdown {
  background-color: #fff;
  border-radius: 10px;
  padding: 15px 0;
  box-shadow: 0px 3px 5px 1px #ddd;
  width: 200px;
  position: absolute;
  top: 100%;
  right: 0;
  text-align: left;
  display: none;
}

.dropdown-toggle:hover .user-dropdown {
  display: block;
}

.user-dropdown ul li a,
.user-dropdown h3 {
  font-size: 14px;
  font-weight: normal;
}

.user-dropdown ul li,
.user-dropdown h3 {
  padding: 5px 15px;
}

.user-dropdown ul li:hover {
  background-color: #ddd;
  border-radius: 0;
}

.user-dropdown .user-info-links {
  padding-bottom: 15px !important;
  border-bottom: 1px solid #ddd;
}

.settings-icon {
  margin-bottom: 0;
}

main {
  background-color: #F5F6FA;
}

.right-side-content-area {
  margin: 20px;
  padding: 15px;
  background-color: white;
  border-radius: 24px;
  font-family: 'Figtree';
}

input {
  font-family: FontAwesome;
}

::placeholder {
  /* color: #F04A00; */
  font-family: FontAwesome;
}

.table-top {
  padding: 10px;
  display: flex;
  justify-content: space-between;
}

.table-top h3 {
  padding: 12px 24px 12px 0px;
}

.table-top input {
  padding: 12px 24px 12px 24px;
  border: 1px solid;
  border-color: #E5E7EB;
  border-radius: 8px;
}

.table-top button {
  padding: 12px 24px 12px 24px;
  background-color: #F04A00;
  color: white;
  border: 0px;
  border-radius: 8px;
}

.table-bottom {
  display: flex;
  justify-content: space-between;
}

.table-bottom-right-side {
  padding-top: 10px;
  padding-bottom: 10px;
}

.pagination>li>a {
  color: black;
}

.pagination .previous::before {
  padding-right: 8px;
  content: '<';
  color: #F04A00;
}

.pagination .next::after {
  padding-left: 8px;
  content: '>';
  color: #F04A00;
}

.pagination .next {
  color: #F04A00;
}

.pagination .active a {
  background-color: #F04A00;
  border: none;
}
</style>../components/layouts/sidebars/sideBar.vue