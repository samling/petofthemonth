<template>
  <div>
    <section>
      <h1>Add new pet</h1>
      <hr/><br/>

      <form @submit.prevent="submit">
        <div class="mb-3">
          <label for="title" class="form-label">Name:</label>
          <input type="text" name="title" v-model="form.name" class="form-control" />
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </section>

    <br/><br/>

    <section>
      <h1>Pets</h1>
      <hr/><br/>

      <div v-for="pet in pets" :key="pet.id" class="pets">
        <div class="card" style="width: 18rem;">
          <div class="card-body">
            <ul>
              <li><strong>Pet Name:</strong> {{ pet.name }}</li>
              <!-- <li><router-link :to="{name: 'Pet', params:{id: pet.id}}">View</router-link></li> -->
              <li><router-link :to="{params:{id: pet.id}}">View</router-link></li>
            </ul>
          </div>
        </div>
        <br/>
      </div>

    </section>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'Dashboard',
  data() {
    return {
      form: {
        name: '',
        created_date: new Date(Date.parse("2012-04-30T02:15:12.356Z")),
        age: 0,
        dob: new Date(Date.parse("2012-04-30T02:15:12.356Z")),
        height: 0,
        weight: 0,
        description: "string"
      },
    };
  },
  created: function() {
    return this.$store.dispatch('getPets');
  },
  computed: {
    ...mapGetters({ pets: 'statePets'}),
  },
  methods: {
    ...mapActions(['createPet']),
    async submit() {
      await this.createPet(this.form);
    },
  },
});
</script>