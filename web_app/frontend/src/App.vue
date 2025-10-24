<script setup lang="ts">
import Header from './components/Header.vue'
import Chat from './components/Chat.vue'
</script>

<template>
  <div id="app">
    <Header />
    <main>
      <router-view />
    </main>
    <Chat />
  </div>
</template>

<style>
/* Add any global styles here */
</style>
