<template>
<div>
  <div class="container cont is-fluid">
    <div class="">
        <div class="tile is-ancestor ">
        <div class="tile is-vertical ">
          <div class="tile" >
            <div class="tile is-parent is-vertical">
              <article class="tile is-child notification is-grey">
                <p class="title is-1">Hi,</p>
                <p class="subtitle is-4">{{user.name}}</p>
                <p class="subtitle is-6">Welcome to isohel.</p>
                <p class="subtitle is-6">Check out the latest guides and tools added!</p>
              </article>
              <article class="tile is-child notification is-light">
                <p class="title"> Charts </p>
                <p class="subtitle"> Powered by TradingView </p>
                <Charts></Charts>
              </article>
            </div>
            <div class="tile is-parent ">
              <article class="tile is-child notification watchlist">
                <div class="content">
                  <p class="title">Your watchlist</p>
                  <p class="subtitle">You've got your eye on these:</p>
                  <div class="content">
                    <!-- Content -->
                  </div>
                </div>
              </article>
            </div>
            <div class="tile is-parent is-vertical ">
              <article class="tile is-child notification portfolio">
                <p class="title">Portfolio</p>
                <p class="subtitle">Your stocks:</p>
                <div class="table=container">
                  <Port></Port>
                </div>
              </article>
            </div>
          </div>
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
  },
};
</script>
<style scoped>
  .tilestruct {
    display: grid;
    align-self: center;
  }
  .cont{
    margin-bottom: 1em;
  }
</style>
