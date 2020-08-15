<template>
    <div>
        <h1 class="title"> Predictions </h1>
        <div class="control">
            <input class="input" v-model="stockEntered" type="text" placeholder="Enter a ticker">
        </div>
        <div class="select margins">
            <select>
                <option v-for="stock in portfolio" :key="stock['Ticker']">
                    <p>{{ stock['Ticker'] }}</p>
                </option>
            </select>
        </div>

    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import port from '../store/port';


export default {
    name: 'Predictions',
    created: function () {
        this.bindPortfolios();
    },
    computed: mapState('port', ['portfolio']),
    methods: {
    ...mapActions('port', ['bindPortfolios', 'addToPortfolio'], ['deleteFromPortfolio']),
    },
};
</script>

<style scoped>

    .margins {
        margin-top:1em;
        margin-bottom: 1em;

    }

</style>
