import Vue from 'vue';
import VueRouter from 'vue-router';
import { mapActions, mapState } from 'vuex';
import auth from '../store/auth';

import Home from '../views/Home.vue';
import Dash from '../views/Dash.vue';
import Analysis from '../views/Analysis.vue';
import Port from '../views/Port.vue';
import Account from '../views/Account.vue';
import Yeet from '../views/Yeet.vue';

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
    path: '/analysis',
    name: 'Analysis',
    component: Analysis,
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
