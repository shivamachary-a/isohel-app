<template>
  <div>
      <a class="button back" @click="$router.go(-1)">
        Back
      </a>
      <p class="centerheading">Black and Scholes Analysis</p>
      <section class="modal" v-bind:class="{ 'is-active':isActive }"
          ref="addStockModal" id="stock-modal">
        <div class="modal-background"></div>
        <div class ="modal-card">
          <div class="box">
            <h1 class="title">Analysis</h1>
            <h1 class="subtitle">Enter the stock ticker:</h1>
            <b-field label="Stock Ticker">
                <b-input v-model="addStockForm.Ticker"></b-input>
            </b-field>
            <b-field label="Price">
                <b-input v-model="addStockForm.Price"></b-input>
            </b-field>
            <b-field label="Strike Price">
                <b-input v-model="addStockForm.Strike"></b-input>
            </b-field>
            <b-field label="Time to Maturity">
                <b-input v-model="addStockForm.Time"></b-input>
            </b-field>
            <b-field label="Interest">
                <b-input v-model="addStockForm.Interest"></b-input>
            </b-field>
            <b-field label="Volatility">
                <b-input v-model="addStockForm.Volatility"></b-input>
            </b-field>
            <div class="control">
                <a class="button" v-on:click.prevent="onSubmit()">Add</a>
            </div>
          </div>
        </div>
        <button class="modal-close is-large" aria-label="close" @click="hide()"></button>
      </section>
        <a class="button analysebutton butlabel" @click="show()">
          Analyse with Black and Scholes
        </a>
      <div class="content">
        <a class="panel-block panel">
          <p class="is-medium">
            Use this analysis tool if you are looking to trade options. What are options?
            In finance, an option is a contract that gives you the right to buy or sell
            an underlying asset
            (this could be a stock, currency, bond
            etc) at a certain price, known as the strike price, before or on a specific date,
            known as the expiry date.
            The Black and Scholes formula is one of the most famous in finance, and is used to
            determine
            a fair value of an option. Essentially, if the option is priced under the value
            calculated
            for the expiry date, you would buy it.
            The formula is focused on European call options, meaning you can only exercise
            your
            right to buy on a specific date.
          </p>
        </a>
        <a class="panel-block panel">
          <p class="is-medium">
            Here's an example.

            Consider you sign into an option contract at £2, with a strike price of £50 and
            an expiry date of 1 year from now. An option contract usually includes 100 shares
            of the underlying asset, which in this case we will
            call 'XMPL'. You pay £200 for the right to buy 100 shares in XMPL one year from
            now, at a price of £50 per share.  Now let's imagine one year from now,
            the price of one share in 'XMPL' is £60. You have the right
            to buy 100 of these shares at £50. So you buy them for a total of £5,000,
            and then sell them at the current rate of £60 per share, meaning you now
            have £6,000. Now after accounting for the £200 you spent
            on the option, you made a cool £800 in profit.
          </p>
        </a>
        <a class="panel-block panel">
          <p class="is-medium">
            Using the B+S formula, you could have predicted the value of the option
            a year from now. If the predicted value of the option a year from now was
            lower than the strike price, you wouldn't engage in the contract,
            or you wouldn't exercise this right, although you'd have lost £200.
          </p>
        </a>
        <section class="hero is-info" v-if="success">
          <div class="hero-content clean">
            <h1 class= "is-large white" v-if="success"> Results </h1>
            <h1 class= "is-medium white" v-if="success"> {{ stocks[0].Ticker }}</h1>
            <p class = "is-large slant" v-if="success">
              Your call option is priced at:
              ${{ (Math.round(stocks[0].Call * 1000)/1000) }}
            </p>
            <p class = "is-large slant" v-if="success">
              Your put option is priced at: ${{ (Math.round(stocks[0].Put * 1000))/1000 }}
            </p>
          </div>
        </section>
      </div>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      success: false,
      isActive: false,
      stocks: [],
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
  methods: {
    getStocks() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.stocks = res.data.stocks;
          console.log(res.data);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    addStock(payload) {
      const path = 'http://localhost:5000/';
      axios.post(path, payload)
        .then(() => {
          this.getStocks();
          this.success = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getStocks();
        });
      console.log(payload);
    },
    initForm() {
      this.addStockForm.Ticker = '';
      this.addStockForm.Price = '';
      this.addStockForm.Strike = '';
      this.addStockForm.Time = '';
      this.addStockForm.Interest = '';
      this.addStockForm.Volatility = '';
    },
    onSubmit() {
      const payload = {
        Ticker: this.addStockForm.Ticker,
        Price: this.addStockForm.Price,
        Strike: this.addStockForm.Strike,
        Time: this.addStockForm.Time,
        Interest: this.addStockForm.Interest,
        Volatility: this.addStockForm.Volatility,
      };
      this.addStock(payload);
      this.initForm();
      this.isActive = false;
    },
    show() {
      this.isActive = true;
      this.success = false;
    },
    hide() {
      this.isActive = false;
    },
  },
  created() {
    this.getStocks();
  },
};
</script>
<style>
  .back {
    margin-bottom: 3em;
  }
  .analysebutton {

    margin-top: 1em;
    margin-bottom: 1em;
    display: grid;
  }
  .panel {

    margin-top: 1em;
    margin-bottom: 1em;
  }
  .clean {
    margin: 1em;
  }
  .white {
    color: white;
  }
  .slant {
    font-style: italic;
  }
  .centerheading{
    text-align: center;
    background: #fae1ff;
  }
</style>
