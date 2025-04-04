import Vue from "vue";
import { Model } from "vue-mc";



Vue.use({
  install(Vue) {
    Vue.prototype.$Model = Model;
  },
});

// Опционально: Настройка базовой конфигурации
