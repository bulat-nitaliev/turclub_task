<template>
    <div class="trip-card box">
      <figure class="image is-4by3">
        <img 
          :src="trip.photo" 
          class="lazyload" 
          alt="Trip photo"
        >
      </figure>
      <h3 class="title is-5 mt-3">{{ trip.title }}</h3>
      <nuxt-link 
        :to="`/${trip.id}`" 
        class="button is-primary is-fullwidth mt-3"
      >
        Перейти
      </nuxt-link>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      trip: {
        type: Object,
        required: true
      }
    }
  }
  </script>