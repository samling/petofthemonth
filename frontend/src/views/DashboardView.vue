<template>
    <div>
      <section>
        <h1>Add new pet</h1>
        <hr/><br/>
  
        <form @submit.prevent="submit">
          <div class="mb-3">
            <label for="name" class="form-label">Name:</label>
            <input type="text" name="name" v-model="form.name" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="description" class="form-label">Description:</label>
            <textarea
              name="description"
              v-model="form.description"
              class="form-control"
            ></textarea>
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </section>
  
      <br/><br/>
  
      <section>
        <h1>Pets</h1>
        <hr/><br/>
  
        <div v-if="pets.length">
          <div v-for="pet in pets" :key="pet.id" class="pets">
            <div class="card" style="width: 18rem;">
              <div class="card-body">
                <ul>
                  <li><strong>Name:</strong> {{ pet.name }}</li>
                  <li><strong>Description:</strong> {{ pet.description }}</li>
                  <li><router-link :to="{name: 'Pet', params:{id: pet.id}}">View</router-link></li>
                </ul>
              </div>
            </div>
            <br/>
          </div>
        </div>
  
        <div v-else>
          <p>Nothing to see. Check back later.</p>
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
          description: '',
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