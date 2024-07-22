<template>
    <div class="container mx-auto p-4">
      <h1 class="text-2xl font-bold mb-4">Reader Detail</h1>
      <div v-if="reader">
        <h2 class="text-xl font-semibold">{{ reader.name }}</h2>
        <p class="mt-2">Books Taken:</p>
        <ul class="list-disc pl-5">
          <li v-for="book in reader.books_taken" :key="book.id" class="mb-2">
            <router-link :to="'/books/' + book.id">{{ book.title }}</router-link>
          </li>
          <li v-if="reader.books_taken.length === 0">No books taken out.</li>
        </ul>
      </div>
      <div v-else>
        <p>Loading...</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        reader: null,
      };
    },
    async created() {
      await this.fetchReader();
    },
    methods: {
      async fetchReader() {
        try {
          const response = await axios.get(`http://localhost:8000/api/readers/${this.$route.params.id}/`);
          this.reader = response.data;
          console.log(this.reader); // Debug line to check data structure
        } catch (error) {
          console.error('Error fetching reader:', error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .container {
    max-width: 800px;
  }
  </style>
  