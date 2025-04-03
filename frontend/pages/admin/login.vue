<template>
    <div class="container">
      <div class="columns is-centered">
        <div class="column is-4">
          <div class="box">
            <h1 class="title has-text-centered">Авторизация</h1>
  
            <ValidationObserver v-slot="{ handleSubmit }">
              <form @submit.prevent="handleSubmit(login)">
                <ValidationProvider name="Логин" rules="required" v-slot="{ errors }">
                  <b-field 
                    label="Логин"
                    :type="errors.length ? 'is-danger' : ''"
                    :message="errors"
                  >
                    <b-input v-model="form.username" />
                  </b-field>
                </ValidationProvider>
  
                <ValidationProvider name="Пароль" rules="required" v-slot="{ errors }">
                  <b-field
                    label="Пароль"
                    :type="errors.length ? 'is-danger' : ''"
                    :message="errors"
                  >
                    <b-input v-model="form.password" type="password" />
                  </b-field>
                </ValidationProvider>
  
                <b-button 
                  native-type="submit" 
                  type="is-primary" 
                  expanded
                  :loading="isLoading"
                >
                  Войти
                </b-button>
              </form>
            </ValidationObserver>
          </div>
        </div>
      </div>
    </div>
  </template>
  
<script>
import { required } from 'vee-validate/dist/rules'
import { extend } from 'vee-validate'

extend('required', {
  ...required,
  message: 'Это поле обязательно'
})
  export default {
    auth: 'guest',
    data() {
      return {
        form: {
          username: '',
          password: ''
        },
        isLoading: false
      }
    },
    methods: {
      async login() {
        this.isLoading = true
        try {
          await this.$auth.loginWith('local', { data: this.form })
          this.$router.push('/admin/trips')
        } catch (error) {
          this.$buefy.toast.open({
            message: 'Ошибка авторизации',
            type: 'is-danger'
          })
        }
        this.isLoading = false
      }
    }
  }
  </script>