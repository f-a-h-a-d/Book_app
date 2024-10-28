import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/dashboard.vue'
import Login from '../views/testLogin.vue'
import Home from '../views/home.vue'
import Practice from '../views/practice.vue'
import Dispute from '../views/dispute.vue'
import Form from '../views/form.vue'
import ShowBooks from '../views/showbooks.vue'
import AddBook from '../views/addBook.vue'
import AddAuthor from '../views/addAuthor.vue'
import Practice2 from '../views/practice2.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: Home,
    },
    {
      path: '/login',
      component: Login,
      beforeEnter(to, from, next) {
        const isAuthenticated = () => {
          const token = localStorage.getItem('Token'); 
          console.log(token);
          if(token != null)return true;
          else return false;
        };
        
        if (isAuthenticated()) { 
          next('/dashboard');
        } else {
          next();
        }
      }
    },
    {
      path: '/dashboard',
      component: Dashboard,
      beforeEnter(to, from, next) {
        const isAuthenticated = () => {
          const token = localStorage.getItem('Token'); 
          console.log(token);
          if(token != null)return true;
          else return false;
        };
        
        if (isAuthenticated()) { 
          next();
        } else {
          next('/login');
        }
      }
    },
    {
      path: '/practice',
      component: Practice
    },
    {
      path: '/form',
      component: Form

    },
    {
      path: '/showbooks',
      component: ShowBooks
    },
    {
      path: '/logout',
      component: Dispute
    },
    {
      path: '/addBook',
      component: AddBook
    },
    {
      path: '/addAuthor',
      component: AddAuthor
    },
    {
      path: '/practice2',
      component :Practice2
    }
   
  ]
})

export default router
