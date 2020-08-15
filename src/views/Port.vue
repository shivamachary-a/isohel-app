<template>
  <div>
    <h1 class="title">YOUR PORTFOLIO</h1>
    <div class="field">
      <div class="control">
        <input v-model="stock" class="input" type="text" v-on:keyup.enter="add()" placeholder="Add stock">
      </div>
    </div>
    <div v-if="error" class="notification is-danger">
      <p>{{ message }}</p>
      <button class="delete" @click="hideNotif()"></button>
    </div>
    <a class="button is-info addbutton" @click="add()" >Add</a>
    <table class="table is-fullwidth is-hoverable">
      <thead>
        <tr>
          <th>STOCK</th>
          <th>PRICE</th>
          <th>REMOVE</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="stock in portfolio" :key="stock['Ticker']" >
          <td class="vert">{{ stock['Ticker'] }}</td>
          <td class="vert"><StockRow class="touch" :ticker= stock :id= stock.id></StockRow></td>
          <td><a class="button is-danger vert" @click="yoink(stock.id)" >X</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import { mapState, mapActions } from 'vuex';
import StockRow from '../components/StockRow.vue';
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
    color: black;
    background: whitesmoke;
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
