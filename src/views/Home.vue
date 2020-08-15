<template>
  <div class="vertical">
    <h3 class="center title" v-if="!isLoggedIn">
        <strong>welcome to isohel</strong>
    </h3>
    <p class="center">
      <button class="button is-rounded log is-outlined is-medium" @click="login()"> login</button>
    </p>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
  name: 'Home',
  computed: mapState('auth', ['user', 'isLoggedIn']),
  methods: mapActions('auth', ['login']),
};
</script>
<style scoped>
  .center {
    text-align: center;
  }
  .log{
    margin: 2em;
  }
  .vertical{
    vertical-align: middle;
  }
</style>
