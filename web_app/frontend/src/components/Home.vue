<script setup lang="ts">
import { useI18n } from 'vue-i18n'
import WelcomeBanner from './WelcomeBanner.vue'
import Banner from './Banner.vue'

const { tm } = useI18n()

const banners = tm('banners') as { title: string; description: string }[]
</script>

<template>
  <div v-if="banners && banners.length > 0">
    <WelcomeBanner
      v-if="banners[0]"
      :title="banners[0].title"
      :description="banners[0].description"
      :image-url="`/main.jpg`"
    />
    <Banner
      v-for="(banner, index) in banners.slice(1)"
      :key="index"
      :title="banner.title"
      :description="banner.description"
      :image-url="
        banner.title === 'Món ăn đặc sản' || banner.title === 'Local Specialties'
          ? '/COMALMGANUONG.jpg'
          : banner.title === 'Tháp cổ linh thiêng' || banner.title === 'Sacred Ancient Tower'
            ? '/thap.jpg'
            : banner.title === 'Bản sắc dân tộc Thái' || banner.title === 'Thai Ethnic Identity'
              ? '/muaxoe.jpeg'
              : banner.title === 'Làng nghề dệt thổ cẩm' || banner.title === 'Brocade Weaving Village'
                ? '/dethocam.jpg'
                : `https://picsum.photos/800/600?random=${index + 1}`
      "
      :reverse="(index + 1) % 2 !== 0"
      :bg-color="(index + 1) % 2 === 0 ? 'bg-white' : 'bg-gray-100'"
    />
  </div>
</template>
