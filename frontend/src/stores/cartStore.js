import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useCartStore = defineStore('cart', () => {
  // --- STATE (L'état de nos données) ---
  const items = ref([]) // La liste des jeux ajoutés
  const isOpen = ref(false) // L'état d'ouverture du panneau latéral

  // --- GETTERS (Données calculées) ---
  const itemCount = computed(() => items.value.length)

  // --- ACTIONS (Fonctions pour modifier l'état) ---
  function addItem(game) {
    items.value.push(game)
  }

  function removeItem(index) {
    items.value.splice(index, 1)
  }

  function clearCart() {
    items.value = []
  }

  function toggleCart() {
    isOpen.value = !isOpen.value
  }

  function closeCart() {
    isOpen.value = false
  }

  return { 
    items, isOpen, itemCount, 
    addItem, removeItem, clearCart, toggleCart, closeCart 
  }
})