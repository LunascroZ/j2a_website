import smtplib
from email.message import EmailMessage
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import QuoteRequest

app = FastAPI(title="API J2A")

# configuration des cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def send_quote_email(quote: QuoteRequest):
    """
    construit et envoie l'email de recapitulatif au format html via le serveur smtp local
    """
    msg = EmailMessage()
    msg['Subject'] = f"Nouvelle demande de devis : {quote.client.prenom} {quote.client.nom}"
    msg['From'] = "website@j2a.fr"
    msg['To'] = "contact@j2a.fr" 

    # 1. on recupere et formatte les donnees complexes
    prestations_list = ", ".join(quote.client.prestations) if quote.client.prestations else "Aucune"
    
    # 2. generation des lignes du tableau pour les jeux
    lignes_panier = ""
    for item in quote.panier:
        surveillance_requise = "✅ Oui" if item.nom in quote.client.surveillanceJeux else "-"
        lignes_panier += f"""
        <tr>
            <td style="padding: 12px; border-bottom: 1px solid #e5e7eb; color: #1e3a8a; font-weight: bold;">
                {item.nom} <br>
                <span style="font-size: 12px; color: #6b7280; font-weight: normal; text-transform: uppercase;">{item.categories[0]}</span>
            </td>
            <td style="padding: 12px; border-bottom: 1px solid #e5e7eb; text-align: center; color: #4b5563;">
                {surveillance_requise}
            </td>
        </tr>
        """

    # 3. construction du template html complet
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
    </head>
    <body style="font-family: Arial, sans-serif; background-color: #f3f4f6; padding: 20px; margin: 0; color: #1f2937;">
        
        <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
            
            <!-- en-tete -->
            <div style="background-color: #1e3a8a; color: white; padding: 24px; text-align: center;">
                <h1 style="margin: 0; font-size: 24px; color: #ffffff;">Nouvelle demande de devis</h1>
                <p style="margin: 8px 0 0 0; color: #93c5fd;">Générée depuis le site web J2A</p>
            </div>

            <div style="padding: 32px;">
                
                <!-- bloc client -->
                <h2 style="color: #ea580c; font-size: 18px; border-bottom: 2px solid #fdba74; padding-bottom: 8px; margin-top: 0;">👤 Informations Client</h2>
                <p><strong>Nom :</strong> {quote.client.prenom} {quote.client.nom}</p>
                <p><strong>Organisme :</strong> {quote.client.organisme or 'Particulier'}</p>
                <p><strong>Email :</strong> <a href="mailto:{quote.client.email}" style="color: #1e3a8a;">{quote.client.email}</a></p>
                <p><strong>Téléphone :</strong> {quote.client.telephone}</p>
                <p><strong>Adresse de facturation :</strong> {quote.client.adresseClient}</p>

                <!-- bloc evenement -->
                <h2 style="color: #ea580c; font-size: 18px; border-bottom: 2px solid #fdba74; padding-bottom: 8px; margin-top: 32px;">📅 Détails de l'événement</h2>
                <p><strong>Type :</strong> {quote.client.typeEvenement}</p>
                <p><strong>Lieu :</strong> {quote.client.lieuEvenement}</p>
                <p><strong>Dates :</strong> Du <b>{quote.client.dateDebut}</b> ({quote.client.heureDebut}) au <b>{quote.client.dateFin}</b> ({quote.client.heureFin})</p>
                <p><strong>Durée calculée :</strong> {quote.dureeLocationJours} jour(s)</p>
                <p><strong>Détails supplémentaires :</strong> {quote.client.detailEvenement or 'Aucun'}</p>

                <!-- bloc logistique -->
                <h2 style="color: #ea580c; font-size: 18px; border-bottom: 2px solid #fdba74; padding-bottom: 8px; margin-top: 32px;">🚚 Logistique & Terrain</h2>
                <p><strong>Type de sol :</strong> {quote.client.typeSol} {quote.client.autreSol}</p>
                <p><strong>Option de livraison :</strong> {quote.client.livraison}</p>
                <p><strong>Notes de livraison :</strong> {quote.client.noteLivraison or 'Aucune'}</p>
                <p><strong>Prestations souhaitées :</strong> {prestations_list}</p>
                <p><strong>Détails prestations :</strong> {quote.client.detailPrestations or 'Aucun'}</p>

                <!-- bloc panier -->
                <h2 style="color: #ea580c; font-size: 18px; border-bottom: 2px solid #fdba74; padding-bottom: 8px; margin-top: 32px;">🎯 Sélection des jeux</h2>
                
                <table style="width: 100%; border-collapse: collapse; margin-top: 16px;">
                    <thead>
                        <tr style="background-color: #f8fafc;">
                            <th style="padding: 12px; text-align: left; border-bottom: 2px solid #e5e7eb; color: #475569;">Jeu</th>
                            <th style="padding: 12px; text-align: center; border-bottom: 2px solid #e5e7eb; color: #475569;">Surveillance demandée</th>
                        </tr>
                    </thead>
                    <tbody>
                        {lignes_panier}
                    </tbody>
                </table>

                <!-- bloc budget -->
                <div style="background-color: #fff7ed; border-left: 4px solid #ea580c; padding: 16px; margin-top: 32px; border-radius: 4px;">
                    <p style="margin: 0 0 8px 0;"><strong>Budget estimatif client :</strong> {quote.client.budget}</p>
                    <p style="margin: 0; font-size: 18px;"><strong>Total calculé (Catalogue HT) :</strong> <span style="color: #ea580c; font-weight: bold;">{quote.totalEstime}</span></p>
                </div>

            </div>
            
            <div style="background-color: #f8fafc; padding: 16px; text-align: center; color: #64748b; font-size: 12px; border-top: 1px solid #e5e7eb;">
                Ce message automatique ne constitue pas un devis final. Veuillez recontacter le client pour confirmer les tarifs de livraison et valider les disponibilités.
            </div>
            
        </div>
    </body>
    </html>
    """

    # on definit d'abord une version texte brut (fallback obligatoire pour les vieux clients mail)
    msg.set_content("Veuillez activer l'affichage HTML pour lire cette demande de devis.")
    
    # on attache la version html principale
    msg.add_alternative(html_content, subtype='html')

    # envoi
    try:
        with smtplib.SMTP('localhost', 1025) as server:
            server.send_message(msg)
    except Exception as e:
        print(f"erreur smtp: {e}")
        raise HTTPException(status_code=500, detail="Erreur lors de l'envoi de l'email")


@app.post("/api/quote")
async def receive_quote(quote: QuoteRequest):
    print(f"traitement du devis pour {quote.client.email}...")
    send_quote_email(quote)
    return {
        "status": "success",
        "message": "la demande de devis a bien ete receptionnee et l'email a ete envoye."
    }