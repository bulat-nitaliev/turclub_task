<template>
  <div>
    <section class="hero is-info">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">Запланированные походы</h1>
          <div class="field">
            <input
              v-model="searchQuery"
              class="input"
              type="text"
              placeholder="Поиск по названию..."
              @input="filteredTrips"
            />
          </div>
        </div>
      </div>
    </section>

    <div class="container mt-5">
      <div class="columns is-multiline">
        <div v-for="trip in trips" :key="trip.id" class="column is-4">
          <TripCard :trip="trip" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { debounce } from "lodash";
import TripCard from "@/components/public/TripCard.vue";

export default {
  components: {
    TripCard,
  },
  data() {
    return {
      searchQuery: "",
      trips: [],
    };
  },
  methods: {
    filteredTrips() {
      this.trips = this.trips.filter((t) =>
        t.title.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
    async asyncData() {
      try {
        const data = await this.$axios.get("/api/v1/public/trips/");
        console.log(data.data);

        this.trips = data.data;
      } catch (error) {
        return { trips: [] };
      }
    },
  },
  mounted() {
    this.asyncData();
  },
  // mounted() {
  //   this.$lazyLoad.update();
  // },
};
</script>
