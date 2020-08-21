import router from '@/router';

const actions = {

  goToDash() {
    router.push('/dash');
  },

  goToAnalysis() {
    router.push('/analysis');
  },
  goToPort() {
    console.log('yeeto');
    router.push('/port');
  },
  goToAcc() {
    console.log('yeeto');
    router.push('/account');
  },
  goToBS() {
    console.log('yeeto');
    router.push('/BlackScholes');
  },
  goToVol() {
    router.push('/volatility');
  },
  goToWatch() {
    router.push('/watchlist');
  },
  goToNews() {
    router.push('/news');
  },
  goToPred() {
    router.push('/pred');
  },
};

export default {
  namespaced: true,
  actions,
};
