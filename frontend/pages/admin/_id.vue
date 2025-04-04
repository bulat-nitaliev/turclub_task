<template>
  <div class="container">
    <h1 class="title">{{ tripId ? "Редактирование" : "Создание" }} похода</h1>

    <ValidationObserver v-slot="{ handleSubmit }">
      <b-form
        @submit.prevent="handleSubmit(submit)"
        enctype="multipart/form-data"
      >
        <ValidationProvider
          name="Название"
          rules="required"
          v-slot="{ errors }"
        >
          <b-field
            label="Название"
            :type="errors.length ? 'is-danger' : ''"
            :message="errors"
          >
            <b-input v-model="form.title" />
          </b-field>
        </ValidationProvider>

        <ValidationProvider
          name="Описание"
          rules="required"
          v-slot="{ errors }"
        >
          <b-field
            label="Описание"
            :type="errors.length ? 'is-danger' : ''"
            :message="errors"
          >
            <b-input v-model="form.description" type="textarea" />
          </b-field>
        </ValidationProvider>

        <div class="columns">
          <div class="column">
            <ValidationProvider
              name="Дата начала"
              rules="required"
              v-slot="{ errors }"
            >
              <b-field
                label="Дата начала"
                :type="errors.length ? 'is-danger' : ''"
                :message="errors"
              >
                <b-datepicker v-model="form.start_date" />
              </b-field>
            </ValidationProvider>
          </div>

          <div class="column">
            <ValidationProvider
              name="Дата окончания"
              rules="required"
              v-slot="{ errors }"
            >
              <b-field
                label="Дата окончания"
                :type="errors.length ? 'is-danger' : ''"
                :message="errors"
              >
                <b-datepicker v-model="form.end_date" />
              </b-field>
            </ValidationProvider>
          </div>
        </div>

        <ValidationProvider name="Фото" rules="required" v-slot="{ errors }">
          <b-field
            label="Фото"
            :type="errors.length ? 'is-danger' : ''"
            :message="errors"
          >
            <b-upload v-model="form.photo" accept="image/*">
              <div class="file is-primary">
                <span class="file-cta">
                  <b-icon class="file-icon" icon="upload"></b-icon>
                  <span class="file-label">{{
                    form.photo ? form.photo.name : "Выбрать файл"
                  }}</span>
                </span>
              </div>
            </b-upload>
          </b-field>
        </ValidationProvider>

        <div class="buttons mt-5">
          <button
            type="submit"
            class="button is-primary"
            :disabled="isSubmitting"
          >
            Сохранить
          </button>
          <nuxt-link to="/admin/trips" class="button"> Отмена </nuxt-link>
        </div>
      </b-form>
    </ValidationObserver>
  </div>
</template>

<script>
import Trip from "@/models/Trip";
import { extend } from "vee-validate";
import { required } from "vee-validate/dist/rules";

extend("required", {
  ...required,
  message: "Это поле обязательно",
});

export default {
  props: {
    tripId: {
      type: [String, Number],
      default: null,
    },
  },

  data() {
    return {
      form: {
        title: "",
        description: "",
        start_date: new Date(),
        end_date: new Date(),
        photo: null,
      },
      isSubmitting: false,
    };
  },

  async mounted() {
    if (this.tripId) {
      await this.loadTrip();
    }
  },

  methods: {
    async loadTrip() {
      try {
        // const trip = await new Trip({ id: this.tripId }).fetch()
        const trip = await this.$axios.get(
          `/api/v1/private/trips/${this.tripId}/`
        );
        this.form = { ...trip.data };
      } catch (error) {
        this.showError("Ошибка загрузки данных");
      }
    },

    async submit() {
      this.isSubmitting = true;
      console.log(this.form);

      try {
        const formData = new FormData();
        Object.entries(this.form).forEach(([key, value]) => {
          if (key === "photo" && value instanceof File) {
            formData.append(key, value, value.name);
          } else {
            formData.append(key, value);
          }
        });

        if (this.tripId) {
          // await new Trip({ id: this.tripId }).update(formData)
          await this.$axios.put(`/api/v1/private/trips/${this.tripId}/`);
        } else {
          await this.$axios.post(`/api/v1/private/trips/`, formData);
        }

        this.$router.push("/admin/trips");
      } catch (error) {
        this.showError("Ошибка сохранения");
      }
      this.isSubmitting = false;
    },

    showError(message) {
      this.$buefy.toast.open({
        message,
        type: "is-danger",
      });
    },
  },
};
</script>
