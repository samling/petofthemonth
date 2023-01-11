<template>
  <div>
    <section>
      <h1>Add new pet</h1>
      <hr/><br/>

      <form @submit.prevent="submit">
        <div class="mb-3">
          <label for="name" class="form-label">Name:</label>
          <input type="text" name="name" v-model="form.name" class="form-control" />

          <label for="description" class="form-label">Description:</label>
          <input type="text" name="description" v-model="form.description" class="form-control" />

          <label for="age" class="form-label">Age:</label>
          <input type="text" name="age" v-model="form.age" class="form-control" />

          <label for="dob" class="form-label">Date of Birth:</label>
          <Datepicker name="dob" v-model="form.dob" @update:model-value="handleAge" class="form-control" auto-apply :close-on-auto-apply="true" :format="format" />

          <label for="height" class="form-label">Height:</label>
          <input type="text" name="height" v-model="form.height" class="form-control" />

          <label for="weight" class="form-label">Weight:</label>
          <input type="text" name="weight" v-model="form.weight" class="form-control" />

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
              <li><router-link :to="{name: 'Pet', params:{id: pet.id}}">View</router-link></li>
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
        created_date: now,
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