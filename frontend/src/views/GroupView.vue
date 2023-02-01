<template>
    <div v-if="group">
      <p><strong>Name:</strong> {{ group.name }}</p>
      <p><strong>Description:</strong> {{ group.description }}</p>
      <p><strong>Members:</strong>
        <p v-for='groupUser in group.users'>
          {{ groupUser.username }}
        </p>
      <span><button @click="editGroupUsersToggle()"><span v-if="!editGroupUserState">Add Member</span><span v-else>Close</span></button></span></p>
      <p v-if="editGroupUserState"><strong>Add member:</strong></p>
      <p v-if="editGroupUserState">
      <form @submit="submitGroupUser">
          <div class="mb-3">
            <multiselect
              name="users"
              v-model="form.users"
              :options="groupUsers"
              :custom-label="groupUser"
              track-by="username"
              label="username">
            </multiselect>
            <button type="submit" class="btn btn-primary">Submit</button>
          </div>
      </form>
      </p>
      <p v-else></p>
      <p><strong>Pets:</strong>
        <p v-for='groupPet in group.pets'>
          {{ groupPet.name }}
        </p>
      <span><button @click="editGroupPetsToggle()"><span v-if="!editGroupPetState">Add Pet</span><span v-else>Close</span></button></span></p>
      <p v-if="editGroupPetState"><strong>Add pet:</strong></p>
      <p v-if="editGroupPetState">
      <form @submit="submitGroupPet">
          <div class="mb-3">
            <multiselect
              name="pets"
              v-model="form.pets"
              :options="groupPets"
              :custom-label="groupPet"
              track-by="name"
              label="name">
            </multiselect>
            <button type="submit" class="btn btn-primary">Submit</button>
          </div>
      </form>
      </p>
      <p v-else></p>
  
    <!-- <p><router-link :to="{name: 'EditPet', params:{id: note.id}}" class="btn btn-primary">Edit</router-link></p> -->
    <p><router-link :to="{params:{id: group.id}}" class="btn btn-primary">Edit</router-link></p>
    <p><button @click="removeGroup()" class="btn btn-secondary">Delete</button></p>
    </div>
  </template>
  
  
  <script>
  import axios from 'axios';
  import { defineComponent, ref } from 'vue';
  import { mapGetters, mapActions } from 'vuex';

  import Multiselect from 'vue-multiselect';
  
  export default defineComponent({
    name: 'Group',
    components: { Multiselect },
    props: ['id'],
    async created() {
      try {
        await this.viewGroup(this.id);
      } catch (error) {
        console.error(error);
        this.$router.push('/');
      }
    },
    data() {
      return {
        editGroupUserState: false,
        editGroupPetState: false,
        groupUsers: [this.$store.state.users],
        groupPets: [this.$store.state.pets],
        form: {
          users: [],
          pets: []
        }
      }
    },
    computed: {
      ...mapGetters({ group: 'stateGroup', users: 'stateUsers', pets: 'statePets' }),
    },
    methods: {
      ...mapActions(['viewGroup', 'deleteGroup', 'getUsers', 'getPets', 'addGroupUser', 'addGroupPet', 'removeGroupUser', 'removeGroupPet']),
      async GetAvailableUsers() {
        let availableUserList = []
        let groupUsers = this.group.users.map(v => v.id)
        axios
          .get('users')
          .then(response => {
            for (let i = 0; i < response.data.length; i++) {
              let user_id = response.data[i].id

              if (!new Set(groupUsers).has(user_id)) {
                availableUserList.push(response.data[i])
              }
              this.groupUsers = availableUserList
            }
          })
      },
      async GetAvailablePets() {
        let availablePetList = []
        let groupPets = this.group.pets.map(v => v.id)
        axios
          .get('pets')
          .then(response => {
            for (let i = 0; i < response.data.length; i++) {
              let pet_id = response.data[i].id

              if (!new Set(groupPets).has(pet_id)) {
                availablePetList.push(response.data[i])
              }
              this.groupPets = availablePetList
            }
          })
      },
      groupUser(option) {
        return `${option.username}`
      },
      groupPet(option) {
        return `${option.name}`
      },
      async editGroupUsersToggle() {
        this.editGroupUserState = !this.editGroupUserState
        if (this.editGroupUserState == true) {
          await this.GetAvailableUsers()
        }
      },
      async editGroupPetsToggle() {
        this.editGroupPetState = !this.editGroupPetState
        if (this.editGroupPetState == true) {
          await this.GetAvailablePets()
        }
      },
      async removeGroup() {
        try {
          await this.deleteGroup(this.id);
          this.$router.push('/');
        } catch (error) {
          console.error(error);
        }
      },
      async submitGroupUser() {
        try {
          let group = {
            id: parseInt(this.id),
            user_id: parseInt(this.form.users.id)
          }
          await this.addGroupUser(group)
        } catch (error) {
          console.log(error);
        }
      },
      async submitGroupPet() {
        try {
          let pet = {
            id: parseInt(this.id),
            pet_id: parseInt(this.form.pets.id)
          }
          await this.addGroupPet(pet)
        } catch (error) {
          console.log(error);
        }
      }
    },
  });
  </script>