<template>
    <div v-if="pet">
      <p><strong>Name:</strong> {{ pet.name }}</p>
      <p><strong>Description:</strong> {{ pet.description }}</p>
      <p><strong>Age:</strong> {{ pet.age }}</p>
      <p><strong>DOB:</strong> {{ pet.dob }}</p>
      <p><strong>Height:</strong> {{ pet.height }}</p>
      <p><strong>Weight:</strong> {{ pet.weight }}</p>
      <p><strong>Owners:</strong> <p v-for='petUser in pet.users'>
        {{ petUser.username }}<button type="button" @click="removePetUserByList(petUser.id)">X</button>
      </p>
      <span><button @click="editPetUsersToggle()"><span v-if="!editPetUserState">Add Owner</span><span v-else>Close</span></button></span></p>
      <p v-if="editPetUserState"><strong>Add owner:</strong></p>
      <p v-if="editPetUserState">
      <form @submit="submit">
          <div class="mb-3">
            <multiselect
              name="users"
              v-model="form.users"
              :options="petUsers"
              :custom-label="petUser"
              track-by="username"
              label="username">
            </multiselect>
            <button type="submit" class="btn btn-primary">Submit</button>
          </div>
      </form>
      </p>
      <p v-else></p>
      <p><strong>Groups:</strong> {{ pet.groups }}</p>
      <p><strong>Points:</strong> {{ pet.points }}</p>
  
    <p><router-link :to="{name: 'EditPet', params:{id: pet.id}}" class="btn btn-primary">Edit</router-link></p>
    <p><button @click="removePet()" class="btn btn-secondary">Delete</button></p>
    </div>
  </template>
  
  
  <script>
  import axios from 'axios';
  import { defineComponent, ref } from 'vue';
  import { mapGetters, mapActions } from 'vuex';

  import Multiselect from 'vue-multiselect';
  
  export default defineComponent({
    name: 'Pet',
    components: { Multiselect },
    props: ['id'],
    async created() {
      try {
        await this.viewPet(this.id);
      } catch (error) {
        console.error(error);
        this.$router.push('/');
      }
    },
    data() {
      return {
        editPetUserState: false,
        petUsers: [this.$store.state.users],
        form: {
          users: []
        }
      }
    },
    computed: {
      ...mapGetters({ pet: 'statePet', users: 'stateUsers' }),
    },
    methods: {
      ...mapActions(['viewPet', 'deletePet', 'getUsers', 'addPetUser', 'removePetUser']),
      async GetAvailableUsers() {
        let availableUserList = []
        let petUsers = this.pet.users.map(v => v.id)
        axios
          .get('users')
          .then(response => {
            for (let i = 0; i < response.data.length; i++) {
              let user_id = response.data[i].id
              console.log(user_id)
              console.log(petUsers)

              if (!new Set(petUsers).has(user_id)) {
                availableUserList.push(response.data[i])
              }
            }
            this.petUsers = availableUserList
          })
      },
      petUser(option) {
        return `${option.username}`
      },
      async editPetUsersToggle() {
        this.editPetUserState = !this.editPetUserState
        if (this.editPetUserState == true) {
          await this.GetAvailableUsers()
        }
      },
      async removePetUserByList(user_id) {
        try {
          let pet = {
            id: parseInt(this.id),
            user_id: parseInt(user_id)
          }
          await this.removePetUser(pet);
          window.location.reload();
        } catch (error) {
          console.log(error)
        }
      },
      async removePet() {
        try {
          this.deletePet(this.id);
        } catch (error) {
          console.error(error);
        }
      },
      async submit() {
        try {
          let pet = {
            id: parseInt(this.id),
            user_id: parseInt(this.form.users.id)
          }
          await this.addPetUser(pet);
        } catch (error) {
          console.log(error);
        }
      }
    },
  });
  </script>