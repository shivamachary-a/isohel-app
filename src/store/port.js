import Vuex from 'vuex';

import { firestoreAction } from 'vuexfire';

import { firestore } from 'firebase';
import db from '../db';
import firebase from '../firebase';
import auth from './auth';

export default {
  namespaced: true,
  state: {
    portfolio: [],
  },
  computed: Vuex.mapState('auth', ['user', 'isLoggedIn']),
  actions: {

    bindPortfolios: firestoreAction(({ bindFirestoreRef }) => {
      console.log(auth.state.user['id']);
      bindFirestoreRef('portfolio', db.collection('users').doc(auth.state.user['id']).collection('stocks'));
    }),
    addToPortfolio: async function (tick) {
      const yonk = tick;
      const newStockRef = db.collection('users').doc(auth.state.user['id']).collection('stocks');
      console.log(yonk);
      const res = await newStockRef.add({
        Ticker: yonk,
      });
    },
    deleteFromPortfolio: function (id) {
     const res = db.collection('users').doc(auth.state.user['id']).collection('stocks').doc(id).delete();
    },
  },
};
