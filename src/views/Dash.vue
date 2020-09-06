<template>
<div class="container is-fluid">
  <div class="level tile is-ancestor">
    <div class ="level-item tile is-vertical is-parent">
      <article class ="tile is-child box">
        WELCOME
      </article>
      <article class ="tile is-child">
        <Charts></Charts>
      </article>
    </div>
      <div class="level-item tile is-parent is-vertical">
        <article class="tile is-child box portfolio mx-4">
          <h1 class="title has-text-weight-light has-text-white header">PORTFOLIO</h1>
          <Port></Port>
        </article>
        <article class="tile is-child box">
          <p class="is-family-code mt-6 is-size-7">note: sometimes you might have to press refresh if theres an error.</p> 
        </article>
      </div>
      <div class="level-item tile is-parent -is-vertical">
        <article class="tile is-child box watchlist mx-4">
            <h1 class="title has-text-weight-light has-text-white header">WATCHLIST</h1>
            <Watch></Watch>
        </article>
      </div>
  </div>
</div>
</template>

<script>

import { mapActions, mapState } from 'vuex';
import VueTradingView from 'vue-trading-view';
import router from '@/router';

import StockRow from '../components/StockRow.vue';
import Charts from '../components/Charts.vue';
import Port from '../components/PortC.vue';
import Watch from '../components/WatchC.vue';

export default {
  computed: mapState('auth', ['user', 'isLoggedIn']),
  methods: {
    cunt: function () {
      router.push('/analysis');
    },

  },
  components: {
    Charts,
    Port,
    Watch,
  },
};
</script>
<style scoped>
  .header {
    margin-bottom:1em;
  }
</style>
