<template>
    <div v-if="group">
      <p><strong>Name:</strong> {{ group.name }}</p>
      <p><strong>Description:</strong> {{ group.description }}</p>
      <p><strong>Members:</strong> {{ group.users }}</p>
      <p><strong>Pets:</strong> {{ group.pets }}</p>
  
    <!-- <p><router-link :to="{name: 'EditPet', params:{id: note.id}}" class="btn btn-primary">Edit</router-link></p> -->
    <p><router-link :to="{params:{id: group.id}}" class="btn btn-primary">Edit</router-link></p>
    <p><button @click="removeGroup()" class="btn btn-secondary">Delete</button></p>
    </div>
  </template>
  
  
  <script>
  import { defineComponent } from 'vue';
  import { mapGetters, mapActions } from 'vuex';
  
  export default defineComponent({
    name: 'Group',
    props: ['id'],
    async created() {
      try {
        await this.viewGroup(this.id);
      } catch (error) {
        console.error(error);
        this.$router.push('/');
      }
    },
    computed: {
      ...mapGetters({ group: 'stateGroup' }),
    },
    methods: {
      ...mapActions(['viewGroup', 'deleteGroup']),
      async removeGroup() {
        try {
          await this.deleteGroup(this.id);
          this.$router.push('/');
        } catch (error) {
          console.error(error);
        }
      }
    },
  });
  </script>