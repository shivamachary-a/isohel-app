<template>
 <VueRssFeed :feedUrl='feedUrl' :name='name' :limit='limit'/>
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
