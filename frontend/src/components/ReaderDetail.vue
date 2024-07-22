<template>
    <div>
      <h1 class="text-2xl font-bold mb-4">Reader Detail</h1>
      <div v-if="reader">
        <h2 class="text-xl font-semibold">{{ reader.name }}</h2>
        <p class="mt-2">Email: {{ reader.email }}</p>
        <p class="mt-2">Books Taken:</p>
        <ul class="list-disc pl-5">
          <li v-for="book in reader.books" :key="book.id" class="mb-2">
            {{ book.title }}
          </li>
        </ul>
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
    name: 'ReaderDetail',
    data() {
      return {
        reader: null,
      };
    },
    methods: {
      async fetchReader() {
        try {
          const response = await axiosInstance.get(`/readers/${this.$route.params.id}/`);
          this.reader = response.data;
        } catch (error) {
          console.error('Error fetching reader:', error);
        }
      }
    },
    created() {
      this.fetchReader();
    }
  };
  </script>
  

  