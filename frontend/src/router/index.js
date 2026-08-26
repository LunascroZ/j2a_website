import { createRouter, createWebHistory } from 'vue-router';
import Catalog from '@/views/Catalog.vue';

const routes = [
  {
    path: '/',
    name: 'catalog',
    component: Catalog
  },
  {
    path: '/devis',
    name: 'checkout',
    component: () => import('@/views/Checkout.vue')
  },
  // route dynamique pour la fiche d'un jeu specifique
  {
    path: '/jeu/:id',
    name: 'game-detail',
    component: () => import('@/views/GameDetail.vue')
  },
  // routes pour les pages statiques
  {
    path: '/prestations',
    name: 'prestations',
    component: () => import('@/views/Prestations.vue')
  },
  {
    path: '/contact',
    name: 'contact',
    component: () => import('@/views/Contact.vue')
  },
  {
    path: '/a-propos',
    name: 'about',
    component: () => import('@/views/About.vue')
  }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  // remonte en haut de page a chaque changement de route
  scrollBehavior() {
    return { top: 0 };
  }
});

export default router;