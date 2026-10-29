import re

def update_collection_liquid():
    path = 'santos-shopify-theme/templates/collection.liquid'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update grid class
    content = content.replace('<div class="product-grid" id="shopify-product-grid">', '<div class="choice-grid" id="shopify-product-grid">')
    
    # 2. Update card markup
    old_card_pattern = re.compile(
        r'<article class="product-card" data-category="\{\{ cat \}\}" data-title="\{\{ product\.title \| escape \}\}" data-price="\{\{ product\.price \}\}" data-tags="\{\{ product\.tags \| join: \',\' \| downcase \}\}" data-handle="\{\{ product\.handle \}\}">.*?</article>',
        re.DOTALL
    )

    new_card = """<article class="choice-card" data-category="{{ cat }}" data-title="{{ product.title | escape }}" data-price="{{ product.price }}" data-tags="{{ product.tags | join: ',' | downcase }}" data-handle="{{ product.handle }}" onclick="if(window.openQuickView){ openQuickView('{{ product.handle }}'); } else { window.location.href='{{ product.url }}'; }">
          <div class="choice-card__media">
            {% if product.compare_at_price > product.price %}
              <span class="choice-card__badge">Promo</span>
            {% elsif badge_text != blank %}
              <span class="choice-card__badge" style="background: rgba(18,18,18,0.85);">{{ badge_text }}</span>
            {% endif %}
            
            {% if card_image != blank %}
              <img class="choice-card__img" src="{{ card_image | img_url: '600x' }}" alt="{{ product.title | escape }}" loading="lazy">
            {% else %}
              <img class="choice-card__img" src="{{ '10022106595618_0_DSC00749.jpg' | asset_url }}" alt="{{ product.title | escape }}" loading="lazy">
            {% endif %}

            <button class="choice-card__quick-add" type="button" onclick="event.stopPropagation(); if(window.openQuickView) { openQuickView('{{ product.handle }}'); } else { window.location.href='{{ product.url }}'; }">
              Aperçu Rapide
            </button>
          </div>

          <div class="choice-card__info">
            <h3 class="choice-card__title" title="{{ product.title | escape }}">{{ product.title }}</h3>
            <div class="choice-card__price-row">
              {% if product.compare_at_price > product.price %}
                <span class="choice-card__price-compare">{{ product.compare_at_price | money }}</span>
                <span class="choice-card__price-sale">{{ product.price | money }}</span>
              {% else %}
                <span class="choice-card__price-regular">{{ product.price | money }}</span>
              {% endif %}
            </div>
          </div>
        </article>"""

    content = old_card_pattern.sub(new_card, content)

    # 3. Update querySelector from .product-card to .choice-card
    content = content.replace("querySelectorAll('#shopify-product-grid .product-card')", "querySelectorAll('#shopify-product-grid .choice-card')")
    content = content.replace("querySelectorAll('.product-card')", "querySelectorAll('.choice-card')")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated collection.liquid successfully!')

def update_featured_selection():
    path = 'santos-shopify-theme/sections/featured-selection.liquid'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('class="products-4col-grid"', 'class="choice-grid"')
    content = content.replace('class="product-card"', 'class="choice-card"')
    content = content.replace('class="product-card__thumbnail"', 'class="choice-card__media"')
    content = content.replace('class="product-card__badge"', 'class="choice-card__badge"')
    content = content.replace('class="product-card__img"', 'class="choice-card__img"')
    content = content.replace('class="product-card__quickadd"', 'class="choice-card__quick-add"')
    content = content.replace('class="product-card__content"', 'class="choice-card__info"')
    content = content.replace('class="product-card__title"', 'class="choice-card__title"')
    content = content.replace('class="product-card__price"', 'class="choice-card__price-sale"')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated featured-selection.liquid successfully!')

def update_featured_manteaux():
    path = 'santos-shopify-theme/sections/featured-manteaux.liquid'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('class="product-card"', 'class="choice-card"')
    content = content.replace('class="product-card__thumbnail"', 'class="choice-card__media"')
    content = content.replace('class="product-card__badge"', 'class="choice-card__badge"')
    content = content.replace('class="product-card__img"', 'class="choice-card__img"')
    content = content.replace('class="product-card__quickadd"', 'class="choice-card__quick-add"')
    content = content.replace('class="product-card__content"', 'class="choice-card__info"')
    content = content.replace('class="product-card__title"', 'class="choice-card__title"')
    content = content.replace('class="product-card__price"', 'class="choice-card__price-sale"')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated featured-manteaux.liquid successfully!')

def update_featured_ensembles():
    path = 'santos-shopify-theme/sections/featured-ensembles.liquid'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('class="product-card"', 'class="choice-card"')
    content = content.replace('class="product-card__thumbnail"', 'class="choice-card__media"')
    content = content.replace('class="product-card__badge"', 'class="choice-card__badge"')
    content = content.replace('class="product-card__img"', 'class="choice-card__img"')
    content = content.replace('class="product-card__quickadd"', 'class="choice-card__quick-add"')
    content = content.replace('class="product-card__content"', 'class="choice-card__info"')
    content = content.replace('class="product-card__title"', 'class="choice-card__title"')
    content = content.replace('class="product-card__price"', 'class="choice-card__price-sale"')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated featured-ensembles.liquid successfully!')

if __name__ == '__main__':
    update_collection_liquid()
    update_featured_selection()
    update_featured_manteaux()
    update_featured_ensembles()

