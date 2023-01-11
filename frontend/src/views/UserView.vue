<template>
    <div v-if="user">
      <p><strong>Username:</strong> {{ user.username }}</p>
      <p><strong>First Name:</strong> {{ user.firstname }}</p>
      <p><strong>Last Name:</strong> {{ user.lastname }}</p>
      <p><strong>Description:</strong> {{ user.description }}</p>
      <p><strong>Email:</strong> {{ user.email }}</p>
      <p><strong>Pets:</strong> {{ user.pets }}</p>
      <p><strong>Groups:</strong> {{ user.groups }}</p>
  
    <!-- <p><router-link :to="{name: 'EditPet', params:{id: note.id}}" class="btn btn-primary">Edit</router-link></p> -->
    <p><router-link :to="{params:{id: user.id}}" class="btn btn-primary">Edit</router-link></p>
    <p><button @click="removeUser()" class="btn btn-secondary">Delete</button></p>
    </div>
  </template>
  
  
  <script>
  import { defineComponent } from 'vue';
  import { mapGetters, mapActions } from 'vuex';
  
  export default defineComponent({
    name: 'User',
    props: ['id'],
    async created() {
      try {
        await this.viewUser(this.id);
      } catch (error) {
        console.error(error);
        this.$router.push('/');
      }
    },
    computed: {
      ...mapGetters({ user: 'stateUser' }),
    },
    methods: {
      ...mapActions(['viewUser', 'deleteUser']),
      async removeUser() {
        try {
          await this.deleteUser(this.id);
          this.$router.push('/');
        } catch (error) {
          console.error(error);
        }
      }
    },
  });
  </script>