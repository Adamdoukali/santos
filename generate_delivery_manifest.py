import csv
import json
import os

orders_sample = [
    {
        'Tracking_Number': 'SN-TRK-784012',
        'Order_ID': 'SN-481920',
        'Date': '2026-10-29 10:15',
        'Customer_Name': 'Kawtar Benjelloun',
        'Phone': '0661234567',
        'City': 'Casablanca',
        'Address': '14 Rue Jean Jaurès, Résidence Al Andalous, Apt 12, Gauthier',
        'Product': 'MANTECO ORIGINALLY ❤️‍🔥 (Taille: M, Couleur: Noir)',
        'Quantity': 1,
        'COD_Amount_MAD': 850.00,
        'Carrier': 'Cathedis Express',
        'Delivery_Status': 'Livré & Encaissé',
        'Payment_Status': 'Encaissé (Virement reçu)',
        'Last_Update': '2026-10-29 16:30',
        'Notes': 'Colis remis en main propre. Paiement espèces.'
    },
    {
        'Tracking_Number': 'SN-TRK-784013',
        'Order_ID': 'SN-481921',
        'Date': '2026-10-29 11:40',
        'Customer_Name': 'Yasmine El Amrani',
        'Phone': '0662890123',
        'City': 'Rabat',
        'Address': '22 Avenue Mohammed VI, Villa Les Orangers, Souissi',
        'Product': 'Trensh original (Taille: S, Couleur: Camel)',
        'Quantity': 1,
        'COD_Amount_MAD': 700.00,
        'Carrier': 'Amana Express',
        'Delivery_Status': 'En cours de livraison',
        'Payment_Status': 'À encaisser à la livraison',
        'Last_Update': '2026-10-29 14:15',
        'Notes': 'Appeler 30min avant passage sur place.'
    },
    {
        'Tracking_Number': 'SN-TRK-784014',
        'Order_ID': 'SN-481922',
        'Date': '2026-10-29 12:05',
        'Customer_Name': 'Houda Chraibi',
        'Phone': '0663789012',
        'City': 'Marrakech',
        'Address': 'Palmeraie Village 2, Villa 48, Circuit de la Palmeraie',
        'Product': 'ENSEMBLE SANTOS (Taille: M, Couleur: Red)',
        'Quantity': 2,
        'COD_Amount_MAD': 848.30,
        'Carrier': 'Cathedis Express',
        'Delivery_Status': 'En cours de livraison',
        'Payment_Status': 'À encaisser à la livraison',
        'Last_Update': '2026-10-29 15:00',
        'Notes': 'Offre bundle 2 pièces (-15%). Sonner à la conciergerie.'
    },
    {
        'Tracking_Number': 'SN-TRK-784015',
        'Order_ID': 'SN-481923',
        'Date': '2026-10-29 13:20',
        'Customer_Name': 'Salma Berrada',
        'Phone': '0664567890',
        'City': 'Tanger',
        'Address': '9 Boulevard Pasteur, Étage 4, Centre Ville',
        'Product': 'BLAZER SURPIQÛRES CONTRASTE ZW (Taille: L, Couleur: Navy)',
        'Quantity': 1,
        'COD_Amount_MAD': 499.00,
        'Carrier': 'Sendit Delivery',
        'Delivery_Status': 'Expédié (En transit)',
        'Payment_Status': 'À encaisser à la livraison',
        'Last_Update': '2026-10-29 16:00',
        'Notes': 'Livraison prévue le 30/10 avant 14h.'
    },
    {
        'Tracking_Number': 'SN-TRK-784016',
        'Order_ID': 'SN-481924',
        'Date': '2026-10-29 14:10',
        'Customer_Name': 'Nadia Tazi',
        'Phone': '0665123456',
        'City': 'Fès',
        'Address': 'Lotissement Al Qods, Villa 15, Route d Imouzzer',
        'Product': 'Regular Fit Wool Like Midi Length Coat (Taille: M, Couleur: Anthracite)',
        'Quantity': 1,
        'COD_Amount_MAD': 750.00,
        'Carrier': 'Amana Express',
        'Delivery_Status': 'Expédié (En transit)',
        'Payment_Status': 'À encaisser à la livraison',
        'Last_Update': '2026-10-29 16:45',
        'Notes': 'Confirmation par WhatsApp effectuée.'
    },
    {
        'Tracking_Number': 'SN-TRK-784017',
        'Order_ID': 'SN-481925',
        'Date': '2026-10-29 14:55',
        'Customer_Name': 'Kenza Idrissi',
        'Phone': '0666234567',
        'City': 'Agadir',
        'Address': 'Résidence Islane, Immeuble C, Apt 8, Founty',
        'Product': 'TRUE AVENUE BLACK VALE JACKET (Taille: M, Couleur: Noir Cuir)',
        'Quantity': 1,
        'COD_Amount_MAD': 800.00,
        'Carrier': 'Cathedis Express',
        'Delivery_Status': 'En attente d enlèvement',
        'Payment_Status': 'À encaisser à la livraison',
        'Last_Update': '2026-10-29 15:30',
        'Notes': 'Colis étiqueté et prêt au hub Casablanca.'
    },
    {
        'Tracking_Number': 'SN-TRK-784018',
        'Order_ID': 'SN-481926',
        'Date': '2026-10-29 15:30',
        'Customer_Name': 'Leila Bensouda',
        'Phone': '0667345678',
        'City': 'Meknès',
        'Address': '18 Rue de Paris, Quartier Hamria',
        'Product': 'Trench Kaki Chic Original (Taille: S, Couleur: Kaki Chic)',
        'Quantity': 1,
        'COD_Amount_MAD': 599.00,
        'Carrier': 'Sendit Delivery',
        'Delivery_Status': 'En attente d enlèvement',
        'Payment_Status': 'À encaisser à la livraison',
        'Last_Update': '2026-10-29 15:45',
        'Notes': 'Validation taille au téléphone.'
    },
    {
        'Tracking_Number': 'SN-TRK-784019',
        'Order_ID': 'SN-481927',
        'Date': '2026-10-29 16:10',
        'Customer_Name': 'Zineb Filali',
        'Phone': '0668456789',
        'City': 'Casablanca',
        'Address': 'Anfa Supérieur, Rue des Merisiers, Villa 5',
        'Product': 'Combinaison Velvet Gold Luxe (Taille: M, Couleur: Velours Doré)',
        'Quantity': 1,
        'COD_Amount_MAD': 620.00,
        'Carrier': 'Livreur Privé Santos',
        'Delivery_Status': 'En cours de livraison',
        'Payment_Status': 'À encaisser à la livraison',
        'Last_Update': '2026-10-29 17:00',
        'Notes': 'Livraison VIP Express Casablanca.'
    },
    {
        'Tracking_Number': 'SN-TRK-784020',
        'Order_ID': 'SN-481928',
        'Date': '2026-10-29 16:45',
        'Customer_Name': 'Meriem Lahlou',
        'Phone': '0669567890',
        'City': 'Kénitra',
        'Address': 'Avenue Diouri, Résidence Maâmora, Apt 14',
        'Product': 'Doudoune Original France (Taille: L, Couleur: Noir Laqué)',
        'Quantity': 1,
        'COD_Amount_MAD': 499.00,
        'Carrier': 'Cathedis Express',
        'Delivery_Status': 'En attente de confirmation',
        'Payment_Status': 'À encaisser à la livraison',
        'Last_Update': '2026-10-29 16:50',
        'Notes': 'Rappel client prévu demain matin 10h.'
    },
    {
        'Tracking_Number': 'SN-TRK-784021',
        'Order_ID': 'SN-481929',
        'Date': '2026-10-29 17:15',
        'Customer_Name': 'Fatima-Zahra Alami',
        'Phone': '0670123456',
        'City': 'Mohammédia',
        'Address': 'Parc Plaza, Bâtiment B, Apt 3, Corniche Mohammédia',
        'Product': 'Robe jeans new collection 2026 (Taille: S, Couleur: Blue Denim)',
        'Quantity': 1,
        'COD_Amount_MAD': 399.00,
        'Carrier': 'Cathedis Express',
        'Delivery_Status': 'En attente de confirmation',
        'Payment_Status': 'À encaisser à la livraison',
        'Last_Update': '2026-10-29 17:20',
        'Notes': 'Commande directe EasySell COD.'
    },
    {
        'Tracking_Number': 'SN-TRK-784022',
        'Order_ID': 'SN-481930',
        'Date': '2026-10-29 17:40',
        'Customer_Name': 'Asmaa Guessous',
        'Phone': '0671234567',
        'City': 'Tétouan',
        'Address': 'Avenue Hassan II, Résidence Wilaya, Étage 2',
        'Product': 'Grace Buckle Detail Black Midi Shirt Dress (Taille: M, Couleur: Noir)',
        'Quantity': 1,
        'COD_Amount_MAD': 349.00,
        'Carrier': 'Amana Express',
        'Delivery_Status': 'En attente de confirmation',
        'Payment_Status': 'À encaisser à la livraison',
        'Last_Update': '2026-10-29 17:45',
        'Notes': 'Paiement à la livraison 349 DH + livraison.'
    },
    {
        'Tracking_Number': 'SN-TRK-784023',
        'Order_ID': 'SN-481931',
        'Date': '2026-10-29 18:20',
        'Customer_Name': 'Ghita Bennani',
        'Phone': '0672345678',
        'City': 'Casablanca',
        'Address': 'Bouskoura Ville Verte, Résidence Les Bosquets, Villa 21',
        'Product': 'Manteco, manteau long ceinturé ultra chic (Taille: M, Couleur: Camel Royal)',
        'Quantity': 1,
        'COD_Amount_MAD': 599.00,
        'Carrier': 'Livreur Privé Santos',
        'Delivery_Status': 'Prêt pour expédition',
        'Payment_Status': 'À encaisser à la livraison',
        'Last_Update': '2026-10-29 18:30',
        'Notes': 'Passage livreur programmé le 30/10 matin.'
    }
]

fields = [
    'Tracking_Number', 'Order_ID', 'Date', 'Customer_Name', 'Phone',
    'City', 'Address', 'Product', 'Quantity', 'COD_Amount_MAD',
    'Carrier', 'Delivery_Status', 'Payment_Status', 'Last_Update', 'Notes'
]

def generate_files():
    # 1. Standard comma-delimited RFC-4180 CSV
    with open('santos_delivery_tracking.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(orders_sample)
    print('Generated santos_delivery_tracking.csv (comma-separated, UTF-8 BOM)')

    # 2. Semicolon-delimited for French Microsoft Excel
    with open('santos_delivery_tracking_excel.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter=';')
        writer.writeheader()
        writer.writerows(orders_sample)
    print('Generated santos_delivery_tracking_excel.csv (semicolon-separated, UTF-8 BOM)')

if __name__ == '__main__':
    generate_files()

