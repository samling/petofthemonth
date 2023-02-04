<template>
    <section>
      <h1>Edit Group</h1>
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
  </template>
  
  <script>
  import { defineComponent, ref } from 'vue';
  import { mapGetters, mapActions } from 'vuex';

  import Multiselect from 'vue-multiselect'
  import Datepicker from '@vuepic/vue-datepicker'
  import '@vuepic/vue-datepicker/dist/main.css'
  import moment from 'moment'
  import axios from 'axios';
  moment.locale('en')

  var now = new Date(Date.now())
  
  export default defineComponent({
    name: 'EditGroup',
    components: { Datepicker, Multiselect },
    props: ['id'],
    data() {
        return {
            groupUsers: [this.$store.state.users],
            form: {
                name: '',
                description: '',
            },
        };
    },
    created: function() {
      this.GetGroup();
    },
    computed: {
      ...mapGetters({ group: 'stateGroup'}),
    },
    methods: {
      ...mapActions(['updateGroup', 'viewGroup']),
      async GetGroup() {
        try {
          await this.viewGroup(this.id);
          this.form.name = this.group.name;
          this.form.description = this.group.description;
        } catch (error) {
          console.error(error);
          this.$router.push('/dashboard');
        }
      },
     async submit() {
        try {
          let group = {
            id: this.id,
            form: this.form,
          }
          await this.updateGroup(group);
          this.$router.push({name: 'Group', params:{id: this.group.id}});
        } catch (error) {
          console.log(error);
        }
      },
    },
  });
  </script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>