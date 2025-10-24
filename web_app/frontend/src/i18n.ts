import { createI18n } from 'vue-i18n'
import { watch } from 'vue'
import en from './locales/en.json'
import vi from './locales/vi.json'

const i18n = createI18n({
  legacy: false,
  locale: localStorage.getItem('locale') || navigator.language.split('-')[0] || 'en',
  fallbackLocale: 'en',
  messages: {
    en,
    vi
  }
})

watch(
  () => i18n.global.locale.value,
  (newLocale: string) => {
    localStorage.setItem('locale', newLocale)
  }
)

export default i18n
