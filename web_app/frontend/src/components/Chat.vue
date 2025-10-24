<script setup lang="ts">
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'

const { t, locale } = useI18n()
const isOpen = ref(false)
const messages = ref<{ role: string; content: string }[]>([])
const userInput = ref('')

const sendMessage = async () => {
  if (!userInput.value.trim()) return

  messages.value.push({ role: 'user', content: userInput.value })
  userInput.value = ''

  try {
    const response = await fetch('http://localhost:8000/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ messages: messages.value, locale: locale.value })
    })

    if (response.ok) {
      const data = await response.json()
      messages.value.push(data)
    } else {
      console.error('Error sending message:', response.statusText)
    }
  } catch (error) {
    console.error('Error sending message:', error)
  }
}
</script>

<template>
  <div>
    <button
      class="fixed bottom-4 right-4 bg-blue-500 text-white rounded-full w-16 h-16 flex items-center justify-center shadow-lg"
      @click="isOpen = !isOpen"
    >
      <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
      </svg>
    </button>
    <div
      v-if="isOpen"
      class="fixed bottom-24 right-4 bg-white rounded-lg shadow-lg w-80 h-96 flex flex-col"
    >
      <div class="p-4 border-b">
        <h3 class="font-bold">{{ t('chat.button') }}</h3>
      </div>
      <div class="flex-1 p-4 overflow-y-auto">
        <div v-for="(message, index) in messages" :key="index" class="mb-2">
          <div
            :class="[
              'p-2 rounded-lg',
              message.role === 'user' ? 'bg-blue-100 text-right' : 'bg-gray-100'
            ]"
          >
            {{ message.content }}
          </div>
        </div>
      </div>
      <div class="p-4 border-t">
        <input
          type="text"
          v-model="userInput"
          :placeholder="t('chat.placeholder')"
          class="w-full border rounded px-2 py-1"
          @keyup.enter="sendMessage"
        >
      </div>
    </div>
  </div>
</template>
