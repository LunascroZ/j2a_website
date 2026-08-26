<template>
  <div class="min-h-screen flex flex-col bg-j2aLightBlue text-gray-800">
    
    <!-- HEADER -->
    <header class="bg-j2aBlue text-white shadow-lg sticky top-0 z-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex justify-between items-center">
        <div class="flex items-center gap-4">
          <div class="text-3xl font-extrabold tracking-tight text-j2aOrange drop-shadow-md">J2A</div>
          <h1 class="text-xl font-bold hidden sm:block">Location de jeux gonflables</h1>
        </div>
        
        <div class="flex-1 max-w-lg mx-8">
          <input type="text" v-model="searchQuery" placeholder="Rechercher un château, un jeu..." 
                 class="w-full px-4 py-2 rounded-full text-gray-900 focus:outline-none focus:ring-4 focus:ring-j2aOrange transition">
        </div>

        <button ref="cartButtonRef" @click="cartStore.toggleCart()" 
                :class="{ 'scale-110 ring-4 ring-j2aOrange': isBouncing }"
                class="relative bg-white text-j2aBlue px-4 py-2 rounded-full font-bold hover:bg-gray-100 transition-all duration-300 shadow-md">
          Mon Devis
          <span v-if="cartStore.itemCount > 0" class="absolute -top-2 -right-2 bg-j2aOrange text-white text-xs font-bold px-2 py-1 rounded-full">
            {{ cartStore.itemCount }}
          </span>
        </button>
      </div>
    </header>

    <main class="flex-1 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 flex gap-8 w-full">
      
      <!-- SIDEBAR -->
      <aside class="w-64 flex-shrink-0 hidden md:block">
        <div class="bg-white p-6 rounded-2xl card-shadow sticky top-24">
          <h2 class="text-lg font-extrabold text-j2aBlue mb-4 uppercase tracking-wider">Catégories</h2>
          <div class="space-y-3">
            <label v-for="category in categoriesList" :key="category" class="flex items-center cursor-pointer group">
              <input type="radio" :value="category" v-model="selectedCategory" class="form-radio text-j2aOrange focus:ring-j2aOrange w-5 h-5">
              <span class="ml-3 text-gray-700 group-hover:text-j2aOrange font-semibold transition">{{ category }}</span>
            </label>
          </div>
          <button v-if="selectedCategory" @click="selectedCategory = ''" class="mt-6 text-sm text-red-500 hover:text-red-700 font-bold underline">
            Réinitialiser les filtres
          </button>
        </div>
      </aside>

      <!-- GRILLE DES JEUX -->
      <section class="flex-1">
        <div v-if="filteredGames.length === 0" class="text-center py-12 text-gray-500 font-bold text-xl">
          Aucun jeu ne correspond à votre recherche.
        </div>
        
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <div v-for="game in filteredGames" :key="game.id" class="bg-white rounded-2xl overflow-hidden card-shadow hover:scale-105 transition duration-300 border-2 border-transparent hover:border-j2aOrange flex flex-col">
            
            <!-- Lien cliquable vers la page de détails du jeu -->
            <router-link :to="`/jeu/${game.id}`" class="cursor-pointer block group">
              <div class="h-48 bg-blue-100 flex items-center justify-center text-blue-300 font-bold text-2xl relative overflow-hidden">
                <span class="group-hover:scale-110 transition duration-300">[Photo {{ game.nom }}]</span>
                <span v-if="game.prix_1_jour === 0" class="absolute top-2 right-2 bg-gray-800 text-white text-xs font-bold px-3 py-1 rounded-full opacity-80">
                  Sur devis
                </span>
              </div>
              
              <div class="p-5 pb-2">
                <h3 class="text-xl font-extrabold text-j2aBlue mb-1 group-hover:text-j2aOrange transition">{{ game.nom }}</h3>
                <p class="text-sm text-gray-500 font-semibold">{{ game.categories[0] }}</p>
              </div>
            </router-link>

            <div class="p-5 pt-0 flex flex-col flex-1">
              <div class="mt-auto pt-4">
                <div v-if="game.prix_1_jour > 0" class="mb-3">
                  <div class="text-sm"><span class="font-bold text-gray-700">1 Jour :</span> {{ game.prix_1_jour }} € HT</div>
                  <div class="text-sm"><span class="font-bold text-gray-700">2 Jours :</span> {{ game.prix_2_jours }} € HT</div>
                </div>
                <div v-else class="mb-3 text-j2aOrange font-bold text-sm h-10 flex items-center">
                  Tarif sur demande spécifique
                </div>
                
                <button @click="addToCart(game, $event)" class="w-full bg-j2aOrange hover:bg-j2aOrangeHover text-white font-bold py-2 px-4 rounded-xl shadow-md transition transform active:scale-95">
                  Ajouter au devis
                </button>
              </div>
            </div>

          </div>
        </div>
      </section>
    </main>

    <!-- PANIER VOLANT (TIROIR LATÉRAL) -->
    <div v-if="cartStore.isOpen" class="fixed inset-0 z-50 overflow-hidden">
      <div class="absolute inset-0 bg-gray-900 bg-opacity-50 transition-opacity" @click="cartStore.closeCart()"></div>
      
      <div class="fixed inset-y-0 right-0 max-w-md w-full flex">
        <div class="w-full bg-white shadow-2xl flex flex-col">
          <div class="px-6 py-4 bg-j2aBlue text-white flex items-center justify-between">
            <h2 class="text-xl font-extrabold">Votre demande de devis</h2>
            <button @click="cartStore.closeCart()" class="text-white hover:text-gray-300 text-2xl font-bold">&times;</button>
          </div>

          <div class="flex-1 flex flex-col overflow-y-auto p-6">
            <!-- Si le panier est vide -->
            <div v-if="cartStore.itemCount === 0" class="text-center text-gray-500 font-bold mt-10">
              Votre sélection est vide pour le moment.
            </div>
            
            <!-- Liste propre des articles du panier -->
            <ul v-else class="space-y-4 mb-auto">
              <li v-for="(item, index) in cartStore.items" :key="index" class="flex justify-between items-center bg-j2aLightBlue p-3 rounded-xl border border-blue-100">
                <div>
                  <div class="font-bold text-j2aBlue">{{ item.nom }}</div>
                  <div class="text-sm text-gray-600" v-if="item.prix_1_jour > 0">À partir de {{ item.prix_1_jour }} €</div>
                  <div class="text-sm text-j2aOrange font-semibold" v-else>Prix sur mesure</div>
                </div>
                <button @click="cartStore.removeItem(index)" class="text-red-500 hover:text-red-700 font-bold px-2 py-1 bg-white rounded-lg shadow-sm">
                  Retirer
                </button>
              </li>
            </ul>

            <!-- Bouton de redirection vers le formulaire de devis -->
            <div v-if="cartStore.itemCount > 0" class="border-t-2 border-dashed border-gray-200 pt-6 mt-6">
              <div class="flex justify-between items-center mb-4">
                <span class="font-bold text-gray-700">Total articles :</span>
                <span class="font-extrabold text-j2aBlue text-lg">{{ cartStore.itemCount }}</span>
              </div>
              <button @click="goToCheckout" class="w-full bg-j2aOrange hover:bg-j2aOrangeHover text-white font-extrabold py-3 px-4 rounded-xl shadow-lg transition transform active:scale-95">
                Continuer vers la demande
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Éléments volants pour l'animation d'ajout au panier -->
    <div v-for="item in flyingItems" :key="item.id"
         class="fixed w-6 h-6 bg-j2aOrange rounded-full shadow-lg pointer-events-none z-[100] animate-fly-to-cart"
         :style="{ 
           '--startX': item.startX + 'px', 
           '--startY': item.startY + 'px',
           '--endX': item.endX + 'px',
           '--endY': item.endY + 'px' 
         }">
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { catalogData, categoriesList } from '@/data/catalog.js';
import { useCartStore } from '@/stores/cartStore.js';
import { useRouter } from 'vue-router';

const cartStore = useCartStore();
const router = useRouter();

const searchQuery = ref('');
const selectedCategory = ref('');

const flyingItems = ref([]);
const isBouncing = ref(false);
const cartButtonRef = ref(null);

const filteredGames = computed(() => {
  return catalogData.filter(game => {
    const matchCategory = selectedCategory.value === '' || game.categories.includes(selectedCategory.value);
    const matchSearch = game.nom.toLowerCase().includes(searchQuery.value.toLowerCase());
    return matchCategory && matchSearch;
  });
});

const addToCart = (game, event) => {
  cartStore.addItem(game);

  let destinationX = window.innerWidth - 80;
  let destinationY = 30;
  
  if (cartButtonRef.value) {
    const rect = cartButtonRef.value.getBoundingClientRect();
    destinationX = rect.left + (rect.width / 2) - 12;
    destinationY = rect.top + (rect.height / 2) - 12;
  }

  const id = Date.now();
  flyingItems.value.push({
    id,
    startX: event.clientX - 12,
    startY: event.clientY - 12,
    endX: destinationX,
    endY: destinationY
  });

  isBouncing.value = true;

  setTimeout(() => {
    flyingItems.value = flyingItems.value.filter(item => item.id !== id);
    isBouncing.value = false;
  }, 700);
};

const goToCheckout = () => {
  cartStore.closeCart();
  router.push('/devis');
};
</script>