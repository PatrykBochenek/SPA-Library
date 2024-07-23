<template>
  <div class="flex flex-col">
    <div class="-m-1.5 overflow-x-auto">
      <div class="p-1.5 min-w-full inline-block align-middle">
        <div class="border rounded-lg shadow overflow-hidden">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th
                  scope="col"
                  class="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase"
                >
                  Title
                </th>
                <th
                  scope="col"
                  class="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase"
                >
                  Author
                </th>
                <th
                  scope="col"
                  class="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase"
                >
                  Availability
                </th>
                <th
                  scope="col"
                  class="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase"
                >
                  Taken Out By
                </th>
                <th
                  scope="col"
                  class="px-6 py-3 text-end text-xs font-medium text-gray-500 uppercase"
                >
                  Action
                </th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200">
              <tr v-for="book in books" :key="book.id">
                <td
                  class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-800"
                >
                  {{ book.title }}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-800">
                  {{ book.author }}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-800">
                  {{ book.is_available ? "Available" : "Checked Out" }}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-800">
                  <span v-if="book.readers.length > 0">
                    <router-link
                      :to="'/readers/' + book.readers[0].id"
                      class="text-blue-600 hover:text-blue-800"
                    >
                      {{ book.readers[0].name }}
                    </router-link>
                  </span>
                  <span v-else> N/A </span>
                </td>

                <td
                  class="px-6 py-4 whitespace-nowrap text-end text-sm font-medium"
                >
                  <router-link
                    :to="'/books/' + book.id"
                    class="inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent text-blue-600 hover:text-blue-800 focus:outline-none focus:text-blue-800"
                  >
                    View
                  </router-link>
                </td>
              </tr>
              <tr v-if="books.length === 0">
                <td
                  colspan="4"
                  class="px-6 py-4 whitespace-nowrap text-center text-sm text-gray-800"
                >
                  No books available.
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
import axios from "axios";

const axiosInstance = axios.create({
  baseURL: "http://localhost:8000/api",
  timeout: 1000,
});

export default {
  name: "BookList",
  data() {
    return {
      books: [],
    };
  },
  methods: {
    async fetchBooks() {
      try {
        const response = await axiosInstance.get("/books/");
        this.books = response.data;
      } catch (error) {
        console.error("Error fetching books:", error);
      }
    },
  },
  created() {
    this.fetchBooks();
  },
};
</script>

<style scoped>
.container {
  max-width: 800px;
}
</style>
