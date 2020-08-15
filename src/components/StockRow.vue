<template>
  <div>
      <tr v-if="componentKey">
        <td class="pricebox">{{ getPrice() }}</td>
        <a class ="button is-small yeet" @click="refresh()">Refresh</a>
      </tr>
  </div>
</template>
<script>
import firebase from '@/firebase';
import store from '@/store';
import db from '@/db';
import port from '../store/port';

export default {
  name: 'StockRow',
  props: ['ticker', 'id'],
  data() {
    return {
      stockdetails: {
        price: null,
        time: null,
        date: null,
      },
      clicked: false,
      componentKey: true,
    };
  },
  methods: {
    async calliex() {
      const base = 'https://sandbox.iexapis.com/stable/stock/';
      const stock = this.ticker['Ticker'];
      const end = '/quote/latestPrice?token=Tsk_12a652ebe24b4421a3401e1a649f418c';
      const url = base.concat(stock).concat(end);
      await fetch(url)
        .then((response) => response.json())
        // eslint-disable-next-line
        .then((data) => {
          this.stockdetails.price = data;
          console.log(this.stockdetails);
        });
    },

    deleteC() {
      port.actions.deleteFromPortfolio(this.id);
    },
    getPrice() {
      const curr = '£';
      const price = (Math.round(this.stockdetails.price * 100) / 100);
      if (price === 0) {
        return 'error';
      } else {
        return curr + price;
      }
    },
    refresh() {
      this.calliex();
      this.getPrice();
    },
  },
  created: function () {
    this.refresh();
    if (this.stockdetails.price === 0) {
      this.refresh();
    }
    window.setInterval(() => {
      this.refresh();
      }, 5000);
  },
};
</script>
<style scoped>
.yeet {
  display: grid;
  margin-left: 1em;
}

.pricebox {
  margin-right: 3em;
}
</style>
