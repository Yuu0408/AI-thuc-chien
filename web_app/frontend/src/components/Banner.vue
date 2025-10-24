<script setup lang="ts">
defineProps<{
  title: string
  description: string
  imageUrl: string
  reverse?: boolean
  bgColor?: string
}>()
</script>

<template>
  <div :class="[bgColor, 'py-8']">
    <div class="container mx-auto px-4">
      <div
        class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center"
        :class="{ 'md:grid-flow-col-dense': reverse }"
      >
        <div
          :class="{ 'md:col-start-2': reverse }"
          data-aos="fade-up"
        >
          <img :src="imageUrl" alt="Banner image" class="rounded-lg shadow-lg">
        </div>
        <div
          :class="{ 'md:col-start-1': reverse }"
          data-aos="fade-up"
          data-aos-delay="200"
        >
          <h2 class="text-3xl font-bold mb-4">{{ title }}</h2>
          <p class="text-gray-600">{{ description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>
