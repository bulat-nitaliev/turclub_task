// models/Application.js
import { Model } from "vue-mc";

export default class Application extends Model {
  baseURL() {
    return "http://localhost:8000";
  }
  defaults() {
    return {
      id: null,
      trip: null,
      full_name: "",
      email: "",
      phone: "",
      is_canceled: false,
      created_at: "",
    };
  }

  routes() {
    return {
      update: "/api/v1/private/applications/{id}/",
    };
  }
}
