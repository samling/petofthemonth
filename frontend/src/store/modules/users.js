import axios from 'axios'

const state = {
    users: null,
    user: null
}

const getters = {
    stateUsers: state => state.users,
    stateUser: state => state.user
}

const actions = {
    async createUser({dispatch}, user) {
        await axios.post('users/', user)
        await dispatch('getUsers')
    },

    async getUsers({commit}) {
        let {data} = await axios.get('users')
        commit('setUsers', data)
    },

    async viewUser({commit}, id) {
        let {data} = await axios.get(`users/${id}`)
        commit('setUser', data)
    },

    async updateUser({}, user) {
        await axios.patch(`users/${user.id}`, user.form)
    },

    async deleteUser({}, id) {
        await axios.delete(`users/${id}`)
    }
}

const mutations = {
    setUsers(state, users) {
        state.users = users
    },
    setUser(state, user) {
        state.user = user
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}