<template>
    <div class="admin-layout">
      <nav class="navbar is-dark">
        <div class="navbar-brand">
          <div class="navbar-item">
            Панель управления
          </div>
        </div>
  
        <div class="navbar-menu">
          <div class="navbar-start">
            <nuxt-link to="/admin/trips" class="navbar-item">
              Походы
            </nuxt-link>
            <nuxt-link to="/admin/applications" class="navbar-item">
              Заявки
            </nuxt-link>
          </div>
  
          <div class="navbar-end">
            <div class="navbar-item">
              <button class="button is-danger" @click="logout">
                Выйти
              </button>
            </div>
          </div>
        </div>
      </nav>
  
      <div class="container mt-5">
        <nuxt />
      </div>
    </div>
  </template>
  
  <script>
    
  export default {
    middleware: 'auth',
    methods: {
      async logout() {
        await this.$auth.logout()
        this.$router.push('/admin/login')
      }
    }
  }
  </script>