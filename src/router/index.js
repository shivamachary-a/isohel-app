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
    path: '/ping',
    name: Yeet,
    component: Yeet,
  },
];

const router = new VueRouter({
  routes,
});


export default router;
