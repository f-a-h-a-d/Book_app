<template>
    <SideBar/>
    <Header />
    <slot />
    
    
</template>

<script>
import Header from './headers/header.vue'
import SideBar from './sidebars/sideBar.vue'

export default {
  name: 'Layout',
  components: {
    Header,
    SideBar
  }
}
</script>