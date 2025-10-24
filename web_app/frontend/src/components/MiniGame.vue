<script setup lang="ts">
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { UploadCloud } from 'lucide-vue-next'

const { t } = useI18n()
const isDragging = ref(false)
const imageSrc = ref('')
const fileInput = ref<HTMLInputElement | null>(null)

function onDragEnter(e: DragEvent) {
  e.preventDefault()
  isDragging.value = true
}

function onDragLeave(e: DragEvent) {
  e.preventDefault()
  isDragging.value = false
}

function onDrop(e: DragEvent) {
  e.preventDefault()
  isDragging.value = false
  const files = e.dataTransfer?.files
  if (files && files.length > 0) {
    const file = files[0]
    if (file) {
      const reader = new FileReader()
      reader.onload = (event) => {
        imageSrc.value = event.target?.result as string
      }
      reader.readAsDataURL(file)
    }
  }
}

function onFileChange(e: Event) {
  const files = (e.target as HTMLInputElement).files
  if (files && files.length > 0) {
    const file = files[0]
    if (file) {
      const reader = new FileReader()
      reader.onload = (event) => {
        imageSrc.value = event.target?.result as string
      }
      reader.readAsDataURL(file)
    }
  }
}

function triggerFileInput() {
  fileInput.value?.click()
}
</script>

<template>
  <div class="mini-game-container">
    <div class="banner">
      <h1>{{ t('mini_game.title') }}</h1>
      <p>{{ t('mini_game.description') }}</p>
    </div>
    <div
      class="upload-section"
      :class="{ 'is-dragging': isDragging }"
      @dragenter="onDragEnter"
      @dragleave="onDragLeave"
      @dragover.prevent
      @drop="onDrop"
    >
      <div v-if="!imageSrc">
        <UploadCloud class="mx-auto h-16 w-16 text-gray-400" />
        <p>{{ t('mini_game.upload_prompt') }}</p>
        <button @click="triggerFileInput" class="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
          Select a File
        </button>
        <input type="file" ref="fileInput" @change="onFileChange" class="hidden" />
      </div>
      <img v-else :src="imageSrc" alt="Uploaded image" class="mx-auto" />
    </div>
  </div>
</template>

<style scoped>
.mini-game-container {
  padding: 2rem;
  max-width: 800px;
  margin: 0 auto;
}

.banner {
  background: linear-gradient(to right, #6a11cb, #2575fc);
  color: white;
  padding: 3rem;
  text-align: center;
  margin-bottom: 2rem;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.banner h1 {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.banner p {
  font-size: 1.2rem;
}

.upload-section {
  border: 2px dashed #ccc;
  padding: 4rem;
  text-align: center;
  transition: background-color 0.3s;
  border-radius: 8px;
}

.upload-section.is-dragging {
  background-color: #f0f8ff;
  border-color: #2575fc;
}

.upload-section p {
  font-size: 1.2rem;
  margin-bottom: 1rem;
}

.upload-section input[type="file"] {
  margin-top: 1rem;
}

.upload-section img {
  margin-top: 2rem;
  max-width: 100%;
  border-radius: 8px;
}
</style>
