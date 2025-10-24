<script setup lang="ts">
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'

const { t, locale } = useI18n()
const locales = ref(['en', 'vi'])
</script>

<template>
  <header class="bg-white shadow-md">
    <div class="container mx-auto px-4 py-2 flex justify-between items-center">
      <div class="flex items-center">
        <img src="/vite.svg" alt="Logo" class="h-8 w-8 mr-2">
        <span class="text-xl font-bold">Bản Yên Hòa</span>
      </div>
      <nav class="hidden md:flex items-center space-x-4">
        <router-link to="/" class="text-gray-600 hover:text-gray-800">{{ t('nav.home') }}</router-link>
        <router-link to="/mini-game" class="text-gray-600 hover:text-gray-800">{{ t('nav.mini_game') }}</router-link>
      </nav>
      <div class="flex items-center space-x-4">
        <select v-model="locale" class="border rounded px-2 py-1">
          <option v-for="lang in locales" :key="lang" :value="lang">{{ lang.toUpperCase() }}</option>
        </select>
        <button class="text-gray-600 hover:text-gray-800">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </button>
        <button class="text-gray-600 hover:text-gray-800">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7" />
          </svg>
        </button>
      </div>
    </div>
  </header>
</template>
