<template>
    <!-- Modale Fiche Produit (Overlay sombre en arrière-plan) -->
    <div class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black bg-opacity-60 backdrop-blur-sm" style="font-family: 'Nunito', sans-serif;">
      
      <!-- Conteneur principal de la modale -->
      <div class="relative flex flex-col w-full max-w-4xl overflow-hidden bg-white shadow-2xl rounded-2xl md:flex-row">
  
        <!-- Bouton Fermer (Croix) -->
        <button class="absolute p-2 text-gray-500 transition bg-white rounded-full shadow hover:bg-gray-100 hover:text-gray-800 top-4 right-4 z-10">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
          </svg>
        </button>
  
        <!-- Zone Image -->
        <div class="w-full h-64 bg-gray-100 md:w-1/2 md:h-auto">
          <img src="https://www.j2a-jeux-gonflables.fr/wp-content/uploads/2018/03/Chateau-clown-320x182.jpg" alt="Château Clown" class="object-cover w-full h-full" />
        </div>
  
        <!-- Zone Contenu -->
        <div class="flex flex-col justify-between w-full p-6 md:w-1/2 md:p-8">
          
          <!-- En-tête : Catégorie & Titre -->
          <div>
            <span class="px-3 py-1 text-xs font-extrabold tracking-wider text-[#5282bd] uppercase bg-blue-50 rounded-full">
              Châteaux et Toboggans
            </span>
            <h2 class="mt-4 text-3xl font-extrabold text-gray-900">Château Clown</h2>
  
            <!-- Description -->
            <p class="mt-4 text-gray-600 leading-relaxed">
              Un grand classique indémodable ! Ce château gonflable coloré sur le thème du cirque ravira les plus petits comme les plus grands. Idéal pour les anniversaires et les fêtes de village.
            </p>
  
            <!-- Caractéristiques techniques -->
            <div class="grid grid-cols-2 gap-4 mt-6">
              <div class="flex items-center text-sm font-medium text-gray-600">
                <svg class="w-5 h-5 mr-2 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4"></path></svg>
                <span>5m x 4m x 3m</span>
              </div>
              <div class="flex items-center text-sm font-medium text-gray-600">
                <svg class="w-5 h-5 mr-2 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
                <span>10 enfants max</span>
              </div>
            </div>
          </div>
  
          <!-- Bloc Prix & Call-to-Action -->
          <div class="pt-6 mt-8 border-t border-gray-100">
            <div class="flex items-end justify-between mb-5">
              <div>
                <p class="text-sm font-semibold text-gray-500 uppercase">Tarif location / jour</p>
                <p class="text-4xl font-extrabold text-gray-900">120 € <span class="text-lg font-medium text-gray-500">HT</span></p>
              </div>
              
              <!-- Sélecteur de quantité -->
              <div class="flex items-center border-2 border-gray-200 rounded-xl">
                <button class="px-4 py-2 font-bold text-gray-500 transition hover:bg-gray-100 rounded-l-xl">-</button>
                <input type="text" value="1" class="w-12 text-lg font-bold text-center text-gray-800 outline-none" readonly />
                <button class="px-4 py-2 font-bold text-gray-500 transition hover:bg-gray-100 rounded-r-xl">+</button>
              </div>
            </div>
  
            <!-- Bouton d'ajout -->
            <button class="flex items-center justify-center w-full py-4 text-lg font-extrabold text-white transition-all transform bg-[#F15F26] rounded-xl hover:bg-[#d9531e] hover:-translate-y-0.5 shadow-lg shadow-orange-500/30">
              <svg class="w-6 h-6 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
              Ajouter au devis
            </button>
          </div>
  
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  // Tu pourras ajouter ici tes props (le jeu sélectionné) et tes événements (fermeture de la modale, ajout au panier) par la suite.
  </script>