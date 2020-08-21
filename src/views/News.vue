<template>
<div>
  <a class="button back" @click="$router.go(-1)">
    Back
  </a>
 <VueRssFeed :feedUrl='feedUrl' :name='name' :limit='limit'/>
</div>
</template>

<script>
import VueRssFeed from 'vue-rss-feed';

export default {
  name: 'Demo',
  components: {
    VueRssFeed,
  },
  data() {
    return {
      feedUrl: 'https://rss.app/feeds/gtIZloLZVNP9YY7z.xml',
      name: '',
      limit: 5,
    };
  },
};
</script>

<style>

</style>
