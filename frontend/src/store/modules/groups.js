import axios from 'axios'

const state = {
    groups: null,
    group: null
}

const getters = {
    stateGroups: state => state.groups,
    stateGroup: state => state.group
}

const actions = {
    async createGroup({dispatch}, group) {
        await axios.post('groups/', group)
        await dispatch('getGroups')
    },

    async getGroups({commit}) {
        let {data} = await axios.get('groups')
        commit('setGroups', data)
    },

    async viewGroup({commit}, id) {
        let {data} = await axios.get(`group/${id}`)
        commit('setGroup', data)
    },

    async updateGroup({}, group) {
        await axios.patch(`group/${group.id}`, group.form)
    },

    async deleteGroup({}, id) {
        await axios.delete(`group/${id}`)
    }
}

const mutations = {
    setGroups(state, groups) {
        state.groups = groups
    },
    setGroup(state, group) {
        state.group = group
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}