<template>
    <section>
      <h1>Edit Pet</h1>
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
        <div class="mb-3">
          <label for="age" class="form-label">Age:</label>
          <input type="text" name="age" v-model="form.age" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="dob" class="form-label">Date of Birth:</label>
            <Datepicker name="dob" v-model="form.dob" @update:model-value="handleAge" auto-apply :close-on-auto-apply="true" :format="format" />
        </div>
        <div class="mb-3">
          <label for="height" class="form-label">Height:</label>
          <input type="text" name="height" v-model="form.height" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="weight" class="form-label">Weight:</label>
          <input type="text" name="weight" v-model="form.weight" class="form-control" />
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </section>
  </template>
  
  <script>
  import { defineComponent, ref } from 'vue';
  import { mapGetters, mapActions } from 'vuex';

  import Datepicker from '@vuepic/vue-datepicker'
  import '@vuepic/vue-datepicker/dist/main.css'
  import moment from 'moment'
  moment.locale('en')

  var now = new Date(Date.now())
  
  export default defineComponent({
    name: 'EditPet',
    components: { Datepicker },
    props: ['id'],
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
                name: '',
                created_date: now,
                age: '',
                dob: this.date,
                height: '',
                weight: '',
                description: ''
            },
        };
    },
    created: function() {
      this.GetPet();
    },
    computed: {
      ...mapGetters({ pet: 'statePet' }),
    },
    methods: {
      ...mapActions(['updateNote', 'viewPet']),
      async submit() {
      try {
        let pet = {
          id: this.id,
          form: this.form,
        };
        await this.updatePet(pet);
        this.$router.push({name: 'Pet', params:{id: this.pet.id}});
      } catch (error) {
        console.log(error);
      }
      },
      async GetPet() {
        try {
          await this.viewPet(this.id);
          this.form.name = this.pet.name;
          this.form.description = this.pet.description;
          this.form.age = this.pet.age;
          this.form.dob = this.pet.dob;
          this.form.height = this.pet.height;
          this.form.weight = this.pet.weight;
        } catch (error) {
          console.error(error);
          this.$router.push('/dashboard');
        }
      }
    },
  });
  </script>