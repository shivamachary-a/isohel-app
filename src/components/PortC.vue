<template>
  <div>
    <table class="table is-fullwidth is-hoverable">
      <thead>
        <tr>
          <th>Stock</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="stock in portfolio" :key="stock['Ticker']" >
          <td class="vert">{{ stock['Ticker'] }}</td>
          <td class="vert"><StockRow class="touch" :ticker= stock :id= stock.id></StockRow></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import { mapState, mapActions } from 'vuex';
import StockRow from './StockRow.vue';
import port from '../store/port';

export default {
  name: 'Port',
  created() {
    this.bindPortfolios();
  },
  data: function () {
    return {
      stock: '',
      message: '',
      error: false,
    };
  },
  computed: mapState('port', ['portfolio']),
  methods: {
    ...mapActions('port', ['bindPortfolios', 'addToPortfolio'], ['deleteFromPortfolio']),
    ...mapActions('StockRow', ['deleteC']),
    add: function () {
      this.message = '';
      if (this.stock.length <= 4 && (typeof this.stock === 'string' || this.stock instanceof String)) {
        port.actions.addToPortfolio(this.stock);
        this.message = '';
        this.error = false;
      } else if (this.stock.length > 4) {
        this.message += 'Invalid input';
        this.error = true;
      }
      this.stock = '';
    },
    yoink: function (id) {
      port.actions.deleteFromPortfolio(id);
    },
    hideNotif: function () {
      this.error = false;
    },
  },
  components: {
    StockRow,
  },
};
</script>
<style scoped>

  .addbutton {
    background: aqua;
    margin-top: 1em;
    margin-bottom:1em;
    display: grid;
  }
  .vert {
    vertical-align: middle;
  }
  .touch{
    margin:0%;
  }


</style>
