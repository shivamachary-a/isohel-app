<template>
    <div>
        <h1 class="columns" v-for="stock in watchlist" :key="stock['Ticker']">
            <p class="vert column is-family-code"> {{ stock['Ticker'] }}</p>
            <StockRow class="touch column is-family-monospace" :ticker= stock :id= stock.id></StockRow>
        </h1>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import StockRow from './StockRow.vue';
import watch from '../store/watch';

export default {
    name: 'Watch',
    data: function () {
        return {
        stock: '',
        };
    },
    created: function () {
    this.bindWatchlist();
    },
    computed: mapState('watch', ['watchlist']),
    methods: {
        ...mapActions('watch', ['bindWatchlist', 'addToWatchlist', 'deleteFromWatchlist']),
        add: function () {
            watch.actions.addToWatchlist(this.stock);
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
