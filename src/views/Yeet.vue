<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addMessage() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.data = res.data.cocks;
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
