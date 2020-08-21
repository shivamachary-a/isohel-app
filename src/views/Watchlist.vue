<template>
  <div>
    <a class="button back" @click="$router.go(-1)">
      Back
    </a>
    <h1 class="title">Your Watchlist</h1>
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
          <th>Stock</th>
          <th>Price</th>
          <th>Remove</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="stock in watchlist" :key="stock['Ticker']" >
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
import watch from '../store/watch';

export default {
    name: 'Watch',
    data: function () {
        return {
        stock: '',
        message: '',
        error: false,
        };
    },
    created: function () {
    this.bindWatchlist();
    },
    computed: mapState('watch', ['watchlist']),
    methods: {
        ...mapActions('watch', ['bindWatchlist', 'addToWatchlist', 'deleteFromWatchlist']),
        add: function () {
            this.message = '';
            if (this.stock.length <= 4 && (typeof this.stock === 'string' || this.stock instanceof String)) {
                watch.actions.addToWatchlist(this.stock);
                this.message = '';
                this.error = false;
            } else if (this.stock.length > 4) {
                this.message += 'Invalid input';
                this.error = true;
            }
            this.stock = '';
        },
        yoink: function (id) {
            watch.actions.deleteFromWatchlist(id);
        },
    },
    components: {
        StockRow,
    },
};
</script>

<style scoped>
.addbutton {
    color:black;
    background:whitesmoke;
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
