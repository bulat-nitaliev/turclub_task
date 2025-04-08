<template>
  <div>
    <div class="level">
      <div class="level-left">
        <h1 class="title">Управление походами</h1>
      </div>
      <div class="level-right">
        <nuxt-link to="/admin/new" class="button is-primary">
          Создать поход
        </nuxt-link>
      </div>
    </div>

    <b-table :data="trips" :loading="isLoading" paginated per-page="10">
      <b-table-column field="id" label="ID" v-slot="props">
        {{ props.row.id }}
      </b-table-column>

      <b-table-column field="title" label="Название" v-slot="props">
        {{ props.row.title }}
      </b-table-column>

      <b-table-column field="dates" label="Даты" v-slot="props">
        {{ formatDate(props.row.start_date) }} -
        {{ formatDate(props.row.end_date) }}
      </b-table-column>

      <b-table-column label="Действия" v-slot="props">
        <div class="buttons">
          <nuxt-link
            :to="`/admin/${props.row.id}`"
            class="button is-info is-small"
          >
            Редактировать
          </nuxt-link>
          <button
            class="button is-danger is-small"
            @click="deleteTrip(props.row.id)"
          >
            Удалить
          </button>
        </div>
      </b-table-column>
    </b-table>
  </div>
</template>

<script>
import Trip from "@/models/Trip";

export default {
  layout: 'admin',
  data() {
    return {
      trips: [],
      isLoading: false,
    };
  },

  async mounted() {
    await this.loadTrips();
  },

  methods: {
    async loadTrips() {
      this.isLoading = true;
      try {
        const response = await this.$axios.get("/api/v1/private/trips/");
        this.trips = response.data;
      } catch (error) {
        this.showError("Ошибка загрузки данных");
      }
      this.isLoading = false;
    },

    async deleteTrip(id) {
      this.$buefy.dialog.confirm({
        message: "Удалить поход?",
        onConfirm: async () => {
          try {
            // const trip = new Trip({ id })
            // await trip.delete()
            await this.$axios.delete(`/api/v1/private/trips/${id}/`)
            
            // await new Trip({ id }).delete();
            await this.loadTrips();
          } catch (error) {
            this.showError("Ошибка удаления");
          }
        },
      });
    },

    formatDate(date) {
      return new Date(date).toLocaleDateString();
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
