import { Model } from 'vue-mc'


export default class Trip extends Model {
  baseURL() {
    return "http://localhost:8000"
  }

  defaults() {
    return {
      id: null,
      title: '',
      description: '',
      start_date: '',
      end_date: '',
      photo: null
    }
  }

  routes() {
    return {
      fetch: 'private/trips/{id}/',
      save: 'private/trips/',
      update: 'private/trips/{id}/',
      delete: 'private/trips/{id}/'
    }
  }
}
