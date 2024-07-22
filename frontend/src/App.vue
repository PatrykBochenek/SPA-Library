<template>
  <div id="app">
    <nav class="bg-gray-800 p-4">
      <div class="container mx-auto flex justify-between items-center">
        <a class="text-white text-xl font-bold" href="#">Library App</a>
        <div>
          <router-link class="text-white mx-2" to="/">Books</router-link>
          <router-link class="text-white mx-2" to="/readers">Readers</router-link>
        </div>
      </div>
    </nav>
    <div class="container mx-auto mt-6">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

