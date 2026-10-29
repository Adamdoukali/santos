import re

def update_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Denim & Jeans tab count
    old_jeans = """        <button class="choice-filter-tab" type="button" onclick="setChoiceCategory('JEANS', this)">
          Denim & Jeans
        </button>"""
    new_jeans = """        <button class="choice-filter-tab" type="button" onclick="setChoiceCategory('JEANS', this)">
          Denim & Jeans <span class="tab-count" id="count-jeans">(1)</span>
        </button>"""

    if old_jeans in content:
        content = content.replace(old_jeans, new_jeans)
        print('index: Updated jeans tab')

    # 2. Update cod-subtotal to cod-item-price in product item row
    old_cod_price = '<div class="choice-cod-product-price" id="cod-subtotal">0.00 dh</div>'
    new_cod_price = '<div class="choice-cod-product-price" id="cod-item-price">0.00 dh</div>'
    if old_cod_price in content:
        content = content.replace(old_cod_price, new_cod_price, 1)
        print('index: Updated cod-item-price')

    # 3. Enhance selectColor
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
        print('index: Updated selectColor')

    with open('index.html', 'w', encoding='utf-8', newline='') as f:
        f.write(content)
    print('index.html saved successfully!')

if __name__ == '__main__':
    update_index()

