import Vue from 'vue';
import VueRouter from 'vue-router';
import { mapActions, mapState } from 'vuex';
import auth from '../store/auth';

import Home from '../views/Home.vue';
import Dash from '../views/Dash.vue';
import BS from '../views/BlackScholes.vue';
import Port from '../views/Port.vue';
import Account from '../views/Account.vue';
import Yeet from '../views/Yeet.vue';
import Anal from '../views/Analysis.vue';
import Vol from '../views/Volatility.vue';
import Watchlist from '../views/Watchlist.vue';
import News from '../views/News.vue';
import Prediction from '../views/PredictionsBeta.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {
      requiresLogOut: true,
    },
  },
  {
    path: '/dash',
    name: 'Dash',
    component: Dash,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/volatility',
    name: 'Vol',
    component: Vol,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/BlackScholes',
    name: 'BlackScholes',
    component: BS,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/Analysis',
    name: 'Analysis',
    component: Anal,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/port',
    name: 'Port',
    component: Port,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/account',
    name: 'Account',
    component: Account,
  },
  {
    path: '/watchlist',
    name: 'Watchlist',
    component: Watchlist,
  },
  {
    path: '/ping',
    name: Yeet,
    component: Yeet,
  },
  {
    path: '/news',
    name: 'News',
    component: News,
  },
  {
    path: '/pred',
    name: 'Prediction',
    component: Prediction,
  },
];

const router = new VueRouter({
  routes,
});


export default router;
