import Vue from "vue";
import { ValidationProvider, ValidationObserver } from "vee-validate";
import { localize } from "vee-validate";
import ru from "vee-validate/dist/locale/ru.json";

// Activate the Arabic locale.
localize("ru", ru);
Vue.component("ValidationProvider", ValidationProvider);
Vue.component("ValidationObserver", ValidationObserver);


// import { extend } from 'vee-validate'
// import { required, email, min } from 'vee-validate/dist/rules'



// extend('email', {
//   ...email,
//   message: 'Некорректный email'
// })

// extend('min', {
//   ...min,
//   message: 'Минимальная длина - {length} символов'
// })

// extend('phone', value => {
//   const pattern = /^\+?[0-9]{7,15}$/
//   return pattern.test(value) || 'Некорректный номер телефона'
// })