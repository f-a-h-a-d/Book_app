<script setup>
import { onMounted } from "vue"
import Modal from './Modal.vue'

var columns = ref([]);
var books = ref();
const showModal = ref(false)


onMounted(() => {
    columns = ref(['SN', 'Book Code', 'Title', 'Quantity', 'Published Date', 'Genre', 'Author Name', 'Book Details', 'BookImage']);
    books = ref()

    axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/books/list/",
        headers: { "Content-Type": "multipart/form-data" },
    }).then((response) => {

        console.log(response.data);
        books = response.data;
        console.log(books);

    }).catch((error) => {
        // Handle error
        console.log(error);
    });

    return { columns, books };
})

</script>

<script>
import Layout from '../components/layouts/layout.vue'
import { ref } from 'vue';
import axios from 'axios';

export default {
    components: {
        Layout
    },
    name: 'App',

}
</script>


<template>
    <!-- General Form Elements -->




    <Layout>
        <div class="card-body">
            <table>
                <thead>
                    <tr>
                        <th v-for="column in columns">
                            {{ column }}
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(book, index) in books" :key="index">
                        <td v-for="(value, key) in book">
                            <span v-if="Array.isArray(value)">

                                <!-- <p v-for="arrValue in value">{{ arrValue.name }}</p> -->

                                <a type="button" v-for="arrValue in value" id="show-modal" @click="showModal = true">{{ arrValue.name }}</a>

                                <Teleport to="body">
                                    <!-- use the modal component, pass in the prop -->
                                    <modal :data="arrValue" :show="showModal" @close="showModal = false">
                                        <template #header>
                                            <template>Cuu</template>h3>
                                        </template>
                                    </modal>
                                </Teleport>

                            </span>
                            <span v-else>{{ value }} </span>

                        </td>
                    </tr>
                    <tr>
                        
                    </tr>
                </tbody>
            </table>
        </div>


    </Layout>

</template>

<style>
.card-body {
    padding-top: 75px;
    padding-right: 100px;

}

.container {
    text-align: center;
    margin-top: 50px;
}

table {
    width: 100%;
    border-collapse: collapse;
    border-spacing: 0;
    background-color: #fff;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin-left: 400px;
}

th,
td {
    border: 1px solid #dddddd;
    padding: 10px;
}

th {
    background-color: #f2f2f2;
    font-weight: bold;
}

tbody tr:nth-child(even) {
    background-color: #f9f9f9;
}

tbody tr:hover {
    background-color: #f0f0f0;
}

.modal {
    position: fixed;
    z-index: 999;
    top: 20%;
    left: 50%;
    width: 300px;
    margin-left: -150px;
}
span, a{
    margin:5px;
}
</style>