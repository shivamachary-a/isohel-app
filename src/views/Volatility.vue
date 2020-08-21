<template>
    <div>
        <a class="button back" @click="$router.go(-1)">
            Back
        </a>
        <div class="box">
            <h1 class="title">Volatility</h1>
            <h1 class="subtitle">Enter the stock ticker:</h1>
            <b-field label="Stock Ticker">
                <b-input v-model="ticker"></b-input>
            </b-field>
            <div class="control">
                <a class="button" v-on:click.prevent="submit()">Calculate</a>
            </div>
        </div>
        <section class="hero is-light" v-if="clicked">
            <div class="hero-body">
                <div class="container">
                <h1 class="title">
                    Volatility calculated: {{ Math.round(results.yonk[0]['Result']) / 100 }}
                </h1>
                <h1 class="subtitle">
                    How did we calculate this?
                </h1>
                <p class="content">
                     Volatility is simply the standard deviation of the stock prices.
                     We calculate volatility over the last two hundred trading days.</p>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            ticker: '',
            addStockForm: {
                ticker: '',
            },
            results: [],
            clicked: false,
        };
    },
    methods: {
        getResult: function () {
            const path = 'http://localhost:5000/volatility';
            axios.get(path)
                .then((res) => {
                    this.results = res.data;
                    console.log(this.results);
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        addstock: function (payload) {
            const path = 'http://localhost:5000/volatility';
            axios.post(path, payload)
            .then(() => {
            this.getResult();
            })
            .catch((error) => {
            // eslint-disable-next-line
            console.log(error);
            this.Result();
            });
            this.clicked = true;
        },
        submit: function () {
            const payload = {
                ticker: this.ticker,
            };
            this.addstock(payload);
            this.ticker = '';
            console.log('Clicked once');
        },
    },
    created: function () {
        this.getResult();
    },

};
</script>

<style>

.vol{
    margin:1em
}

</style>
