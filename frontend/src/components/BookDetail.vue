<template>
    <div>
      <h1 class="text-2xl font-bold mb-4">Book Detail</h1>
      <div v-if="book">
        <h2 class="text-xl font-semibold">{{ book.title }}</h2>
        <p class="mt-2">Author: {{ book.author }}</p>
        <p class="mt-2">Description: {{ book.description }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  const axiosInstance = axios.create({
    baseURL: 'http://localhost:8000/api',
    timeout: 1000,
  });
  
  export default {
    name: 'BookDetail',
    data() {
      return {
        book: null,
      };
    },
    methods: {
      async fetchBook() {
        try {
          const response = await axiosInstance.get(`/books/${this.$route.params.id}/`);
          this.book = response.data;
        } catch (error) {
          console.error('Error fetching book:', error);
        }
      }
    },
    created() {
      this.fetchBook();
    }
  };
  </script>
  