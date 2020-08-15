import Vuex from 'vuex';

import { firestoreAction } from 'vuexfire';

import { firestore } from 'firebase';
import db from '../db';
import firebase from '../firebase';
import auth from './auth';

export default {
    namespaced: true,
    state: {
        watchlist: [],
    },
    computed: Vuex.mapState('auth', ['user', 'isLoggedIn']),
    actions: {
        bindWatchlist: firestoreAction(({ bindFirestoreRef }) => {
            const user = auth.state.user['id'];
            console.log(user);
            bindFirestoreRef('watchlist', db.collection('users').doc(user).collection('watchlist'));
        }),
        addToWatchlist: async function (tick) {
            const yonk = tick;
            console.log(yonk);
            const newStockRef = db.collection('users').doc(auth.state.user['id']).collection('watchlist');
            const res = await newStockRef.add({
                Ticker: yonk,
              });
        },
        deleteFromWatchlist: function (id) {
            const res = db.collection('users').doc(auth.state.user['id']).collection('watchlist').doc(id).delete();
           },
    },
};
