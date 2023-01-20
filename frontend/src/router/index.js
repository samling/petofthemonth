import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import RegisterView from '@/views/RegisterView.vue'
import LoginView from '@/views/LoginView.vue'
import DashboardView from '@/views/DashboardView.vue'
import ProfileView from '@/views/ProfileView.vue'
import UsersView from '@/views/UsersView.vue'
import UserView from '@/views/UserView.vue'
import GroupsView from '@/views/GroupsView.vue'
import GroupView from '@/views/GroupView.vue'
import PetsView from '@/views/PetsView.vue'
import PetView from '@/views/PetView.vue'
import EditPetView from '@/views/EditPetView.vue'
import store from '@/store';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView
    },
    {
      path: '/register',
      name: 'Register',
      component: RegisterView
    },
    {
      path: '/login',
      name: 'Login',
      component: LoginView
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: DashboardView,
      meta: { requiresAuth: true }
    },
    {
      path: '/profile',
      name: 'Profile',
      component: ProfileView,
      meta: { requiresAuth: true }
    },
    {
      path: '/about',
      name: 'About',
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
      component: PetsView,
      meta: { requiresAuth: true }
    },
    {
      path: '/pet/:id',
      name: 'Pet',
      component: PetView,
      meta: { requiresAuth: true },
      props: true
    },
    {
      path: '/editpet/:id',
      name: 'EditPet',
      component: EditPetView,
      meta: { requiresAuth: true },
      props: true
    }
  ]
})

router.beforeEach((to, _, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next();
      return;
    }
    next('/login');
  } else {
    next();
  }
});

export default router
