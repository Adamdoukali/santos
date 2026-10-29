import re

def update_collection():
    with open('collection.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update .collection-container max-width
    old_css = """    .collection-container {
      width: 100%;
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 20px;
      box-sizing: border-box;
    }"""

    new_css = """    .collection-container {
      width: 100%;
      max-width: 1600px;
      margin: 0 auto;
      padding: 0 16px;
      box-sizing: border-box;
    }"""
    if old_css in content:
        content = content.replace(old_css, new_css)
        print('collection: Updated container max-width')

    # 2. Add marquee ticker before <main class="collection-page"
    ticker_html = """  <!-- CHOICE MARQUEE TICKER (EXACT CHOICEWOMEN) -->
  <div class="choice-ticker" aria-hidden="true">
    <div class="choice-ticker__track">
      <div class="choice-ticker__item">Livraison gratuite à partir de 500 DH d'achat !</div>
      <span class="choice-ticker__separator"></span>
      <div class="choice-ticker__item">Paiement à la livraison partout au Maroc</div>
      <span class="choice-ticker__separator"></span>
      <div class="choice-ticker__item">Échange et remboursement garantis sous 7 jours</div>
      <span class="choice-ticker__separator"></span>
      <div class="choice-ticker__item">Nouvelle Collection Winter 2026-2027</div>
      <span class="choice-ticker__separator"></span>
      <div class="choice-ticker__item">Pièces Couture & Drapés d'Exception</div>
      <span class="choice-ticker__separator"></span>
      <div class="choice-ticker__item">Livraison gratuite à partir de 500 DH d'achat !</div>
      <span class="choice-ticker__separator"></span>
      <div class="choice-ticker__item">Paiement à la livraison partout au Maroc</div>
      <span class="choice-ticker__separator"></span>
      <div class="choice-ticker__item">Échange et remboursement garantis sous 7 jours</div>
      <span class="choice-ticker__separator"></span>
      <div class="choice-ticker__item">Nouvelle Collection Winter 2026-2027</div>
      <span class="choice-ticker__separator"></span>
      <div class="choice-ticker__item">Pièces Couture & Drapés d'Exception</div>
    </div>
  </div>\n\n"""

    target_main = '  <!-- Main Collection Content -->\n  <main class="collection-page" role="main">'
    if target_main in content and 'choice-ticker' not in content:
        content = content.replace(target_main, ticker_html + target_main)
        print('collection: Added marquee ticker')

    # 3. Update filter tabs
    old_tabs = """        <div class="filter-tabs">
          <button class="filter-tab is-active" data-filter="all" onclick="setFilter('all', this)">Tous</button>
          <button class="filter-tab" data-filter="MANTEAUX" onclick="setFilter('MANTEAUX', this)">Manteaux & Trenchs</button>
          <button class="filter-tab" data-filter="ENSEMBLES" onclick="setFilter('ENSEMBLES', this)">Ensembles & Tailleurs</button>
          <button class="filter-tab" data-filter="ROBES" onclick="setFilter('ROBES', this)">Robes</button>
          <button class="filter-tab" data-filter="JEANS" onclick="setFilter('JEANS', this)">Jeans & Denim</button>
        </div>"""

    new_tabs = """        <div class="filter-tabs">
          <button class="filter-tab is-active" data-filter="all" onclick="setFilter('all', this)">
            Tous <span class="tab-count" id="count-all"></span>
          </button>
          <button class="filter-tab" data-filter="MANTEAUX" onclick="setFilter('MANTEAUX', this)">
            Manteaux & Trenchs <span class="tab-count" id="count-manteaux"></span>
          </button>
          <button class="filter-tab" data-filter="ENSEMBLES" onclick="setFilter('ENSEMBLES', this)">
            Ensembles & Tailleurs <span class="tab-count" id="count-ensembles"></span>
          </button>
          <button class="filter-tab" data-filter="ROBES" onclick="setFilter('ROBES', this)">
            Robes & Combinaisons <span class="tab-count" id="count-robes"></span>
          </button>
          <button class="filter-tab" data-filter="JEANS" onclick="setFilter('JEANS', this)">
            Denim & Jeans <span class="tab-count" id="count-jeans"></span>
          </button>
        </div>"""

    if old_tabs in content:
        content = content.replace(old_tabs, new_tabs)
        print('collection: Updated filter tabs')

    # 4. Update grid element
    old_grid = '<div class="product-grid" id="collection-grid"></div>'
    new_grid = '<div class="choice-grid" id="collection-grid"></div>'
    if old_grid in content:
        content = content.replace(old_grid, new_grid)
        print('collection: Updated grid class to choice-grid')

    # 5. Update cod-subtotal to cod-item-price in product item row
    old_cod_price = '<div class="choice-cod-product-price" id="cod-subtotal">0.00 dh</div>'
    new_cod_price = '<div class="choice-cod-product-price" id="cod-item-price">0.00 dh</div>'
    if old_cod_price in content:
        content = content.replace(old_cod_price, new_cod_price, 1)
        print('collection: Updated cod-item-price')

    # 6. Update loadRealCatalog, setFilter, renderProducts
    old_catalog_js = """    async function loadRealCatalog() {
      try {
        const resp = await fetch('santos_real_products.json');
        realProducts = await resp.json();
      } catch (err) {
        console.error('Error fetching santos_real_products:', err);
      }

      const params = new URLSearchParams(window.location.search);
      const filterParam = params.get('filter');
      const titleMap = {
        all: 'Toutes les Pièces',
        MANTEAUX: 'Manteaux & Trenchs Santos',
        ENSEMBLES: 'Ensembles & Tailleurs',
        ROBES: 'Robes & Combinaisons',
        JEANS: 'Denim & Jeans Santos'
      };
      if (filterParam) {
        activeFilter = filterParam;
        document.querySelectorAll('.filter-tab').forEach(t => {
          if (t.dataset.filter === filterParam) t.classList.add('is-active');
          else t.classList.remove('is-active');
        });
        if (titleMap[filterParam]) {
          document.getElementById('page-title').textContent = titleMap[filterParam];
        }
      }

      renderProducts();
      updateCartDisplay();
    }

    function setFilter(category, btn) {
      activeFilter = category;
      document.querySelectorAll('.filter-tab').forEach(b => b.classList.remove('is-active'));
      btn.classList.add('is-active');

      const titleMap = {
        all: 'Toutes les Pièces',
        MANTEAUX: 'Manteaux & Trenchs Santos',
        ENSEMBLES: 'Ensembles & Tailleurs',
        ROBES: 'Robes & Combinaisons',
        JEANS: 'Denim & Jeans Santos'
      };
      document.getElementById('page-title').textContent = titleMap[category] || 'Collection';

      renderProducts();
    }

    function applySorting() {
      renderProducts();
    }

    function renderProducts() {
      const grid = document.getElementById('collection-grid');
      let filtered = (activeFilter === 'all') 
        ? [...realProducts] 
        : realProducts.filter(p => {
            if (activeFilter === 'JEANS') {
              return p.category === 'JEANS' || (p.tags && p.tags.includes('jeans')) || p.title.toLowerCase().includes('jeans') || p.title.toLowerCase().includes('denim');
            }
            return p.category === activeFilter;
          });

      const sortMode = document.getElementById('sort-select').value;
      if (sortMode === 'price-asc') {
        filtered.sort((a, b) => a.price - b.price);
      } else if (sortMode === 'price-desc') {
        filtered.sort((a, b) => b.price - a.price);
      } else if (sortMode === 'name-asc') {
        filtered.sort((a, b) => a.title.localeCompare(b.title));
      }

      document.getElementById('product-count-text').textContent = `Affichage de ${filtered.length} créations Santos`;

      grid.innerHTML = filtered.map((p, idx) => {
        let badge = 'Santos';
        const t = p.title.toLowerCase();
        if (t.includes('manteco')) badge = 'Manteco';
        else if (t.includes('trench') || t.includes('trensh') || t.includes('coat') || t.includes('manteau') || t.includes('doudoune')) badge = 'Manteau';
        else if (t.includes('ensemble') || t.includes('blazer') || t.includes('suit')) badge = 'Ensemble';
        else if (t.includes('robe') || t.includes('dress')) badge = 'Robe';
        else if (t.includes('jeans') || t.includes('denim')) badge = 'Denim';

        return `
        <article class="product-card" onclick="openProductModalByIndex(${realProducts.indexOf(p)})">
          <div class="product-card__thumbnail">
            <span class="product-card__badge">${badge}</span>
            <img class="product-card__img" src="${p.img}" alt="${p.title}" loading="lazy">
            <button class="product-card__quickadd" type="button">Aperçu Rapide</button>
          </div>
          <div class="product-card__content">
            <h3 class="product-card__title">${p.title}</h3>
            <p class="product-card__price">${p.price.toFixed(2)} MAD</p>
          </div>
        </article>
      `;
      }).join('');
    }"""

    new_catalog_js = """    async function loadRealCatalog() {
      try {
        const resp = await fetch('santos_real_products.json');
        realProducts = await resp.json();
        window.realProducts = realProducts;
        window.allProductsData = realProducts;
      } catch (err) {
        console.error('Error fetching santos_real_products:', err);
      }

      // Populate tab counts
      const countAll = document.getElementById('count-all');
      if (countAll) countAll.textContent = `(${realProducts.length})`;
      const countManteaux = document.getElementById('count-manteaux');
      if (countManteaux) countManteaux.textContent = `(${realProducts.filter(p => p.category === 'MANTEAUX').length})`;
      const countEnsembles = document.getElementById('count-ensembles');
      if (countEnsembles) countEnsembles.textContent = `(${realProducts.filter(p => p.category === 'ENSEMBLES').length})`;
      const countRobes = document.getElementById('count-robes');
      if (countRobes) countRobes.textContent = `(${realProducts.filter(p => p.category === 'ROBES').length})`;
      const countJeans = document.getElementById('count-jeans');
      if (countJeans) countJeans.textContent = `(${realProducts.filter(p => (p.category === 'JEANS') || (p.tags && p.tags.includes('jeans')) || p.title.toLowerCase().includes('jean')).length})`;

      const params = new URLSearchParams(window.location.search);
      const filterParam = params.get('filter');
      const titleMap = {
        all: 'Toutes les Pièces',
        MANTEAUX: 'Manteaux & Trenchs Santos',
        ENSEMBLES: 'Ensembles & Tailleurs',
        ROBES: 'Robes & Combinaisons',
        JEANS: 'Denim & Jeans Santos'
      };
      if (filterParam) {
        activeFilter = filterParam;
        document.querySelectorAll('.filter-tab').forEach(t => {
          if (t.dataset.filter === filterParam) t.classList.add('is-active');
          else t.classList.remove('is-active');
        });
        if (titleMap[filterParam]) {
          document.getElementById('page-title').textContent = titleMap[filterParam];
        }
      }

      renderProducts();
      updateCartDisplay();
    }

    function setFilter(category, btn) {
      activeFilter = category;
      document.querySelectorAll('.filter-tab').forEach(b => b.classList.remove('is-active'));
      btn.classList.add('is-active');

      const titleMap = {
        all: 'Toutes les Pièces',
        MANTEAUX: 'Manteaux & Trenchs Santos',
        ENSEMBLES: 'Ensembles & Tailleurs',
        ROBES: 'Robes & Combinaisons',
        JEANS: 'Denim & Jeans Santos'
      };
      document.getElementById('page-title').textContent = titleMap[category] || 'Collection';

      renderProducts();
    }

    function applySorting() {
      renderProducts();
    }

    function renderProducts() {
      const grid = document.getElementById('collection-grid');
      if (!grid) return;

      let filtered = (activeFilter === 'all') 
        ? [...realProducts] 
        : realProducts.filter(p => {
            if (activeFilter.toUpperCase() === 'JEANS') {
              return p.category === 'JEANS' || (p.tags && p.tags.includes('jeans')) || p.title.toLowerCase().includes('jeans') || p.title.toLowerCase().includes('denim') || p.title.toLowerCase().includes('jean');
            }
            return (p.category || '').toUpperCase() === activeFilter.toUpperCase();
          });

      const sortMode = document.getElementById('sort-select') ? document.getElementById('sort-select').value : 'featured';
      if (sortMode === 'price-asc') {
        filtered.sort((a, b) => a.price - b.price);
      } else if (sortMode === 'price-desc') {
        filtered.sort((a, b) => b.price - a.price);
      } else if (sortMode === 'name-asc') {
        filtered.sort((a, b) => a.title.localeCompare(b.title));
      }

      document.getElementById('product-count-text').textContent = `Affichage de ${filtered.length} créations Santos`;

      grid.className = 'choice-grid';

      if (filtered.length === 0) {
        grid.innerHTML = `
          <div style="grid-column: 1/-1; text-align: center; padding: 60px 20px; color: #777;">
            <p style="font-size: 15px; text-transform: uppercase; letter-spacing: 0.05em;">Aucune création trouvée dans cette catégorie.</p>
          </div>
        `;
        return;
      }

      if (typeof createChoiceCardHtml === 'function') {
        grid.innerHTML = filtered.map(p => createChoiceCardHtml(p)).join('');
      } else {
        grid.innerHTML = filtered.map(p => `
          <article class="choice-card" onclick="openProductModalByIndex(${realProducts.indexOf(p)})">
            <div class="choice-card__media">
              <img class="choice-card__img" src="${p.img}" alt="${p.title}" loading="lazy">
              <button class="choice-card__quick-add" type="button">Aperçu Rapide</button>
            </div>
            <div class="choice-card__info">
              <h3 class="choice-card__title">${p.title}</h3>
              <div class="choice-card__price-row">
                <span class="choice-card__price-sale">${p.price.toFixed(2)} dh</span>
              </div>
            </div>
          </article>
        `).join('');
      }
    }"""

    if old_catalog_js in content:
        content = content.replace(old_catalog_js, new_catalog_js)
        print('collection: Updated catalog JS')

    # 7. Enhance selectColor in collection.html
    old_select_color = """    function selectColor(color, chip) {
      selectedModalColor = color;
      document.querySelectorAll('.color-chip').forEach(c => c.classList.remove('is-active'));
      chip.classList.add('is-active');
    }"""

    new_select_color = """    function selectColor(color, chip) {
      selectedModalColor = color;
      document.querySelectorAll('.color-chip').forEach(c => c.classList.remove('is-active'));
      chip.classList.add('is-active');

      if (currentModalProduct && currentModalProduct.colors_data) {
        const cData = currentModalProduct.colors_data.find(c => c.name.toLowerCase() === color.toLowerCase());
        if (cData && currentModalProduct.images && currentModalProduct.images[cData.img_idx]) {
          const targetSrc = currentModalProduct.images[cData.img_idx];
          document.getElementById('modal-img').src = targetSrc;
          const thumbs = document.querySelectorAll('.modal-thumb');
          thumbs.forEach((t, i) => {
            if (i === cData.img_idx) t.classList.add('is-active');
            else t.classList.remove('is-active');
          });
        }
      }
    }"""

    if old_select_color in content:
        content = content.replace(old_select_color, new_select_color)
        print('collection: Updated selectColor')

    with open('collection.html', 'w', encoding='utf-8', newline='') as f:
        f.write(content)
    print('collection.html saved successfully!')

if __name__ == '__main__':
    update_collection()

