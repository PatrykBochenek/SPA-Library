<template>
    <div class="max-w-[85rem] px-4 py-10 sm:px-6 lg:px-8 lg:py-14 mx-auto" v-if="book">
      <div class="bg-white p-6 rounded-lg shadow-lg">
        <h1 class="text-2xl font-bold mb-4">{{ book.title }}</h1>
        <p class="mb-2"><strong>Author:</strong> {{ book.author }}</p>
        <p class="mb-4">
          <strong>Status:</strong>
          <span :class="book.is_available ? 'text-green-600' : 'text-red-600'">{{ book.is_available ? 'Available' : 'Checked out' }}</span>
        </p>
        <p v-if="book.expiration_date"><strong>Expiration Date:</strong> {{ new Date(book.expiration_date).toLocaleDateString() }}</p>

        <h2 class="text-xl font-semibold mt-6 mb-2">Readers Who Have Taken Out This Book:</h2>
        <ul class="list-disc pl-5 mb-4">
          <li v-for="reader in book.readers" :key="reader.id">
            <router-link :to="'/readers/' + reader.id" class="text-blue-600 hover:text-blue-800">{{ reader.name }}</router-link>
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
            <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Check Out</button>
          </form>
        </div>
    
        <div v-else>
          <h2 class="text-xl font-semibold mb-2">Uncheck Out Book</h2>
          <button @click="uncheckoutBook" class="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600">Uncheck Out</button>
        </div>
    
        <div v-if="!book.is_available && !book.requested_by">
          <h2 class="text-xl font-semibold mb-2">Request Book</h2>
          <form @submit.prevent="requestBook">
            <div class="mb-4">
              <label for="request_reader_id" class="block text-gray-700">Select Reader:</label>
              <select v-model="requestReader" id="request_reader_id" class="form-select mt-1 block w-full">
                <option v-for="reader in readers" :key="reader.id" :value="reader.id">
                  {{ reader.name }}
                </option>
              </select>
            </div>
            <button type="submit" class="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">Request Book</button>
          </form>
        </div>
    
        <div v-if="book.requested_by">
          <h2 class="text-xl font-semibold mb-2">Book Requested By</h2>
          <p>{{ book.requested_by }}</p>
        </div>
      </div>
    </div>
    <div v-else class="text-center mt-10">
      <p>Loading book details...</p>
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
        requestReader: null,
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
      },
      async requestBook() {
        try {
          await axios.post(`http://localhost:8000/api/books/${this.book.id}/request/`, {
            reader_id: this.requestReader
          });
          await this.fetchBook(); 
        } catch (error) {
          console.error('Error requesting book:', error);
        }
      }
    }
  };
  </script>
    
  <style scoped>
  .container {
    max-width: 800px;
  }
  
  .form-select {
    border: 1px solid #d1d5db;
    border-radius: 0.375rem;
    padding: 0.5rem 0.75rem;
  }
  
  button {
    transition: background-color 0.3s;
  }
  </style>
  