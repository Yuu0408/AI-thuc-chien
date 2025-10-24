<script setup lang="ts">
defineProps<{
  title: string
  description: string
  imageUrl: string
}>()
</script>

<template>
  <div
    class="relative h-96 bg-cover bg-center text-white flex items-center justify-center text-center"
    :style="{ backgroundImage: `url(${imageUrl})` }"
    data-aos="zoom-in"
  >
    <div class="absolute inset-0 bg-black opacity-50"></div>
    <div class="relative z-10 p-4">
      <h1 class="text-5xl font-bold mb-4">{{ title }}</h1>
      <p class="text-lg">{{ description }}</p>
    </div>
  </div>
</template>
