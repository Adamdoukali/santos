import os
import shutil
import zipfile

theme_dir = 'santos-shopify-theme'
os.makedirs(f"{theme_dir}/assets", exist_ok=True)
os.makedirs(f"{theme_dir}/config", exist_ok=True)
os.makedirs(f"{theme_dir}/layout", exist_ok=True)
os.makedirs(f"{theme_dir}/locales", exist_ok=True)
os.makedirs(f"{theme_dir}/sections", exist_ok=True)
os.makedirs(f"{theme_dir}/snippets", exist_ok=True)
os.makedirs(f"{theme_dir}/templates", exist_ok=True)

# 1. Copy Assets
assets_to_copy = [
    'santos-custom.css',
    'app_style_balmoral.css',
    'santos-logo-white.png',
    'santos-logo-black.png',
    'favicon.png',
    'ABCArizonaMix-Regular.woff2',
    'FTKunstGrotesk-Regular.woff2',
    'FTKunstGrotesk-Medium.woff2',
    'PPNeueMontreal-Regular.woff2',
    'PPNeueMontreal-Medium.woff2',
]
for a in assets_to_copy:
    if os.path.exists(a):
        shutil.copy(a, f"{theme_dir}/assets/{a}")

# Copy videos
if os.path.exists('hero-video.mp4'):
    shutil.copy('hero-video.mp4', f"{theme_dir}/assets/hero-video.mp4")
if os.path.exists('assets/videos/atelier-video.mp4'):
    shutil.copy('assets/videos/atelier-video.mp4', f"{theme_dir}/assets/atelier-video.mp4")

# Copy collection images
if os.path.exists('assets/images/collections'):
    for f in os.listdir('assets/images/collections'):
        shutil.copy(f"assets/images/collections/{f}", f"{theme_dir}/assets/{f}")

print("Assets copied.")

# 2. config/settings_schema.json
settings_schema = '''[
  {
    "name": "theme_info",
    "theme_name": "Santos Haute Couture",
    "theme_version": "1.0.0",
    "theme_author": "Maison Santos",
    "theme_documentation_url": "https://a9xpr3-x0.myshopify.com",
    "theme_support_url": "https://a9xpr3-x0.myshopify.com"
  },
  {
    "name": "General Settings",
    "settings": [
      {
        "type": "text",
        "id": "hero_title",
        "label": "Hero Title",
        "default": "New Collection Winter 2026-2027"
      },
      {
        "type": "text",
        "id": "free_shipping_threshold",
        "label": "Free Shipping Threshold (MAD)",
        "default": "1000"
      }
    ]
  }
]'''
with open(f"{theme_dir}/config/settings_schema.json", 'w', encoding='utf-8') as f:
    f.write(settings_schema)

# 3. locales/fr.json & en.default.json
locales_fr = '''{
  "general": {
    "search": "Recherche",
    "cart": "Panier",
    "checkout": "Commander en Toute Sécurité",
    "all_collections": "Toutes les Pièces"
  }
}'''
with open(f"{theme_dir}/locales/fr.json", 'w', encoding='utf-8') as f:
    f.write(locales_fr)
with open(f"{theme_dir}/locales/en.default.json", 'w', encoding='utf-8') as f:
    f.write(locales_fr)

# 4. layout/theme.liquid
theme_liquid = '''<!DOCTYPE html>
<html lang="{{ request.locale.iso_code }}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>{{ page_title }} | {{ shop.name }}</title>
  {% if page_description %}
    <meta name="description" content="{{ page_description | escape }}">
  {% endif %}
  <link rel="canonical" href="{{ canonical_url }}">
  <link rel="icon" type="image/png" href="{{ 'favicon.png' | asset_url }}">

  {{ 'app_style_balmoral.css' | asset_url | stylesheet_tag }}
  {{ 'santos-custom.css' | asset_url | stylesheet_tag }}

  {{ content_for_header }}
</head>
<body class="template-{{ template.name }}">

  {% section 'header' %}

  <main role="main" id="MainContent">
    {{ content_for_layout }}
  </main>

  {% section 'footer' %}

  {% render 'cart-drawer' %}
  {% render 'search-drawer' %}
  {% render 'quick-view-modal' %}

</body>
</html>'''
with open(f"{theme_dir}/layout/theme.liquid", 'w', encoding='utf-8') as f:
    f.write(theme_liquid)

# 5. sections/header.liquid
header_liquid = '''<header id="site-header" class="{% if template.name == 'index' %}header-inverted{% else %}header-scrolled{% endif %}" role="banner">
  <div class="site-header__wrap">
    <nav class="site-header__leftNav" aria-label="Main Navigation">
      <button class="site-header__burger d-xl-none" id="burger-btn" aria-label="Toggle Menu" onclick="toggleMobileNav()">
        <span></span><span></span><span></span>
      </button>
      <ul class="menu d-none d-xl-flex">
        <li class="menu-item"><a href="/collections/all">Collections</a></li>
        <li class="menu-item"><a href="/collections/manteaux">Manteaux</a></li>
        <li class="menu-item"><a href="/collections/ensembles">Ensembles</a></li>
        <li class="menu-item"><a href="/collections/robes">Robes</a></li>
        <li class="menu-item"><a href="/collections/jeans">Jeans</a></li>
      </ul>
    </nav>

    <figure class="site-header__logo m-0 p-0">
      <a class="site-header__logoLink" href="/" rel="home">
        <img class="logo-img-white" src="{{ 'santos-logo-white.png' | asset_url }}" alt="Santos Haute Couture">
        <img class="logo-img-black" src="{{ 'santos-logo-black.png' | asset_url }}" alt="Santos Haute Couture">
      </a>
    </figure>

    <nav class="site-header__rightNav" aria-label="Utility Navigation">
      <button class="site-header__searchBtn" onclick="openSearch()" aria-label="Search">
        <span class="d-none d-md-inline">Recherche</span>
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M6.93 0.35C10.22 0.52 12.84 3.24 12.84 6.57L12.84 6.9C12.76 8.35 12.18 9.68 11.28 10.7L15.97 15.19L15.27 15.91L10.55 11.4C9.48 12.28 8.11 12.81 6.61 12.81L6.29 12.8C3.1 12.64 0.55 10.08 0.39 6.9L0.38 6.57C0.38 3.13 3.17 0.34 6.61 0.34L6.93 0.35Z" fill="currentColor"/></svg>
      </button>

      <button class="site-header__cartBtn" onclick="openCart()" aria-label="Cart">
        <span>Panier</span>
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M14.49 15.5L13.87 5.29H2.13L1.51 15.5H14.49Z" stroke="currentColor"/><path d="M4.8 4.79V3.72C4.8 1.95 6.23 0.52 8 0.52C9.77 0.52 11.2 1.95 11.2 3.72V4.79" stroke="currentColor"/></svg>
        <span class="cart-badge" id="header-cart-count">{{ cart.item_count }}</span>
      </button>
    </nav>
  </div>
</header>'''
with open(f"{theme_dir}/sections/header.liquid", 'w', encoding='utf-8') as f:
    f.write(header_liquid)

# 6. sections/hero-video.liquid
hero_liquid = '''<section class="pb-row-hero" id="hero">
  <div class="pb-row-hero__media" aria-hidden="true">
    <video class="pb-row-hero__video" autoplay muted loop playsinline preload="auto">
      <source src="{{ 'hero-video.mp4' | asset_url }}" type="video/mp4">
    </video>
  </div>
  <div class="pb-row-hero__inner">
    <div>
      <h1 class="pb-row-hero__title">New Collection Winter 2026-2027</h1>
      <a href="/collections/all" class="btn --link">Découvrir la Collection</a>
    </div>
    <div>
      <p class="pb-row-hero__text">
        L'élégance intemporelle façonnée pour sublimer la silhouette. Des manteaux d'exception en laine Manteco aux tailleurs surpiqués ZW, la Maison Santos présente des pièces alliant architecture de coupe, matières luxueuses et finitions d'atelier.
      </p>
      <a href="/collections/manteaux" class="btn --link">Voir les Manteaux & Trenchs</a>
    </div>
  </div>
</section>'''
with open(f"{theme_dir}/sections/hero-video.liquid", 'w', encoding='utf-8') as f:
    f.write(hero_liquid)

# 7. sections/collections-grid.liquid
col_grid_liquid = '''<section class="section-container" id="collections-showcase" style="padding-top: 48px; padding-bottom: 24px;">
  <div class="section-header">
    <div>
      <h2 class="section-title">Les Collections</h2>
      <p class="fz-14" style="color: #666; margin: 4px 0 0 0;">Explorez l'univers Santos à travers nos lignes exclusives</p>
    </div>
    <a href="/collections/all" class="btn --link">Voir Tout</a>
  </div>
  <div class="collections-category-grid">
    <a href="/collections/manteaux" class="category-banner-card">
      <img src="{{ '10022106595618_0_DSC00749.jpg' | asset_url }}" alt="Manteaux & Trenchs" loading="lazy">
      <div class="category-banner-badge">Manteaux</div>
      <div class="category-banner-overlay">
        <h3>Manteaux d'Atelier</h3>
        <span>Découvrir</span>
      </div>
    </a>
    <a href="/collections/ensembles" class="category-banner-card">
      <img src="{{ 'ensembles.webp' | asset_url }}" alt="Ensembles & Tailleurs" loading="lazy">
      <div class="category-banner-badge">Ensembles & Tailleurs</div>
    </a>
    <a href="/collections/robes" class="category-banner-card">
      <img src="{{ 'robes.webp' | asset_url }}" alt="Robes & Combinaisons" loading="lazy">
      <div class="category-banner-badge">Robes & Combinaisons</div>
    </a>
    <a href="/collections/jeans" class="category-banner-card">
      <img src="{{ 'jeans.webp' | asset_url }}" alt="Denim & Jeans" loading="lazy">
      <div class="category-banner-badge">Denim & Jeans</div>
    </a>
  </div>
</section>'''
with open(f"{theme_dir}/sections/collections-grid.liquid", 'w', encoding='utf-8') as f:
    f.write(col_grid_liquid)

# 8. sections/about-atelier.liquid
about_liquid = '''<section class="section-container" id="about-us">
  <div class="about-section">
    <div class="about-header">
      <div>
        <h2 class="section-title">La Maison Santos</h2>
        <p class="about-header__desc">
          Fondée sur une exigence absolue de coupe et de noblesse des matières, la Maison Santos façonne des pièces couture contemporaines. Chaque drapé, chaque surpiqûre exprime un art de vivre empreint de raffinement et d'assurance.
        </p>
      </div>
      <a href="/collections/all" class="btn --link">Découvrir Notre Univers</a>
    </div>

    <div class="about-media-box">
      <img src="{{ '10022106595618_2_DSC00712.jpg' | asset_url }}" alt="Atelier Santos Craftsmanship">
    </div>

    <div class="about-media-box">
      <video autoplay muted loop playsinline preload="auto">
        <source src="{{ 'atelier-video.mp4' | asset_url }}" type="video/mp4">
      </video>
    </div>
  </div>
</section>'''
with open(f"{theme_dir}/sections/about-atelier.liquid", 'w', encoding='utf-8') as f:
    f.write(about_liquid)

# 9. sections/footer.liquid
footer_liquid = '''<footer class="site-footer" role="contentinfo">
  <div class="footer-grid">
    <nav class="footer-nav">
      <ul>
        <li><a href="/pages/contact">Contact</a></li>
        <li><a href="https://instagram.com" target="_blank" rel="noopener">Instagram</a></li>
        <li><a href="/pages/faq">FAQ</a></li>
      </ul>
      <ul>
        <li><a href="/pages/livraison">Livraison & Retours</a></li>
        <li><a href="/pages/suivi">Suivi de commande</a></li>
      </ul>
      <ul>
        <li><a href="/#about-us">La Maison Santos</a></li>
        <li><a href="/pages/conditions">Conditions & Confidentialité</a></li>
      </ul>
    </nav>
    <div class="newsletter-box">
      <h4>Newsletter Santos Privilège</h4>
      <form class="newsletter-form" action="/contact#contact_form" method="post">
        <input type="email" name="contact[email]" class="newsletter-input" placeholder="Votre adresse email" required>
        <button type="submit" class="newsletter-submit">S'inscrire</button>
      </form>
    </div>
    <div class="footer-selectors">
      <div class="footer-select-wrap">
        <label>Pays / Devise</label>
        <select class="footer-select">
          <option value="MA" selected>Maroc (MAD)</option>
          <option value="FR">France (EUR)</option>
          <option value="US">États-Unis (USD)</option>
          <option value="CA">Canada (CAD)</option>
        </select>
      </div>
    </div>
  </div>
  <div class="footer-bottom">
    <p class="m-0">Copyright © 2026 Santos. Tous droits réservés.</p>
    <p class="m-0">Maison de Couture & Prêt-à-Porter d'Exception</p>
  </div>
</footer>'''
with open(f"{theme_dir}/sections/footer.liquid", 'w', encoding='utf-8') as f:
    f.write(footer_liquid)

# 10. templates/index.liquid
index_liquid = '''{% section 'hero-video' %}
{% section 'collections-grid' %}
{% section 'about-atelier' %}
'''
with open(f"{theme_dir}/templates/index.liquid", 'w', encoding='utf-8') as f:
    f.write(index_liquid)

# 11. templates/collection.liquid
col_liquid = '''<main class="section-container collection-header" role="main">
  <div class="collection-header__inner">
    <div>
      <h1 class="collection-title">{{ collection.title | default: 'Toutes les Pièces' }}</h1>
      <div class="collection-count">{{ collection.products_count }} créations Santos</div>
    </div>
    <a href="/" class="btn --link">Retour à l'Accueil</a>
  </div>

  <div class="product-grid">
    {% for product in collection.products %}
      <article class="product-card">
        <a href="{{ product.url }}" class="product-card__thumbnail">
          <img class="product-card__img" src="{{ product.featured_image | img_url: '800x' }}" alt="{{ product.title }}" loading="lazy">
        </a>
        <div class="product-card__content">
          <h3 class="product-card__title">{{ product.title }}</h3>
          <p class="product-card__price">{{ product.price | money }}</p>
        </div>
      </article>
    {% endfor %}
  </div>
</main>'''
with open(f"{theme_dir}/templates/collection.liquid", 'w', encoding='utf-8') as f:
    f.write(col_liquid)

# 12. templates/product.liquid
product_liquid = '''<div class="section-container" style="padding-top: 100px;">
  <div style="display: grid; grid-template-columns: 1fr; gap: 40px;" class="product-detail-grid">
    <div>
      <img src="{{ product.featured_image | img_url: '1200x' }}" style="width: 100%; aspect-ratio: 3/4; object-fit: cover;" alt="{{ product.title }}">
    </div>
    <div>
      <h1 class="ff-heading" style="font-size: 32px; margin-bottom: 8px;">{{ product.title }}</h1>
      <div style="font-size: 22px; margin-bottom: 24px;">{{ product.price | money }}</div>
      <form action="/cart/add" method="post">
        <input type="hidden" name="id" value="{{ product.selected_or_first_available_variant.id }}">
        <button type="submit" class="btn-checkout" style="max-width: 320px;">Ajouter au Panier</button>
      </form>
      <div style="margin-top: 32px; line-height: 1.6; color: #555;">{{ product.description }}</div>
    </div>
  </div>
</div>'''
with open(f"{theme_dir}/templates/product.liquid", 'w', encoding='utf-8') as f:
    f.write(product_liquid)

# 13. snippets/cart-drawer.liquid
cart_drawer_liquid = '''<div class="site-cart" id="cart-drawer" aria-hidden="true">
  <div class="site-cart__backdrop" onclick="closeCart()"></div>
  <div class="site-cart__container">
    <div class="site-cart__header">
      <h3 class="ff-heading">Votre Panier (<span id="cart-drawer-count">{{ cart.item_count }}</span>)</h3>
      <button class="site-cart__close" onclick="closeCart()" aria-label="Fermer">✕</button>
    </div>
    <div class="site-cart__freeship">
      <span>Livraison express Santos offerte dès 1 000 MAD d'achats</span>
    </div>
    <div class="site-cart__items">
      {% for item in cart.items %}
        <div class="cart-item">
          <img src="{{ item.image | img_url: '200x' }}" alt="{{ item.title }}">
          <div class="cart-item__info">
            <h4>{{ item.product.title }}</h4>
            <div class="cart-item__meta">{{ item.variant.title }}</div>
            <div class="cart-item__qty">Qté: {{ item.quantity }}</div>
          </div>
          <div class="cart-item__price">{{ item.final_line_price | money }}</div>
        </div>
      {% endfor %}
    </div>
    <div class="site-cart__footer">
      <div class="cart-subtotal">
        <span>Sous-total</span>
        <span>{{ cart.total_price | money }}</span>
      </div>
      <a href="/checkout" class="btn-checkout" style="display:block; text-align:center; text-decoration:none;">Commander en Toute Sécurité</a>
    </div>
  </div>
</div>'''
with open(f"{theme_dir}/snippets/cart-drawer.liquid", 'w', encoding='utf-8') as f:
    f.write(cart_drawer_liquid)

# 14. snippets/search-drawer.liquid
search_liquid = '''<div class="site-header__searchbar" id="search-overlay" aria-hidden="true">
  <button class="site-header__searchClose" onclick="closeSearch()" aria-label="Close search">✕</button>
  <form action="/search" method="get" class="search-form__fieldset">
    <input type="text" name="q" class="search-form__input" placeholder="Rechercher dans la collection Santos..." autocomplete="off">
    <button class="search-form__btn" type="submit">Chercher</button>
  </form>
</div>'''
with open(f"{theme_dir}/snippets/search-drawer.liquid", 'w', encoding='utf-8') as f:
    f.write(search_liquid)

# 15. snippets/quick-view-modal.liquid
quick_liquid = '''<div class="modal-overlay" id="product-modal" aria-hidden="true">
  <div class="modal-container">
    <button class="modal-close" onclick="closeProductModal()">✕</button>
    <div class="modal-media">
      <img id="modal-img" src="" alt="Produit Santos" style="aspect-ratio:3/4; object-fit:cover; width:100%;">
      <div class="modal-thumbs" id="modal-thumbs"></div>
    </div>
    <div class="modal-details">
      <h2 class="modal-title ff-heading" id="modal-title"></h2>
      <div class="modal-price" id="modal-price"></div>
      <p id="modal-desc" style="color: #555;"></p>
      <button class="btn-checkout" onclick="addModalItemToCart()">Ajouter au Panier</button>
    </div>
  </div>
</div>'''
with open(f"{theme_dir}/snippets/quick-view-modal.liquid", 'w', encoding='utf-8') as f:
    f.write(quick_liquid)

# Create ZIP archive
zip_path = 'santos-shopify-theme.zip'
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(theme_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, theme_dir)
            zipf.write(full_path, arcname=rel_path)

print(f"Shopify Theme successfully created and zipped to {zip_path}!")
