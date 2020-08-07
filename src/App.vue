<template>
  <div id="app">
    <nav class="navbar navigationbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
      <a class="navbar-item" href="/#/">
        ISOHEL
      </a>
      </div>
      <div class="navbar-end">
        <p class = "control" v-if="isLoggedIn">
          <a class="button is-white myButton" @click="goToPort()">Portfolio</a>
        </p>
        <p class = "control" v-if="isLoggedIn">
          <a class="button is-white myButton" @click="goToDash()">Dashboard</a>
        </p><p class = "control" v-if="isLoggedIn">
          <a class="button is-white myButton" @click="goToAnalysis()">Analysis</a>
        </p>
        <p class = "control" v-if="isLoggedIn">
          <a class="button namelabel myButton" @click="goToAcc()">{{ user.name }}</a>
        </p>
        <p class="control" v-if="!isLoggedIn">
          <a class="button is-white myButton" @click="login()">Login with Google</a>
        </p>
        <p class = "control" v-if="isLoggedIn">
          <a class="button is-danger myButton" @click="logout(); leave();">Logout</a>
        </p>
      </div>
    </nav>
    <router-view class="main container"/>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';
import router from '@/router';

export default {
  computed: mapState('auth', ['user', 'isLoggedIn']),
  methods: {
    ...mapActions('auth', ['login', 'logout', 'leave']),

    ...mapActions('navigation', ['goToPort', 'goToAnalysis', 'goToDash', 'goToAcc']),
  },
};
</script>

<style lang="scss">
.main{
  margin-top: 2em;

}

.home{
  margin-right: 2em;
  margin-left: 2em;
}

.myButton{

  margin-left: 1em;
  margin-right: 1em;
  margin-top: 1em;
  margin-bottom: 1em;
}

.namelabel{

  color: white;
  background: #1ec2cb;
  margin-left: 1em;
  margin-right: 1em;
  margin-top: 1em;
  border: #3e82ad;

}

.butlabel{

  color: white;
  background: #1ec2cb;
  border: #3e82ad;

}

.navigationbar{
  background: rgb(221,170,231);
  background:
   linear-gradient(90deg, rgba(221,170,231,1) 0%, rgba(170,196,233,1) 31%, rgba(56,255,236,1) 100%);
}

.portfolio{
  background: #cbfffa;
}

.watchlist{
  background: #fae1ff;
}

</style>
