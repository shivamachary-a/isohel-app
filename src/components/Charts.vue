<template>
  <div class="hello">
    <VueTradingView :options="{
      theme: 'light',
      width: '600',
      height: '400',
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
