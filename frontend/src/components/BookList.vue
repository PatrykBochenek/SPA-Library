<template>
    <div class="max-w-[85rem] px-4 py-10 sm:px-6 lg:px-8 lg:py-14 mx-auto">

      <div class="max-w-2xl mx-auto text-center mb-10 lg:mb-14">
        <h2 class="text-2xl font-bold md:text-4xl md:leading-tight">Book List</h2>
        <p class="mt-1 text-gray-600">Explore our collection of books and find your next great read.</p>
      </div>

      <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">

        <a
          v-for="book in books"
          :key="book.id"
          :href="'/books/' + book.id"
          class="block border border-gray-200 rounded-lg hover:shadow-sm focus:outline-none"
        >
          <div class="relative flex items-center overflow-hidden">

            <img
              class="w-32 sm:w-48 h-full absolute inset-0 object-cover rounded-s-lg"
              :src="book.cover_image || 'https://images.pexels.com/photos/4238507/pexels-photo-4238507.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'"
              alt="Book Cover"
            />
  
            <div class="grow p-4 ms-32 sm:ms-48">
              <div class="min-h-24 flex flex-col justify-center">
                <h3 class="font-semibold text-sm text-gray-800">{{ book.title }}</h3>
                <p class="mt-1 text-sm text-gray-500">By {{ book.author }}</p>
                <p
                  class="mt-1 text-sm"
                  :class="{
                    'text-green-600': book.is_available,
                    'text-red-600': !book.is_available
                  }"
                >
                  {{ book.is_available ? 'Available' : 'Checked Out' }}
                </p>
              </div>
            </div>
          </div>
        </a>

        <div v-if="books.length === 0" class="col-span-full text-center text-gray-600">
          <p>No books available.</p>
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
      },
    },
    created() {
      this.fetchBooks();
    },
  };
  </script>
 