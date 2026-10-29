// Minimal DOM mock to test choice-reverse.js
const fs = require('fs');

global.window = global;
global.document = {
  readyState: 'complete',
  addEventListener: () => {},
  getElementById: (id) => {
    return {
      style: {},
      classList: { add: () => {}, remove: () => {} },
      setAttribute: () => {},
      addEventListener: () => {},
      textContent: '',
      innerHTML: '',
      value: ''
    };
  },
  querySelectorAll: () => [],
  querySelector: () => ({ style: {} }),
  body: { style: {} }
};

global.fetch = async (url) => {
  const data = fs.readFileSync(url, 'utf8');
  return {
    json: async () => JSON.parse(data)
  };
};

try {
  require('../choice-reverse.js');
  console.log('choice-reverse.js loaded into Node successfully!');
  console.log('Exported window functions:', {
    createChoiceCardHtml: typeof window.createChoiceCardHtml,
    openCodCheckout: typeof window.openCodCheckout,
    cycleCardImage: typeof window.cycleCardImage,
    switchCardColor: typeof window.switchCardColor,
    renderChoiceSection: typeof window.renderChoiceSection,
    setChoiceCategory: typeof window.setChoiceCategory,
    toggleChoiceShowAll: typeof window.toggleChoiceShowAll
  });

  const products = JSON.parse(fs.readFileSync('santos_real_products.json', 'utf8'));
  const cardHtml = window.createChoiceCardHtml(products[0]);
  console.log('Sample card generated successfully! Length:', cardHtml.length);
} catch (err) {
  console.error('Test error:', err);
  process.exit(1);
}
