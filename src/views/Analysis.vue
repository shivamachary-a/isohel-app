
<template>
    <div>
        <h1 class="title has-text-weight-light">ANALYSIS</h1>
        <article class="panel is-primary">
            <p class="panel-heading has-text-weight-light">
                METHODS
            </p>
            <a class="panel-block">
                <a @click="goToBS()"> Black + Scholes</a>
                <a id="BS" class="infoB button is-small" @click="infoClick(event,'blackscholes')">
                    Quick Info
                </a>
            </a>
            <a class="panel-block">
                <a @click="goToVol()">Volatility</a>
                <a id="VOL" class="infoB button is-small">Quick Info</a>
            </a>
        </article>
        <div class="modal" id="blackscholes">
            <div class="modal-background"></div>
                <div class="modal-card">
                    <div class="modal-card-body">
                        <p class="title">
                            A tool to help price options contracts. Find out more by going to our  Black and Scholes analysis page.
                        </p>
                        <a class="button is-info booton" @click="goToBS()">Here</a>
                        <p></p>
                        <a class="button booton" target="_blank" href="https://www.investopedia.com/terms/b/blackscholes.asp">Or click here to view the Investopedia page</a>
                    </div>
                </div>
            <button class="modal-close is-large" aria-label="close" @click="closeModal(event, 'blackscholes')"></button>
        </div>
    </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';
import router from '@/router';

export default {
    methods: {
        ...mapActions('auth', ['login', 'logout', 'leave']),

        ...mapActions('navigation', ['goToPort', 'goToAnalysis', 'goToDash', 'goToAcc', 'goToBS', 'goToVol']),

        infoClick(event, id) {
            const currentModal = document.getElementById(id);
            currentModal.className += ' is-active';
            console.log('test');
        },
        closeModal(event, id) {
            const currentModal = document.getElementById(id);
            currentModal.className = currentModal.className.replace(' is-active', '');
            console.log('test');
        },
    },
};
</script>

<style>

    .infoB {
        margin-left: 3em;
    }
    .booton {
        margin-top: 1em;
        margin-bottom: 1em;
    }

</style>
