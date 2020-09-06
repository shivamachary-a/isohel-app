<template>
    <div>
        <a class="button back" @click="$router.go(-1)">
            Back
        </a>
        <h1 class="title is-1 title has-text-weight-light"> PREDICTIONS </h1>
        <h3 class="title is-3 has-text-weight-light"> ENTER A TICKER: </h3>
        <div class="control">
            <input class="input is-rounded" v-model="options" type="text" placeholder="Enter a ticker">
        </div>
        <h3 class="title margins is-3 has-text-weight-light"> OR CHOOSE FROM YOUR PORTFOLIO: </h3>
        <div class="margins">
            <p v-for="stock in portfolio" :key="stock['Ticker']" :value="stock['Ticker']">
                <button class="button buttons is-outlined" @click="map(stock['Ticker'])">{{ stock['Ticker'] }}</button>
            </p>
        </div>
        <button class="button buttons is-rounded is-outlined" @click="submit()">Submit</button>
        <div class="title is-2 has-text-weight-light is-italic" v-if="loading">
            <p> Price: £{{ stocks['yonk'][0]['Price'] }}</p>
            <p>{{ result }}</p>
        </div>
        <div v-if="loadingbar">
            <progress class="progress is-danger" max="100">30%</progress>
        </div>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import port from '../store/port';
import axios from 'axios';

export default {
    name: 'Predictions',
    created: function () {
        this.bindPortfolios();
    },
    created() {
        this.getResult();
    },
    data() {
        return {
        success: false,
        isActive: false,
        stocks: [],
        options: '',
        result: '',
        loading: false,
        loadingbar:false,
        addStockForm: {
            Ticker: '',
            Price: '',
            Strike: '',
            Time: '',
            Interest: '',
            Volatility: '',
        },
    };
  },
    computed: mapState('port', ['portfolio']),
    methods: {
        ...mapActions('port', ['bindPortfolios', 'addToPortfolio'], ['deleteFromPortfolio']),
        getResult() {
            this.loading = true;
            console.log('GETTING');
            const path = 'http://localhost:5000/analysis';
            axios.get(path)
                .then((res) => {
                this.stocks = res.data;
                if (this.stocks['yonk'][0]['Result'] == true) {
                    this.result = 'We see this stock going up, and advise a buy.';
                } else if (this.stocks['yonk'][0]['Result'] == false) {
                    this.result = 'We see this stock going down, and advise you not to buy, or to sell now.';
                } else if (this.stocks['yonk'][0]['Price'] == 0) {
                    this.result = 'We could not complete your request as of now. Please try again later';
                };

                this.loading = true;
                this.loadingbar = false;
                console.log(res.data);
                console.log('DATA ABOVE');
                })
                .catch((error) => {
                console.error(error);
                });
            },
        addstock: function (payload) {
            this.loading = false;
            this.loadingbar = true;
            this.result = 'Loading';
            const path = 'http://localhost:5000/analysis';
            axios.post(path, payload)
            .then(( ) => {
            this.getResult();
            })
            .catch((error) => {
            // eslint-disable-next-line
            console.log(error);
            this.Result();
            });
        },      
        submit: function () {
            const payload = {
                ticker: this.options,
            };
            this.addstock(payload);
            this.options = '';
            console.log('YOINK');
        },
        map: function (value) {
            this.options = value;
        }
    },
};
</script>

<style scoped>

    .margins {
        margin-top:1em;
        margin-bottom: 1em;

    }
    .buttons {
        margin-top: 1em;
        background: #FFFFFF;
    }

</style>
