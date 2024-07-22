<template>
    <div class="flex flex-col">
      <div class="-m-1.5 overflow-x-auto">
        <div class="p-1.5 min-w-full inline-block align-middle">
          <div class="border rounded-lg shadow overflow-hidden">
            <table class="min-w-full divide-y divide-gray-200">
              <thead class="bg-gray-50">
                <tr>
                  <th scope="col" class="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase">Name</th>
                  <th scope="col" class="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase">Books Taken</th>
                  <th scope="col" class="px-6 py-3 text-end text-xs font-medium text-gray-500 uppercase">Action</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-200">
                <tr v-for="reader in readers" :key="reader.id">
                  <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-800">{{ reader.name }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-800">
                    <ul class="list-disc pl-5">
                      <li v-for="book in reader.books" :key="book.id" class="mb-2">
                        <a @click="viewBook(book.id)" href="#" class="text-blue-600 hover:text-blue-800">
                          {{ book.title }}
                        </a>
                      </li>
                    </ul>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-end text-sm font-medium">
                    <button @click="viewReader(reader.id)" type="button" class="inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent text-blue-600 hover:text-blue-800 focus:outline-none focus:text-blue-800 disabled:opacity-50 disabled:pointer-events-none">View</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
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
      },
      viewBook(bookId) {
        this.$router.push(`/books/${bookId}`);
      }
    },
    created() {
      this.fetchReaders();
    }
  };
  </script>
  
  