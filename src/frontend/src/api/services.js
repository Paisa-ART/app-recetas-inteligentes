import api from './client';

export const authService = {
  register: (userData) =>
    api.post('/auth/users/register/', userData),

  login: (username, password) =>
    api.post('/auth/users/login/', { username, password }),

  logout: () =>
    api.post('/auth/users/logout/'),

  getProfile: () =>
    api.get('/auth/users/me/'),

  updateProfile: (userData) =>
    api.patch('/auth/users/me/', userData),
};

export const recipeService = {
  // Recetas
  getRecipes: (params) =>
    api.get('/recipes/', { params }),

  getRecipe: (id) =>
    api.get(`/recipes/${id}/`),

  createRecipe: (data) =>
    api.post('/recipes/', data),

  updateRecipe: (id, data) =>
    api.patch(`/recipes/${id}/`, data),

  deleteRecipe: (id) =>
    api.delete(`/recipes/${id}/`),

  // Ajuste de porciones
  adjustPortions: (recipeId, portions) =>
    api.post(`/recipes/${recipeId}/adjust_portions/`, { portions }),

  // Lista de compras
  generateShoppingList: (recipeId, portions) =>
    api.post(`/recipes/${recipeId}/generate_shopping_list/`, { portions }),

  getShoppingLists: (params) =>
    api.get('/recipes/shopping-lists/', { params }),

  getShoppingList: (id) =>
    api.get(`/recipes/shopping-lists/${id}/`),

  exportShoppingListPDF: (id) =>
    api.get(`/recipes/shopping-lists/${id}/export_pdf/`),

  // Favoritas
  addFavorite: (recipeId) =>
    api.post(`/recipes/${recipeId}/favorite/`),

  removeFavorite: (recipeId) =>
    api.delete(`/recipes/${recipeId}/favorite/`),

  getFavorites: () =>
    api.get('/recipes/favorites/'),

  getMyRecipes: () =>
    api.get('/recipes/?my_recipes=true'),
};
