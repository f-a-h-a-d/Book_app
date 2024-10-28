<script setup>
import { ref } from 'vue'
import practiceComp from './practice.vue';

const value = ref('I am from parent component')

</script>

<template>
    <div>
        <button> Click</button>
    </div>
    <div> 
        <practiceComp :msg = 'value'/>
    </div>
   
</template>