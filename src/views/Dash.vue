<template>
  <div class="container is-fluid">
    <div class="tile is-ancestor ">
      <div class="tile is-vertical ">
        <div class="tile" >
          <div class="tile is-parent is-vertical">
            <article class="tile is-child notification ding">
              <p class="title is-1 has-text-weight-light">
                  WELCOME
              </p>
            </article>
            <article class="tile is-child notification is-black">
              <Charts></Charts>
            </article>
          </div>
          <div class="tile is-parent">
            <article class="tile is-child notification watchlist">
                <p class="title has-text-weight-light">WATCHLIST</p>
                  <Watch></Watch>
            </article>
          </div>
          <div class="tile is-parent is-vertical">
            <article class="tile is-child notification portfolio">
              <p class="title has-text-weight-light">PORTFOLIO</p>
              <div>
                <Port></Port>
              </div>
            </article>
          </div>
        </div>
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
