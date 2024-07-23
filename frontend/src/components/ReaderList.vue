<template>
    <div class="max-w-[85rem] px-4 py-10 sm:px-6 lg:px-8 lg:py-14 mx-auto">

      <div class="max-w-2xl mx-auto text-center mb-10 lg:mb-14">
        <h2 class="text-2xl font-bold md:text-4xl md:leading-tight">Reader List</h2>
        <p class="mt-1 text-gray-600">Browse through our list of readers and their borrowed books.</p>
      </div>

      <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">

        <a
          v-for="reader in readers"
          :key="reader.id"
          @click="viewReader(reader.id)"
          href="#"
          class="block border border-gray-200 rounded-lg hover:shadow-sm focus:outline-none cursor-pointer"
        >
          <div class="relative flex items-center overflow-hidden p-4">

            <img
              class="w-16 h-16 rounded-full border border-gray-200"
              :src="`https://api.dicebear.com/9.x/fun-emoji/svg?seed=${reader.id}`"
              alt="Reader Avatar"
            />
  
            <div class="grow ms-4">
              <div class="flex flex-col justify-center min-h-[4rem]">
                <h3 class="font-semibold text-sm text-gray-800">{{ reader.name }}</h3>
                <div class="mt-1 text-sm text-gray-500">
                  <strong>Books Taken:</strong>
                  <ul class="list-disc pl-5 mt-1">
                    <li v-for="book in reader.books_taken" :key="book.id">
                      <router-link :to="'/books/' + book.id">{{ book.title }}</router-link>
                    </li>
                    <li v-if="reader.books_taken.length === 0">No books taken out yet.</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </a>

        <div v-if="readers.length === 0" class="col-span-full text-center text-gray-600">
          <p>No readers available.</p>
        </div>
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
    name: 'ReaderList',
    data() {
      return {
        readers: [],
      };
    },
    methods: {
      async fetchReaders() {
        try {
          const response = await axiosInstance.get('/readers/');
          this.readers = response.data;
        } catch (error) {
          console.error('Error fetching readers:', error);
        }
      },
      viewReader(readerId) {
        this.$router.push(`/readers/${readerId}`);
      }
    },
    created() {
      this.fetchReaders();
    }
  };
  </script>
  
  <style scoped>
  .container {
    max-width: 800px;
  }
  </style>
  