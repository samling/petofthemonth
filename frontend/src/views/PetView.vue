<template>
    <div v-if="pet">
      <p><strong>Name:</strong> {{ pet.name }}</p>
      <p><strong>Description:</strong> {{ pet.description }}</p>
      <p><strong>Age:</strong> {{ pet.age }}</p>
      <p><strong>DOB:</strong> {{ pet.dob }}</p>
      <p><strong>Height:</strong> {{ pet.height }}</p>
      <p><strong>Weight:</strong> {{ pet.weight }}</p>
      <p><strong>Owners:</strong> {{ pet.users }}</p>
      <p><strong>Groups:</strong> {{ pet.groups }}</p>
      <p><strong>Points:</strong> {{ pet.points }}</p>
  
    <!-- <p><router-link :to="{name: 'EditPet', params:{id: note.id}}" class="btn btn-primary">Edit</router-link></p> -->
    <p><router-link :to="{params:{id: pet.id}}" class="btn btn-primary">Edit</router-link></p>
    <p><button @click="removePet()" class="btn btn-secondary">Delete</button></p>
    </div>
  </template>
  
  
  <script>
  import { defineComponent } from 'vue';
  import { mapGetters, mapActions } from 'vuex';
  
  export default defineComponent({
    name: 'Pet',
    props: ['id'],
    async created() {
      try {
        await this.viewPet(this.id);
      } catch (error) {
        console.error(error);
        this.$router.push('/');
      }
    },
    computed: {
      ...mapGetters({ pet: 'statePet' }),
    },
    methods: {
      ...mapActions(['viewPet', 'deletePet']),
      async removePet() {
        try {
          await this.deletePet(this.id);
          this.$router.push('/');
        } catch (error) {
          console.error(error);
        }
      }
    },
  });
  </script>