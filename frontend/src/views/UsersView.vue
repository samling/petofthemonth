<template>
  <div>
    <section>
      <h1>Add new user</h1>
      <hr/><br/>

      <form @submit.prevent="submit">
        <div class="mb-3">
          <label for="name" class="form-label">Name:</label>
          <input type="text" name="name" v-model="form.name" class="form-control" />

          <label for="description" class="form-label">Description:</label>
          <input type="text" name="description" v-model="form.description" class="form-control" />

          <label for="email" class="form-label">Email:</label>
          <input type="text" name="email" v-model="form.email" class="form-control" />

          <label for="password" class="form-label">Password:</label>
          <input type="text" name="password" v-model="form.password" class="form-control" />

        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </section>

    <br/><br/>

    <section>
      <h1>Users</h1>
      <hr/><br/>

      <div v-for="user in users" :key="user.id" class="users">
        <div class="card" style="width: 18rem;">
          <div class="card-body">
            <ul>
              <li><strong>Username:</strong> {{ user.name }}</li>
              <li><router-link :to="{name: 'User', params:{id: user.id}}">View</router-link></li>
            </ul>
          </div>
        </div>
        <br/>
      </div>

    </section>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue'
import { mapGetters, mapActions } from 'vuex'

import Datepicker from '@vuepic/vue-datepicker'
import '@vuepic/vue-datepicker/dist/main.css'
import moment from 'moment'
moment.locale('en')

import { deAT } from 'date-fns/locale';

var now = new Date(Date.now())

export default defineComponent({
  name: 'Users',
  components: { Datepicker },
  setup() {
    const date = ref(new Date())
    const format = (date) => {
      const day = date.getDate()
      const month = date.getMonth() + 1
      const year = date.getFullYear()

      return `${month}/${day}/${year}`
    }

    return {
      date,
      format
    }
  },
  data() {
    var age = ref()
    age.value=""

    const handleAge = (modelData) => {
      var DOB_ms = new Date(modelData).getTime()
      var dob_diff = Date.now() - DOB_ms
      age.value = moment.duration(dob_diff).years()
    }
 
    return {
      handleAge,
      form: {
        name: "",
        created_date: now,
        email: "",
        password: "",
        description: ""
      },
    };
  },
  created: function() {
    return this.$store.dispatch('getUsers');
  },
  computed: {
    ...mapGetters({ users: 'stateUsers'}),
  },
  methods: {
    ...mapActions(['createUser']),
    async submit() {
      await this.createUser(this.form);
    },
  },
});
</script>