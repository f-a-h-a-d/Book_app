<script>
import Layout from '../components/layouts/layout.vue'
import { onMounted } from "vue"

import 'jquery';

export default {
    components: {
        Layout
    },
    data() {
        return {
            authors: []
        }
    }

}

</script>

<script setup>
import axios from "axios";
import { ref } from "vue";
import { onMounted } from "vue"

const allAuthors = ref();

$(document).ready(function () {
    $('.authorsSelect').select2();
});

onMounted(() => {
    try {
        const response = axios.get("http://127.0.0.1:8000/api/author/list/").then((response) => {


            allAuthors.value = response.data;
            console.log(allAuthors.value);

        });


    } catch (error) {
        console.error(error);
    }
})


const bookId = ref('');
const bookTitle = ref('');
const bookQuantity = ref('');
const bookDate = ref('');
const bookGenre = ref('');
const bookAuthorId = ref('');
const bookAuthorName = ref('');

const AuthorId = ref('');
const AuthorName = ref('');
const AuthorAge = ref('');


const submitBook = async (e) => {

    var originalDate = bookDate.value;

    var formattedDate = '';
    var year = '';
    var month = '';
    var day = '';



    for (var i = 0; i < originalDate.length; i++) {

        if (originalDate[i] === '-') {
            if (year === '') {

                year = formattedDate;
                formattedDate = '';
            } else if (month === '') {

                month = formattedDate;
                formattedDate = '';
            }
        } else {

            formattedDate += originalDate[i];
        }
    }


    day = formattedDate;


    formattedDate = year + '-' + month + '-' + day;
    console.log(authors);
    const formData = {
        book_id: bookId.value,
        title: bookTitle.value,
        quantity: parseInt(bookQuantity.value),
        published_date: formattedDate,
        genre: bookGenre.value,
        author_id: parseInt(bookAuthorId.value),
        author_names: authors

    }
    console.log(formData);

    axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/books/add/",
        data: formData,
        headers: { "Content-Type": "multipart/form-data" },
    }).then((response) => {

        console.log(response);
        alert('Book added successfully!');

        bookId = ref('');
        bookTitle = ref('');
        bookQuantity = ref('');
        bookDate = ref('');
        bookGenre = ref('');
        bookAuthorId = ref('');


    })
        .catch((error) => {
            // Handle error
            console.log(error);
        });
}


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
            <h2 class="card-title">Add Books</h2>

            <!-- General Form Elements -->
            <form>

                <form @submit.prevent="submitBook" method="post">
                    <label for="id">BooK ID:</label>
                    <input v-model="bookId" type="text" id="id" name="id">

                    <div class="input-group mb-3">
                        <div class="input-group-prepend">
                            <span class="input-group-text" id="basic-addon3">https://example.com/users/</span>
                        </div>
                        <input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3">
                    </div>


                    <label for="title">Title:</label>
                    <input v-model="bookTitle" type="text" id="title" name="title">

                    <label for="quantity">Quantity:</label>
                    <input v-model="bookQuantity" type="text" id="quantity" name="quantity">

                    <label for="published_date">Published Date:</label>
                    <input v-model="bookDate" type="date" id="published_date" name="published_date">

                    <label for="genre">Genre:</label>
                    <input v-model="bookGenre" type="text" id="genre" name="genre">

                    <!-- <label for="author_id">Author ID:</label>
                    <input v-model="bookAuthorId" type="text" id="author_id" name="author_id"> -->

                    <label for="author_name">Author Name</label>
                    <select class="authorsSelect form-select" v-model="authors" multiple name="authors[]">
                        <option v-for="(authValue, index) in allAuthors" :value="authValue.id">{{ authValue.name }}
                        </option>
                    </select>

                    <input type="submit" value="Submit">
                </form>

            </form><!-- End General Form Elements -->

        </div>

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