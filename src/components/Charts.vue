<template>
  <div class="hello hi is-flex">
    <VueTradingView :options="{
      theme: 'dark',
    }" />
  </div>
</template>

<script>
import VueTradingView from 'vue-trading-view';


export default {
  name: 'HelloWorld',
  props: {
    msg: String,
  },
  components: {
    VueTradingView,
  },
};
</script>
<style scoped>
  .hi{
    display: flexbox;
  }
</style>
