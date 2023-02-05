<template>
  <div>
    <section>
      <router-link :to="{name: 'AddPet'}">Add Pet</router-link>
    </section>

    <section>
      <h1>My Pets</h1>
      <hr/><br/>
      <div v-for="pet in pets" :key="pet.id" class="pets">
        <div v-for="user in pet.users" :key="pet.id" class="pets">
          <div class="card" v-if="parseInt(this.$store.state.users.user.id) === parseInt(user.id)" style="width: 18rem;">
            <div class="card-body">
              <ul>
                <li><strong>Pet Name:</strong> {{ pet.name }}</li>
                <li><router-link :to="{name: 'Pet', params:{id: pet.id}}">View</router-link></li>
              </ul>
            </div>
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
  name: 'Pets',
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
        age: age,
        dob: this.date,
        height: "",
        weight: "",
        description: ""
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