<template>
    <div class="container mx-auto p-4">

      <div v-if="reader" class="flex items-center gap-x-3">
        <div class="shrink-0">
          <img
            class="shrink-0 size-16 rounded-full"
            :src="`https://api.dicebear.com/9.x/fun-emoji/svg?seed=${reader.id}`"
            alt="Avatar"
          />
        </div>
  
        <div class="grow">
          <h1 class="text-lg font-medium text-gray-800">{{ reader.name }}</h1>
        </div>
      </div>

      <div v-if="reader" class="mt-8">
        <p class="text-sm text-gray-600">
          <strong>Books Taken:</strong>
        </p>
  
        <ul class="list-disc pl-5 mt-2">
          <li v-for="book in reader.books_taken" :key="book.id" class="mb-2">
            <router-link :to="'/books/' + book.id">{{ book.title }}</router-link>
          </li>
          <li v-if="reader.books_taken.length === 0">No books taken out.</li>
        </ul>
      </div>
  
      <div v-if="!reader" class="mt-8">
        <p>Loading reader details...</p>
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
        const readerId = this.$route.params.id;
        console.log(`Fetching reader with ID: ${readerId}`);
        try {
          const response = await axios.get(`http://localhost:8000/api/readers/${readerId}/`);
          console.log('Reader data:', response.data);
          this.reader = response.data;
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
  