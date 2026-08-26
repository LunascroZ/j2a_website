<template>
    <div class="min-h-screen bg-gray-50 pb-12">
      
      <!-- en-tete de navigation -->
      <header class="bg-j2aBlue text-white shadow-md">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex justify-between items-center">
          <button @click="router.push('/')" class="text-white hover:text-gray-300 flex items-center transition">
            <svg class="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
            Retour au catalogue
          </button>
          
          <!-- rappel du panier -->
          <button @click="router.push('/devis')" class="bg-j2aOrange px-4 py-2 rounded-full font-bold shadow-md hover:bg-orange-600 transition text-sm">
            Mon devis ({{ cartStore.itemCount }})
          </button>
        </div>
      </header>
  
      <!-- affichage si le jeu n'est pas trouve -->
      <div v-if="!game" class="max-w-7xl mx-auto mt-12 text-center">
        <h2 class="text-2xl font-bold text-gray-700">Jeu introuvable</h2>
        <button @click="router.push('/')" class="mt-4 text-j2aBlue font-bold underline">Retourner à l'accueil</button>
      </div>
  
      <!-- fiche detaillee du jeu -->
      <main v-else class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-8">
        <div class="bg-white rounded-3xl shadow-sm overflow-hidden border border-gray-100 flex flex-col md:flex-row">
          
          <!-- zone image -->
          <div class="md:w-1/2 bg-gray-100 flex items-center justify-center p-8 min-h-[400px]">
            <!-- a remplacer par game.image quand tu auras les vraies photos -->
            <svg class="w-32 h-32 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
            </svg>
          </div>
  
          <!-- zone informations -->
          <div class="md:w-1/2 p-8 lg:p-12 flex flex-col justify-between">
            <div>
              <div class="inline-block px-3 py-1 bg-blue-50 text-j2aBlue text-xs font-bold uppercase tracking-wider rounded-full mb-4">
                {{ game.categories[0] }}
              </div>
              <h1 class="text-4xl font-extrabold text-gray-900 mb-4">{{ game.nom }}</h1>
              
              <p class="text-gray-600 leading-relaxed mb-8">
                Description complète du jeu à intégrer ici. Actuellement, notre base de données ne contient que le nom et le prix, mais il suffira d'ajouter une clé "description" dans le fichier catalog.js pour chaque objet.
              </p>
  
              <div class="grid grid-cols-2 gap-6 mb-8">
                <div class="bg-gray-50 p-4 rounded-2xl border border-gray-100">
                  <span class="block text-xs text-gray-500 uppercase font-bold mb-1">Tarif 1 jour</span>
                  <span class="text-xl font-extrabold text-j2aBlue">{{ game.prix_1_jour > 0 ? game.prix_1_jour + ' €' : 'Sur devis' }}</span>
                </div>
                <div class="bg-gray-50 p-4 rounded-2xl border border-gray-100">
                  <span class="block text-xs text-gray-500 uppercase font-bold mb-1">Tarif 2 jours</span>
                  <span class="text-xl font-extrabold text-j2aBlue">{{ game.prix_2_jours > 0 ? game.prix_2_jours + ' €' : 'Sur devis' }}</span>
                </div>
              </div>
  
              <!-- caracteristiques techniques fictives (a lier au json plus tard) -->
              <ul class="space-y-2 mb-8 text-sm text-gray-600">
                <li class="flex items-center">
                  <svg class="w-5 h-5 text-j2aOrange mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
                  Dimensions : 5m x 4m x 3m
                </li>
                <li class="flex items-center">
                  <svg class="w-5 h-5 text-j2aOrange mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
                  Capacité : 10 enfants simultanément
                </li>
              </ul>
            </div>
  
            <button @click="addToCartAndReturn" class="w-full bg-j2aOrange hover:bg-j2aOrangeHover text-white font-extrabold py-4 rounded-xl shadow-lg transition transform active:scale-95 text-lg">
              Ajouter au devis
            </button>
          </div>
        </div>
      </main>
    </div>
  </template>
  
  <script setup>
  import { computed } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import { useCartStore } from '@/stores/cartStore.js';
  import { catalogData } from '@/data/catalog.js';
  
  const route = useRoute();
  const router = useRouter();
  const cartStore = useCartStore();
  
  // recuperation de l'id depuis l'url et recherche dans le catalogue
  const gameId = parseInt(route.params.id);
  const game = computed(() => catalogData.find(g => g.id === gameId));
  
  // ajoute le jeu au store et redirige vers le catalogue pour continuer les achats
  const addToCartAndReturn = () => {
    if (game.value) {
      cartStore.addItem(game.value);
      router.push('/');
    }
  };
  </script>