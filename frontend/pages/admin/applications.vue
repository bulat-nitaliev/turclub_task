<template>
    <div>
      <h1 class="title">Управление заявками</h1>
  
      <b-table
        :data="applications"
        :loading="isLoading"
        paginated
        per-page="20"
      >
        <b-table-column field="id" label="ID" v-slot="props">
          {{ props.row.id }}
        </b-table-column>
  
        <b-table-column field="created_at" label="Дата" v-slot="props">
          {{ formatDate(props.row.created_at) }}
        </b-table-column>
  
        <b-table-column field="full_name" label="Имя" v-slot="props">
          {{ props.row.full_name }}
        </b-table-column>
  
        <b-table-column field="trip.title" label="Поход" v-slot="props">
          {{ props.row.trip_title }}
        </b-table-column>
  
        <b-table-column field="is_canceled" label="Статус" v-slot="props">
          <b-switch 
            v-model="props.row.is_canceled"
            @input="updateStatus(props.row)"
          >
            {{ props.row.is_canceled ? 'Отменена' : 'Активна' }}
          </b-switch>
        </b-table-column>
      </b-table>
    </div>
  </template>
  
  <script>
  import Application from '@/models/Application'
  
  export default {
    data() {
      return {
        applications: [],
        isLoading: false
      }
    },
  
    async mounted() {
      await this.loadApplications()
    },
  
    methods: {
      async loadApplications() {
        this.isLoading = true
        try {
          const response = await this.$axios.get('/api/v1/private/applications/')
          this.applications = response.data
        } catch (error) {
          this.showError('Ошибка загрузки данных')
        }
        this.isLoading = false
      },
  
      async updateStatus(application) {
        try {
          await new Application({ id: application.id }).update({
            is_canceled: application.is_canceled
          })
        } catch (error) {
          this.showError('Ошибка обновления статуса')
        }
      },
  
      formatDate(date) {
        return new Date(date).toLocaleString()
      },
  
      showError(message) {
        this.$buefy.toast.open({
          message,
          type: 'is-danger'
        })
      }
    }
  }
  </script>