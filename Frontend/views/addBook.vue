<script>
import Layout from '../components/layouts/layout.vue'
import { onMounted } from "vue"
import { isProxy, toRaw } from 'vue';

import 'jquery';

export default {
    components: {
        Layout
    },

}

</script>

<script setup>
import axios from "axios";
import { ref } from "vue";
import { onMounted } from "vue";
import vSelect from "vue-select";
import "vue-select/dist/vue-select.css";


const allAuthors = ref();
let booklen = ref(0);
let bookcode = ref()
var selectedFile = ref(null);

onMounted(() => {
    try {
        const response = axios.get("http://127.0.0.1:8000/api/author/list/").then((response) => {

            allAuthors.value = response.data;

        });

        const response2 = axios.get("http://127.0.0.1:8000/api/books/list/").then((response2) => {
            console.log(response2.data);
            booklen = response2.data.length;
            bookcode = 'B-' + String(booklen);
            console.log(bookcode);
        })


    } catch (error) {
        console.error(error);
    }
})


const bookId = ref('');
const bookTitle = ref('');
const bookQuantity = ref('');
const bookDate = ref('');
const bookGenre = ref('');
const bookAuthorName = ref('');
const author_id = ref(1);
const authors = ref([]);
const bookDetails = ref('');


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
    
    console.log(selectedFile);
    console.log(authors.value);
    console.log(authors.value.ProxyArray[0].target.ProxyObjectŒ);

    const formData = {
        book_code: bookcode,
        title: bookTitle.value,
        quantity: parseInt(bookQuantity.value),
        published_date: formattedDate,
        genre: bookGenre.value,
        //author: authors.value,
        book_details: bookDetails.value,
        book_image: selectedFile
    }
    
    // console.log(formData);

    // const myform = new FormData();
    // myform.append("book_code", bookcode);
    // myform.append("title", bookTitle.value);
    // myform.append("quantity", bookQuantity.value);
    // myform.append("genre", bookGenre.value);
    // myform.append("author", authors.value);
    // myform.append("book_details",bookDetails.value);
    
    // myform.append("book_image", selectedfile.value); 

    // console.log(myform);

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
        bookDetails = ref('');


    })
        .catch((error) => {
            // Handle error
            console.log(error);
        });
}

function onFieldSelected(event){
    console.log(event);
    selectedFile = event.target.files[0];
    console.log(selectedFile);
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
                    
                    <label>Book Code</label>
                    <div class="input-group mb-3">
                        <div class="input-group-prepend">
                            <span class="input-group-text" id="basic-addon3">{{ bookcode }}</span>
                        </div>
                        
                    </div>

                    <label for="title">Title:</label>
                    <input v-model="bookTitle" type="text" id="title" name="title">

                    <label for="quantity">Quantity:</label>
                    <input v-model="bookQuantity" type="text" id="quantity" name="quantity">

                    <label for="published_date">Published Date:</label>
                    <input v-model="bookDate" type="date" id="published_date" name="published_date">

                    <label for="genre">Genre:</label>
                    <input v-model="bookGenre" type="text" id="genre" name="genre">

                    <label for="exampleFormControlTextarea1">Book Details</label>
                    <textarea v-model="bookDetails" placeholder="Add Details" rows="3"></textarea>
                    
                    <label>Book Authors</label>
                    <v-select v-model="authors" multiple :options="allAuthors" label="name"></v-select>

                    <label>Input Image</label>
                    <input type="file" @change="onFieldSelected">

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