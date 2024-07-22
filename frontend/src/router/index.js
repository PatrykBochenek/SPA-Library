import { createRouter, createWebHistory } from 'vue-router';
import BookList from '@/components/BookList.vue';
import ReaderList from '@/components/ReaderList.vue';
import BookDetail from '@/components/BookDetail.vue';
import ReaderDetail from '@/components/ReaderDetail.vue';

const routes = [
  {
    path: '/',
    name: 'BookList',
    component: BookList
  },
  {
    path: '/readers',
    name: 'ReaderList',
    component: ReaderList
  },
  {
    path: '/books/:id',
    name: 'BookDetail',
    component: BookDetail
  },
  {
    path: '/readers/:id',
    name: 'ReaderDetail',
    component: ReaderDetail
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
