let cart = [];

function addToCart(item, qty = 1) {
  const existing = cart.find(i => i.id === item.id);
  if (existing) existing.qty += qty;
  else cart.push({ ...item, qty });
}
