<template>
  <div id="app">
    <nav class="navbar navigationbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
      <a class="navbar-item isohel" @click="goToDash()">
        ISOHEL
      </a>
      </div>
        <div class="navbar-item has-dropdown is-hoverable" v-if="isLoggedIn">
          <a class="navbar-item isohel is-arrowless">
            MENU
          </a>
          <div class="navbar-dropdown">
            <a class="navbar-item" @click="goToNews()">
              News
            </a>
            <a class="navbar-item" @click="goToWatch()">
              Watchlist
            </a>
            <a class="navbar-item" @click="goToPort()">
              Portfolio
            </a>
            <a class="navbar-item" @click="goToAnalysis()">
              Analysis
            </a>
          </div>
        </div>
      <div class="navbar-end">
        <p class = "navbar-item isohel" v-if="isLoggedIn">
              {{ user.name  }}
        </p>
        <a class = "navbar-item is-danger isohel" v-if="isLoggedIn" @click="logout();leave()">
            Logout
        </a>
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

    ...mapActions('navigation', ['goToPort', 'goToAnalysis', 'goToDash', 'goToAcc', 'goToWatch', 'goToNews']),
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
  background: #363636;
  color: whitesmoke;
}

.portfolio{
  background: #e8175d;
  color: whitesmoke;
  margin-left: 0.5em;
  margin-right: 0.5em;
}

.watchlist{
  background: #cc527a;
  color: whitesmoke;
  margin-left: 0.5em;
  margin-right: 0.5em;
}
.loggedIn{
  display: grid;

}
.isohel{
  color:whitesmoke;
}

.ding{
  background: white;
  color: #363636;
}
.chartstuff {
  background: #141722;
}

</style>
