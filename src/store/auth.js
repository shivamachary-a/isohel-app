import firebase from '@/firebase';
import router from '@/router';

const state = {
  user: {},
  isLoggedIn: false,
};

const actions = {

  async login() {
    const provider = new firebase.auth.GoogleAuthProvider();
    await firebase.auth().signInWithPopup(provider);
  },
  async logout() {
    await firebase.auth().signOut();
    console.log('yeet');
  },
  leave() {
    router.push('/');
  },

};

const mutations = {
  setUser(state, user) {
    if (user) {
      state.user = user;
      state.isLoggedIn = true;
    } else {
      state.user = {};
      state.isLoggedIn = false;
    }
  },
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
};
