<template>
    <div class="container mx-auto p-4" v-if="book">
      <h1 class="text-2xl font-bold mb-4">{{ book.title }}</h1>
      <p class="mb-2"><strong>Author:</strong> {{ book.author }}</p>
      <p class="mb-4"><strong>Status:</strong> {{ book.is_available ? 'Available' : 'Checked out' }}</p>
      <p v-if="book.expiration_date"><strong>Expiration Date:</strong> {{ new Date(book.expiration_date).toLocaleDateString() }}</p>
  
      <h2 class="text-xl font-semibold mb-2">Readers Who Have Taken Out This Book:</h2>
      <ul class="list-disc pl-5 mb-4">
        <li v-for="reader in book.readers" :key="reader.id">
          <router-link :to="'/readers/' + reader.id">{{ reader.name }}</router-link>
        </li>
        <li v-if="book.readers.length === 0">No readers yet.</li>
      </ul>
  
      <div v-if="book.is_available">
        <h2 class="text-xl font-semibold mb-2">Check Out Book</h2>
        <form @submit.prevent="checkoutBook">
          <div class="mb-4">
            <label for="reader_id" class="block text-gray-700">Select Reader:</label>
            <select v-model="selectedReader" id="reader_id" class="form-select mt-1 block w-full">
              <option v-for="reader in readers" :key="reader.id" :value="reader.id">
                {{ reader.name }}
              </option>
            </select>
          </div>
          <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded">Check Out</button>
        </form>
      </div>
  
      <div v-else>
        <h2 class="text-xl font-semibold mb-2">Uncheck Out Book</h2>
        <button @click="uncheckoutBook" class="bg-red-500 text-white px-4 py-2 rounded">Uncheck Out</button>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        book: null,
        readers: [],
        selectedReader: null,
      };
    },
    async created() {
      await this.fetchBook();
      await this.fetchReaders();
    },
    methods: {
      async fetchBook() {
        try {
          const response = await axios.get(`http://localhost:8000/api/books/${this.$route.params.id}/`);
          this.book = response.data;
        } catch (error) {
          console.error('Error fetching book:', error);
          this.book = {};
        }
      },
      async fetchReaders() {
        try {
          const response = await axios.get('http://localhost:8000/api/readers/');
          this.readers = response.data;
        } catch (error) {
          console.error('Error fetching readers:', error);
        }
      },
      async checkoutBook() {
        try {
          await axios.post(`http://localhost:8000/api/books/${this.book.id}/checkout/`, {
            reader_id: this.selectedReader
          });
          await this.fetchBook(); 
        } catch (error) {
          console.error('Error checking out book:', error);
        }
      },
      async uncheckoutBook() {
        try {
          await axios.post(`http://localhost:8000/api/books/${this.book.id}/uncheckout/`);
          await this.fetchBook(); 
        } catch (error) {
          console.error('Error unchecking out book:', error);
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
  