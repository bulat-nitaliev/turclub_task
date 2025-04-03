<template>
    <div class="container">
      <div v-if="trip" class="columns">
        <div class="column is-6">
          <img :src="trip.photo" class="image" alt="Trip photo">
          <h2 class="title is-3">{{ trip.title }}</h2>
          <p class="content">{{ trip.description }}</p>
        </div>
  
        <div class="column is-6">
          <ValidationObserver v-slot="{ handleSubmit }">
            <form @submit.prevent="handleSubmit(submitForm)">
              <ValidationProvider 
                name="Имя" 
                rules="required|min:3"
                v-slot="{ errors }"
              >
                <b-field 
                  label="Полное имя"
                  :type="errors.length ? 'is-danger' : ''"
                  :message="errors[0]"
                >
                  <b-input v-model="form.full_name" />
                </b-field>
              </ValidationProvider>
  
              <ValidationProvider 
                name="Email"
                rules="required|email"
                v-slot="{ errors }"
              >
                <b-field
                  label="Email"
                  :type="errors.length ? 'is-danger' : ''"
                  :message="errors[0]"
                >
                  <b-input v-model="form.email" type="email" />
                </b-field>
              </ValidationProvider>
  
              <ValidationProvider 
                name="Телефон"
                rules="required|phone"
                v-slot="{ errors }"
              >
                <b-field
                  label="Телефон"
                  :type="errors.length ? 'is-danger' : ''"
                  :message="errors[0]"
                >
                  <b-input v-model="form.phone" type="tel" />
                </b-field>
              </ValidationProvider>
  
              <b-button 
                native-type="submit" 
                type="is-primary" 
                expanded
                :loading="isSubmitting"
              >
                Отправить заявку
              </b-button>
            </form>
          </ValidationObserver>
        </div>
      </div>
  
      <b-modal v-model="showSuccessModal">
        <div class="content has-text-centered">
          <h3 class="title is-4">Спасибо за заявку!</h3>
          <p>Мы свяжемся с вами в ближайшее время</p>
        </div>
      </b-modal>
    </div>
  </template>
  
  <script>
import { extend } from 'vee-validate'
import { required, email, min } from 'vee-validate/dist/rules'

extend('required', {
  ...required,
  message: 'Это поле обязательно'
})

extend('email', {
  ...email,
  message: 'Некорректный email'
})

extend('min', {
  ...min,
  message: 'Минимальная длина - {length} символов'
})

extend('phone', value => {
  const pattern = /^89[0-9]{9}$/
  return pattern.test(value) || 'Некорректный номер телефона'
})
  
  export default {
    
  
    data() {
      return {
        trip: null,
        form: {
          full_name: '',
          email: '',
          phone: ''
        },
        isSubmitting: false,
        showSuccessModal: false
      }
    },
  
    async asyncData({ $axios, params }) {
      try {
        const { data } = await $axios.get(`/api/v1/public/trips/${params.id}/`)
        return { trip: data }
      } catch (error) {
        return { trip: null }
      }
    },
  
    methods: {
      async submitForm() {
        this.isSubmitting = true
        try {
          const data = await this.$axios.post('/api/v1/public/applications/', {
            ...this.form,
            trip: this.trip.id
          })
          console.log(data.data);
          
          this.form = {
            full_name: '',
            email: '',
            phone: ''
          }
          
          this.showSuccessModal = true
        } catch (error) {
          this.$buefy.toast.open({
            message: 'Ошибка при отправке заявки',
            type: 'is-danger'
          })
        }
        this.isSubmitting = false
      }
    }
  }
  </script>