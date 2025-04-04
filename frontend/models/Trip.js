import { Model, axios } from 'vue-mc'

axios.baseUrl = 'http://localhost:8000';
export default class Trip extends Model {
 
  
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
