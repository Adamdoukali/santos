import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace video
old_video = '''        <div class="about-media-box">
          <video autoplay muted loop playsinline preload="auto">
            <source src="assets/videos/about-secondary.mp4" type="video/mp4">
          </video>
        </div>'''

new_video = '''        <div class="about-media-box">
          <video autoplay muted loop playsinline preload="auto">
            <source src="assets/videos/atelier-video.mp4" type="video/mp4">
            <source src="assets/videos/about-secondary.mp4" type="video/mp4">
            <source src="IMG_7829.MP4" type="video/mp4">
          </video>
        </div>'''

content = content.replace(old_video, new_video)

# Replace CAD prices in HTML
# Pattern: $850.00 CAD -> 850.00 MAD
content = re.sub(r'\$(\d+(?:\.\d+)?)\s*CAD', r'\1 MAD', content)
content = re.sub(r'\$(\d+(?:\.\d+)?)\.00\s*CAD', r'\1.00 MAD', content)

# Currency select
content = content.replace(
    '<option value="CA" selected>Canada (CAD)</option>',
    '<option value="CA">Canada (CAD)</option>'
)
content = content.replace(
    '<option value="MA">Maroc (MAD)</option>',
    '<option value="MA" selected>Maroc (MAD)</option>'
)

# Free shipping threshold in index.html
content = content.replace(
    'Livraison express offerte dès $500 CAD d\'achats',
    'Livraison express offerte dès 1 000 MAD d\'achats'
)
content = content.replace(
    'const threshold = 500;',
    'const threshold = 1000;'
)
content = content.replace(
    'Ajoutez $${(threshold - subtotal).toFixed(2)} CAD pour la livraison offerte',
    'Ajoutez ${(threshold - subtotal).toFixed(2)} MAD pour la livraison offerte'
)
content = content.replace(
    '\'$\' + subtotal.toFixed(2) + \' CAD\'',
    'subtotal.toFixed(2) + \' MAD\''
)
content = content.replace(
    '\'$\' + p.price.toFixed(2) + \' CAD\'',
    'p.price.toFixed(2) + \' MAD\''
)
content = content.replace(
    '<div class="cart-item__price">$${(item.price * item.qty).toFixed(2)} CAD</div>',
    '<div class="cart-item__price">${(item.price * item.qty).toFixed(2)} MAD</div>'
)
content = content.replace(
    '<p class="product-card__price">$${p.price.toFixed(2)} CAD</p>',
    '<p class="product-card__price">${p.price.toFixed(2)} MAD</p>'
)
content = content.replace(
    '<span id="cart-subtotal-price">$0.00 CAD</span>',
    '<span id="cart-subtotal-price">0.00 MAD</span>'
)
content = content.replace(
    '<div class="modal-price" id="modal-price">$0.00 CAD</div>',
    '<div class="modal-price" id="modal-price">0.00 MAD</div>'
)
content = content.replace(
    'Commande confirmée pour un montant de $\' + cart.reduce((s, i) => s + (i.price * i.qty), 0).toFixed(2) + \' CAD.',
    'Commande confirmée pour un montant de \' + cart.reduce((s, i) => s + (i.price * i.qty), 0).toFixed(2) + \' MAD.'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html successfully!")

# 2. Update collection.html
with open('collection.html', 'r', encoding='utf-8') as f:
    c_content = f.read()

c_content = re.sub(r'\$(\d+(?:\.\d+)?)\s*CAD', r'\1 MAD', c_content)
c_content = c_content.replace(
    '<option value="CA" selected>Canada (CAD)</option>',
    '<option value="CA">Canada (CAD)</option>'
)
c_content = c_content.replace(
    '<option value="MA">Maroc (MAD)</option>',
    '<option value="MA" selected>Maroc (MAD)</option>'
)
c_content = c_content.replace(
    'Livraison offerte dès $500 CAD d\'achats',
    'Livraison express offerte dès 1 000 MAD d\'achats'
)
c_content = c_content.replace(
    'const threshold = 500;',
    'const threshold = 1000;'
)
c_content = c_content.replace(
    'Ajoutez $${(threshold - subtotal).toFixed(2)} CAD pour la livraison offerte',
    'Ajoutez ${(threshold - subtotal).toFixed(2)} MAD pour la livraison offerte'
)
c_content = c_content.replace(
    '\'$\' + subtotal.toFixed(2) + \' CAD\'',
    'subtotal.toFixed(2) + \' MAD\''
)
c_content = c_content.replace(
    '\'$\' + p.price.toFixed(2) + \' CAD\'',
    'p.price.toFixed(2) + \' MAD\''
)
c_content = c_content.replace(
    '<div class="cart-item__price">$${(item.price * item.qty).toFixed(2)} CAD</div>',
    '<div class="cart-item__price">${(item.price * item.qty).toFixed(2)} MAD</div>'
)
c_content = c_content.replace(
    '<p class="product-card__price">$${p.price.toFixed(2)} CAD</p>',
    '<p class="product-card__price">${p.price.toFixed(2)} MAD</p>'
)
c_content = c_content.replace(
    '<span id="cart-subtotal-price">$0.00 CAD</span>',
    '<span id="cart-subtotal-price">0.00 MAD</span>'
)
c_content = c_content.replace(
    '<div class="modal-price" id="modal-price">$0.00 CAD</div>',
    '<div class="modal-price" id="modal-price">0.00 MAD</div>'
)
c_content = c_content.replace(
    'Commande confirmée pour un montant de $\' + cart.reduce((s, i) => s + (i.price * i.qty), 0).toFixed(2) + \' CAD.',
    'Commande confirmée pour un montant de \' + cart.reduce((s, i) => s + (i.price * i.qty), 0).toFixed(2) + \' MAD.'
)

with open('collection.html', 'w', encoding='utf-8') as f:
    f.write(c_content)

print("Updated collection.html successfully!")
