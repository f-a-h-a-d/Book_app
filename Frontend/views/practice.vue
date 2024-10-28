

<script setup>
import { ref } from 'vue'
import Layout from '../components/layouts/layout.vue'


    const props = defineProps(
        {
          msg: String  
        }
    )

    const favouriteCharacters = ref([]);
    const allCharacter = ref([ "Naruto" , "Itachi", "Saskae"]);
    const newCharacterValue= ref('');

    function ImplementAdding(eachCharacter){
        favouriteCharacters.value.push(eachCharacter)
    };
    function AddingCharacterToList(){      
        allCharacter.value.push(newCharacterValue)
    }

</script>

<template>

    <div>
        <p>{{favouriteCharacters }}</p>
    </div>
    <div>
    <ul>
        <li v-for="eachCharacter in allCharacter">
            <p>{{eachCharacter}}</p>
            <button @click="ImplementAdding(eachCharacter)">Favourite</button>
        </li>
    </ul>
    </div>
    <div>
        <form action="">
            <label for="">Put your favourite Characters</label>
            <input type="text" v-model="newCharacterValue">
            <button @keyup.enter="allCharacter.push(newCharacterValue)">Click</button>
        </form>
    </div>

    <p>{{ msg }}</p>

    <Layout>
        
    </Layout>
    
</template>

<style>

</style>
