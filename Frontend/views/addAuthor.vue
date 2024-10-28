<script>
import Layout from '../components/layouts/layout.vue'
import { onMounted } from "vue"

import 'jquery';

export default {
    components: {
        Layout
    },
    data(){
        return {
            authors: []
        }
    }

}

</script>

<script setup>
import axios from "axios";
import { ref } from "vue";

const AuthorId = ref('');
const AuthorName = ref('');
const AuthorAge = ref('');

const submitAuthor = async (e) => {
    const formData = {
        name: AuthorName.value,
        age: AuthorAge.value

    }
    console.log(formData);

    axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/author/add/",
        data: formData,
        headers: { "Content-Type": "multipart/form-data" },
    }).then((response) => {

        console.log(response);
        alert('Author added successfully!');

        AuthorAge.value = "",
            AuthorName.value = ""


    })
        .catch((error) => {
            // Handle error
            console.log(error);
        });
}

</script>

<template>
    <!-- General Form Elements -->

    <Layout>

        <div class="card-body">
            <h2 class="card-title">Add Author</h2>

            <!-- General Form Elements -->
            <form>

                <form @submit.prevent="submitAuthor" method="post">

                    <label for="title">Author Name:</label>
                    <input v-model="AuthorName" type="text" id="title" name="title">

                    <label for="quantity">Author Age</label>
                    <input v-model="AuthorAge" type="text" id="quantity" name="quantity">

                    <input type="submit" value="Submit">
                </form>

            </form><!-- End General Form Elements -->

        </div>


    </Layout>

</template>

<style>
.card-body {
    padding-top: 75px;
    padding-right: 0px;
}

form {
    margin: 10px;
    padding: 6px;
    border: 1px solid #ccc;
    border-radius: 5px;
    width: 300px;
}

label,
input {
    display: block;
    margin-bottom: 10px;
}

input[type="submit"] {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: lightblue;
}
</style>