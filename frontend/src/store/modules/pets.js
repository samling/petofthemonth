import axios from 'axios'

const state = {
    pets: null,
    pet: null
}

const getters = {
    statePets: state => state.pets,
    statePet: state => state.pet
}

const actions = {
    async createPet({dispatch}, pet) {
        await axios.post('pets/', pet)
        await dispatch('getPets')
    },

    async getPets({commit}) {
        let {data} = await axios.get('pets')
        commit('setPets', data)
    },

    async viewPet({commit}, id) {
        let {data} = await axios.get(`pets/${id}`)
        commit('setPet', data)
    },

    async updatePet({}, pet) {
        await axios.patch(`pets/${pet.id}`, pet.form)
    },

    async deletePet({}, id) {
        await axios.delete(`pets/${id}`)
    }
}

const mutations = {
    setPets(state, pets) {
        state.pets = pets
    },
    setPet(state, pet) {
        state.pet = pet
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}