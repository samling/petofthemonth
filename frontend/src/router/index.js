import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import UsersView from '@/views/UsersView.vue'
import UserView from '@/views/UserView.vue'
import GroupsView from '@/views/GroupsView.vue'
import GroupView from '@/views/GroupView.vue'
import PetsView from '@/views/PetsView.vue'
import PetView from '@/views/PetView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: HomeView
    },
    {
      path: '/users',
      name: 'Users',
      component: UsersView
    },
    {
      path: '/user/:id',
      name: 'User',
      component: UserView,
      props: true
    },
    {
      path: '/groups',
      name: 'Groups',
      component: GroupsView
    },
    {
      path: '/group/:id',
      name: 'Group',
      component: GroupView,
      props: true
    },
    {
      path: '/pets',
      name: 'Pets',
      component: PetsView
    },
    {
      path: '/pet/:id',
      name: 'Pet',
      component: PetView,
      props: true
    }
  ]
})

export default router
