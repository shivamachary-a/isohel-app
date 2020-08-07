import firebase from 'firebase';
import 'firebase/firestore';

const firebaseConfig = {
  apiKey: 'AIzaSyDdiHzFoaUhdWu_O1BiTg5memQA_dqzyuY',
  authDomain: 'isohel-57a33.firebaseapp.com',
  databaseURL: 'https://isohel-57a33.firebaseio.com',
  projectId: 'isohel-57a33',
  storageBucket: 'isohel-57a33.appspot.com',
  messagingSenderId: '910743560719',
  appId: '1:910743560719:web:a8d8b6efccda002abff97a',
  measurementId: 'G-VE02HBTN4R',
};

firebase.initializeApp(firebaseConfig);

export default firebase;
