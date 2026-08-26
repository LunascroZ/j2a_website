import { createRouter, createWebHistory } from 'vue-router';
import Catalog from '@/views/Catalog.vue';

// definition des routes de l'application
const routes = [
  {
    path: '/',
    name: 'catalog',
    component: Catalog
  },
  {
    path: '/devis',
    name: 'checkout',
    // chargement paresseux (lazy loading) pour optimiser les performances au demarrage
    component: () => import('@/views/Checkout.vue')
  }
];

const router = createRouter({
  // utilisation de l'historique html5 pour des urls propres sans le hash (#)
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  // gestion du defilement lors des changements de page
  scrollBehavior() {
    return { top: 0 };
  }
});

export default router;