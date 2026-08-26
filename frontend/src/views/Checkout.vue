<template>
    <div class="min-h-screen bg-j2aLightBlue text-gray-800 pb-12">
      
      <!-- en-tete -->
      <header class="bg-j2aBlue text-white shadow-md">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center">
          <button @click="router.push('/')" class="text-white hover:text-gray-300 flex items-center transition">
            <svg class="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
            Retour au catalogue
          </button>
        </div>
      </header>
  
      <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-8">
        <h1 class="text-3xl font-extrabold text-j2aBlue mb-8">Finalisation de votre devis</h1>
  
        <!-- affichage si panier vide -->
        <div v-if="cartStore.itemCount === 0" class="bg-white rounded-2xl shadow-sm p-12 text-center border border-gray-100">
          <svg class="w-16 h-16 text-gray-400 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
          <h2 class="text-xl font-bold text-gray-700 mb-4">Votre sélection est vide</h2>
          <button @click="router.push('/')" class="bg-j2aOrange hover:bg-j2aOrangeHover text-white font-bold py-2 px-6 rounded-xl transition">
            Parcourir le catalogue
          </button>
        </div>
  
        <div v-else class="grid grid-cols-1 lg:grid-cols-12 gap-8">
          
          <!-- zone de formulaire principale -->
          <div class="lg:col-span-8 bg-white rounded-2xl shadow-sm p-6 sm:p-8 border border-gray-100">
            <form @submit.prevent="submitOrder" class="space-y-8">
              
              <!-- section coordonnees client -->
              <div>
                <h2 class="text-xl font-bold text-j2aBlue mb-4 border-b pb-2">Vos coordonnées</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label class="block text-sm font-bold text-gray-700 mb-1">Prénom *</label>
                    <input type="text" v-model="form.prenom" required class="w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-j2aOrange outline-none" />
                  </div>
                  <div>
                    <label class="block text-sm font-bold text-gray-700 mb-1">Nom *</label>
                    <input type="text" v-model="form.nom" required class="w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-j2aOrange outline-none" />
                  </div>
                </div>
                <div class="mt-4">
                  <label class="block text-sm font-bold text-gray-700 mb-1">Organisme (optionnel)</label>
                  <input type="text" v-model="form.organisme" placeholder="Entreprise, association, collectivité..." class="w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-j2aOrange outline-none" />
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
                  <div>
                    <label class="block text-sm font-bold text-gray-700 mb-1">Téléphone *</label>
                    <input type="tel" v-model="form.telephone" required class="w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-j2aOrange outline-none" />
                  </div>
                  <div>
                    <label class="block text-sm font-bold text-gray-700 mb-1">Email *</label>
                    <input type="email" v-model="form.email" required class="w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-j2aOrange outline-none" />
                  </div>
                </div>
                
                <!-- autocompletion adresse client -->
                <div class="mt-4 relative">
                  <label class="block text-sm font-bold text-gray-700 mb-1">Votre adresse *</label>
                  <input type="text" v-model="form.adresseClient" @input="searchAddressClient" required placeholder="Commencez à taper votre adresse..." class="w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-j2aOrange outline-none" />
                  <ul v-if="suggestionsClient.length > 0" class="absolute z-10 w-full mt-1 bg-white border border-gray-200 rounded-xl shadow-lg overflow-hidden">
                    <li v-for="suggestion in suggestionsClient" :key="suggestion.place_id" @click="selectAddressClient(suggestion)" class="p-3 hover:bg-blue-50 cursor-pointer text-sm text-gray-700 transition border-b border-gray-100 last:border-0">
                      {{ suggestion.display_name }}
                    </li>
                  </ul>
                </div>
              </div>
    
              <!-- section details evenement -->
              <div>
                <h2 class="text-xl font-bold text-j2aBlue mb-4 border-b pb-2">L'événement</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label class="block text-sm font-bold text-gray-700 mb-1">Type d'événement *</label>
                    <select v-model="form.typeEvenement" required class="w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-j2aOrange outline-none bg-white">
                      <option value="" disabled>Sélectionnez un type</option>
                      <option value="Fête de village ou de quartier">Fête de village ou de quartier</option>
                      <option value="Événement privé">Événement privé (mariage, cousinade...)</option>
                      <option value="Centre aéré">Centre aéré, centre de loisir...</option>
                      <option value="Kermesse">Kermesse, foire, salon...</option>
                      <option value="Événement interne">Événement interne (Ets ou collectivité)</option>
                      <option value="Porte ouverte">Porte ouverte commerciale</option>
                      <option value="Autre">Autre type d'événement</option>
                    </select>
                  </div>
                  
                  <!-- autocompletion lieu evenement -->
                  <div class="relative">
                    <label class="block text-sm font-bold text-gray-700 mb-1">Lieu de l'événement *</label>
                    <input type="text" v-model="form.lieuEvenement" @input="searchAddressLieu" placeholder="Commencez à taper la ville ou l'adresse..." required class="w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-j2aOrange outline-none" />
                    <ul v-if="suggestionsLieu.length > 0" class="absolute z-10 w-full mt-1 bg-white border border-gray-200 rounded-xl shadow-lg overflow-hidden">
                      <li v-for="suggestion in suggestionsLieu" :key="suggestion.place_id" @click="selectAddressLieu(suggestion)" class="p-3 hover:bg-blue-50 cursor-pointer text-sm text-gray-700 transition border-b border-gray-100 last:border-0">
                        {{ suggestion.display_name }}
                      </li>
                    </ul>
                  </div>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
                  <div class="flex gap-2">
                    <div class="w-1/2">
                      <label class="block text-sm font-bold text-gray-700 mb-1">Date début *</label>
                      <input type="date" v-model="form.dateDebut" required class="w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-j2aOrange outline-none" />
                    </div>
                    <div class="w-1/2">
                      <label class="block text-sm font-bold text-gray-700 mb-1">Heure de début *</label>
                      <input type="time" v-model="form.heureDebut" required class="w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-j2aOrange outline-none" />
                    </div>
                  </div>
                  <div class="flex gap-2">
                    <div class="w-1/2">
                      <label class="block text-sm font-bold text-gray-700 mb-1">Date fin *</label>
                      <input type="date" v-model="form.dateFin" required class="w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-j2aOrange outline-none" />
                    </div>
                    <div class="w-1/2">
                      <label class="block text-sm font-bold text-gray-700 mb-1">Heure de fin *</label>
                      <input type="time" v-model="form.heureFin" required class="w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-j2aOrange outline-none" />
                    </div>
                  </div>
                </div>
    
                <div class="mt-4">
                  <label class="block text-sm font-bold text-gray-700 mb-1">Détails sur l'événement (optionnel)</label>
                  <textarea v-model="form.detailEvenement" rows="2" class="w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-j2aOrange outline-none resize-none"></textarea>
                </div>
              </div>
    
              <!-- section logistique et terrain -->
              <div>
                <h2 class="text-xl font-bold text-j2aBlue mb-4 border-b pb-2">Logistique et Terrain</h2>
                
                <div class="mb-4">
                  <label class="block text-sm font-bold text-gray-700 mb-2">Type de sol *</label>
                  <div class="grid grid-cols-2 md:grid-cols-3 gap-3">
                    <label v-for="sol in ['Herbe', 'Bitume', 'Gravier', 'Carrelage', 'Parquet bois', 'Sable', 'Autre']" :key="sol" class="flex items-center p-3 border border-gray-200 rounded-xl cursor-pointer hover:bg-gray-50 transition">
                      <input type="radio" :value="sol" v-model="form.typeSol" required class="text-j2aOrange focus:ring-j2aOrange w-4 h-4">
                      <span class="ml-2 text-sm font-medium">{{ sol }}</span>
                    </label>
                  </div>
                  <div v-if="form.typeSol === 'Autre'" class="mt-3">
                    <input type="text" v-model="form.autreSol" placeholder="Précisez le type de sol" required class="w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-j2aOrange outline-none" />
                  </div>
                </div>
    
                <div class="mb-4">
                  <label class="block text-sm font-bold text-gray-700 mb-2">Choix de livraison *</label>
                  <div class="space-y-2">
                    <label class="flex items-start p-3 border border-gray-200 rounded-xl cursor-pointer hover:bg-gray-50 transition">
                      <input type="radio" value="J2A" v-model="form.livraison" required class="mt-1 text-j2aOrange focus:ring-j2aOrange w-4 h-4">
                      <span class="ml-2 text-sm font-medium">Par J2A sur le lieu de l'événement (transport et installation en supplément)</span>
                    </label>
                    <label class="flex items-start p-3 border border-gray-200 rounded-xl cursor-pointer hover:bg-gray-50 transition">
                      <input type="radio" value="Retrait" v-model="form.livraison" class="mt-1 text-j2aOrange focus:ring-j2aOrange w-4 h-4">
                      <span class="ml-2 text-sm font-medium">Pas de livraison, je viens chercher les jeux à Coutiches (Particuliers : -20%)</span>
                    </label>
                  </div>
                </div>
    
                <div class="mt-4">
                  <label class="block text-sm font-bold text-gray-700 mb-1">Note sur la livraison (optionnel)</label>
                  <textarea v-model="form.noteLivraison" placeholder="Accessibilité, code portail, étage..." rows="2" class="w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-j2aOrange outline-none resize-none"></textarea>
                </div>
              </div>
    
              <!-- section prestations -->
              <div>
                <h2 class="text-xl font-bold text-j2aBlue mb-4 border-b pb-2">Prestations souhaitées</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-4">
                  <label v-for="presta in ['Livraison aller', 'Installation', 'Surveillance', 'Désinstallation', 'Livraison retour', 'Pas de prestation souhaitée']" :key="presta" class="flex items-center p-3 border border-gray-200 rounded-xl cursor-pointer hover:bg-gray-50 transition">
                    <input type="checkbox" :value="presta" v-model="form.prestations" class="rounded text-j2aOrange focus:ring-j2aOrange w-4 h-4">
                    <span class="ml-2 text-sm font-medium">{{ presta }}</span>
                  </label>
                </div>
    
                <div v-if="form.prestations.includes('Surveillance')" class="mt-4 p-4 bg-orange-50 rounded-xl border border-orange-100">
                  <label class="block text-sm font-bold text-j2aOrange mb-2">Pour quels jeux souhaitez-vous la surveillance ? *</label>
                  <div class="space-y-2">
                    <label v-for="item in cartStore.items" :key="item.id" class="flex items-center cursor-pointer">
                      <input type="checkbox" :value="item.nom" v-model="form.surveillanceJeux" class="rounded text-j2aOrange focus:ring-j2aOrange w-4 h-4">
                      <span class="ml-2 text-sm text-gray-700">{{ item.nom }}</span>
                    </label>
                  </div>
                </div>
    
                <div class="mt-4">
                  <label class="block text-sm font-bold text-gray-700 mb-1">Détail sur les prestations (optionnel)</label>
                  <textarea v-model="form.detailPrestations" rows="2" class="w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-j2aOrange outline-none resize-none"></textarea>
                </div>
              </div>
    
              <!-- section budget -->
              <div>
                <h2 class="text-xl font-bold text-j2aBlue mb-4 border-b pb-2">Budget</h2>
                <label class="block text-sm font-bold text-gray-700 mb-1">Budget estimatif *</label>
                <select v-model="form.budget" required class="w-full md:w-1/2 p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-j2aOrange outline-none bg-white">
                  <option value="" disabled>Sélectionnez une tranche</option>
                  <option value="- de 200 €">- de 200 €</option>
                  <option value="de 200 à 400 €">de 200 à 400 €</option>
                  <option value="de 400 à 800 €">de 400 à 800 €</option>
                  <option value="de 800 à 2 000 €">de 800 à 2 000 €</option>
                  <option value="+ de 2 000 €">+ de 2 000 €</option>
                </select>
              </div>
    
              <button type="submit" class="w-full bg-j2aBlue hover:bg-blue-900 text-white font-extrabold py-4 rounded-xl shadow-md transition transform active:scale-95 text-lg">
                Envoyer la demande de devis
              </button>
            </form>
          </div>
    
          <!-- zone recapitulatif panier avec calcul de prorata dynamique -->
          <aside class="lg:col-span-4">
            <div class="bg-white rounded-2xl shadow-sm p-6 border border-gray-100 sticky top-6">
              <h2 class="text-xl font-bold text-gray-900 mb-6">Votre sélection</h2>
              
              <ul class="space-y-4 mb-6">
                <li v-for="(item, index) in cartStore.items" :key="index" class="flex justify-between items-start pb-4 border-b border-gray-100 last:border-0 last:pb-0">
                  <div>
                    <div class="font-bold text-j2aBlue">{{ item.nom }}</div>
                    <div class="text-xs text-gray-500 uppercase font-semibold tracking-wide">{{ item.categories[0] }}</div>
                  </div>
                  <div class="text-right ml-4 flex flex-col items-end">
                    <!-- affichage du prix en fonction du nombre de jours calcules -->
                    <div class="font-semibold text-gray-800" v-if="item.prix_1_jour > 0">{{ getItemPrice(item, numberOfDays) }} €</div>
                    <div class="text-sm font-semibold text-j2aOrange" v-else>Sur devis</div>
                    
                    <button @click="cartStore.removeItem(index)" class="text-xs text-red-500 hover:text-red-700 mt-2 font-bold flex items-center transition">
                      Retirer
                    </button>
                  </div>
                </li>
              </ul>
    
              <div class="pt-4 border-t-2 border-dashed border-gray-200">
                <div class="flex justify-between items-center mb-2">
                  <span class="text-gray-600 font-bold">Total estimé HT</span>
                  <div class="text-right">
                    <div class="text-2xl font-extrabold text-j2aOrange">{{ estimatedTotal }}</div>
                    <div class="text-xs font-semibold text-gray-500" v-if="numberOfDays > 1">pour {{ numberOfDays }} jours</div>
                  </div>
                </div>
                <p class="text-xs text-gray-400 mt-2 leading-relaxed">
                  Ce montant est une estimation calculée sur la durée renseignée. Un devis finalisé vous sera communiqué par email.
                </p>
              </div>
            </div>
          </aside>
    
        </div>
      </main>
    </div>
  </template>
    
  <script setup>
  import { ref, reactive, computed } from 'vue';
  import { useRouter } from 'vue-router';
  import { useCartStore } from '@/stores/cartStore.js';
  
  const router = useRouter();
  const cartStore = useCartStore();
  
  // etats pour l'autocompletion
  const suggestionsClient = ref([]);
  const suggestionsLieu = ref([]);
  
  // initialisation du formulaire
  const form = reactive({
    prenom: '',
    nom: '',
    organisme: '',
    telephone: '',
    email: '',
    adresseClient: '',
    typeEvenement: '',
    lieuEvenement: '',
    dateDebut: '',
    heureDebut: '',
    dateFin: '',
    heureFin: '',
    detailEvenement: '',
    typeSol: '',
    autreSol: '',
    livraison: '',
    noteLivraison: '',
    prestations: [],
    surveillanceJeux: [],
    detailPrestations: '',
    budget: ''
  });
  
  // calcul du nombre de jours de location
  const numberOfDays = computed(() => {
    if (!form.dateDebut || !form.dateFin) return 1;
    
    const debut = new Date(form.dateDebut);
    const fin = new Date(form.dateFin);
    
    // si la date de fin est anterieure a la date de debut, on force a 1 jour par defaut
    if (fin < debut) return 1;
    
    const diffTime = fin.getTime() - debut.getTime();
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    
    // on ajoute +1 car meme date debut/fin = 1 jour de location
    return diffDays + 1;
  });
  
  // calcul dynamique du prix par article selon le nombre de jours
  const getItemPrice = (item, days) => {
    if (!item.prix_1_jour || item.prix_1_jour === 0) return 0;
    if (days === 1) return item.prix_1_jour;
    
    // si le tarif 2 jours existe, le cout additionnel journalier est la difference entre 2j et 1j
    // sinon, on facture le tarif 1j pour chaque jour supplementaire
    const additionalDayPrice = (item.prix_2_jours && item.prix_2_jours > 0) 
      ? (item.prix_2_jours - item.prix_1_jour) 
      : item.prix_1_jour;
      
    return item.prix_1_jour + ((days - 1) * additionalDayPrice);
  };
  
  // calcul du total estime pour l'affichage
  const estimatedTotal = computed(() => {
    const total = cartStore.items.reduce((sum, item) => sum + getItemPrice(item, numberOfDays.value), 0);
    return total > 0 ? `${total} €` : 'Sur mesure';
  });
  
  // methode generique d'appel a l'api nominatim (openstreetmap)
  const fetchNominatim = async (query) => {
    if (query.length < 3) return [];
    try {
      const response = await fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(query)}&countrycodes=fr,be&limit=5`);
      return await response.json();
    } catch (error) {
      console.error("erreur api adresse", error);
      return [];
    }
  };
  
  // handlers pour l'adresse client
  const searchAddressClient = async (event) => {
    suggestionsClient.value = await fetchNominatim(event.target.value);
  };
  
  const selectAddressClient = (suggestion) => {
    form.adresseClient = suggestion.display_name;
    suggestionsClient.value = []; 
  };
  
  // handlers pour le lieu de l'evenement
  const searchAddressLieu = async (event) => {
    suggestionsLieu.value = await fetchNominatim(event.target.value);
  };
  
  const selectAddressLieu = (suggestion) => {
    form.lieuEvenement = suggestion.display_name;
    suggestionsLieu.value = []; 
  };
  
  // envoi de la commande
  const submitOrder = () => {
    const payload = {
      client: { ...form },
      panier: cartStore.items,
      dureeLocationJours: numberOfDays.value,
      totalEstime: estimatedTotal.value
    };
    
    console.log('payload pret pour le backend:', payload);
    
    cartStore.clearCart();
    router.push('/');
    alert("votre demande de devis a bien été envoyée.");
  };
  </script>