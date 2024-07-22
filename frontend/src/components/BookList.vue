<template>
    <div>
      <h1 class="text-2xl font-bold mb-4">Book List</h1>
      <ul class="list-disc pl-5">
        <li v-for="book in books" :key="book.id" class="mb-2">
          {{ book.title }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  const axiosInstance = axios.create({
    baseURL: 'http://localhost:8000/api',
    timeout: 1000,
  });
  
  export default {
    name: 'BookList',
    data() {
      return {
        books: [],
      };
    },
    methods: {
      async fetchBooks() {
        try {
          const response = await axiosInstance.get('/books/');
          this.books = response.data;
        } catch (error) {
          console.error('Error fetching books:', error);
        }
      }
    },
    created() {
      this.fetchBooks();
    }
  };
  </script>
  

  