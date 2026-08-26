from pydantic import BaseModel, EmailStr
from typing import List, Optional

class CartItem(BaseModel):
    id: int
    nom: str
    categories: List[str]
    prix_1_jour: Optional[float] = 0
    prix_2_jours: Optional[float] = 0

class ClientInfo(BaseModel):
    prenom: str
    nom: str
    organisme: Optional[str] = ""
    telephone: str
    email: EmailStr
    adresseClient: str
    typeEvenement: str
    lieuEvenement: str
    dateDebut: str
    heureDebut: str
    dateFin: str
    heureFin: str
    detailEvenement: Optional[str] = ""
    typeSol: str
    autreSol: Optional[str] = ""
    livraison: str
    noteLivraison: Optional[str] = ""
    prestations: List[str]
    surveillanceJeux: List[str]
    detailPrestations: Optional[str] = ""
    budget: str

class QuoteRequest(BaseModel):
    client: ClientInfo
    panier: List[CartItem]
    dureeLocationJours: int
    totalEstime: str