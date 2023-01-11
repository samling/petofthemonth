import axios from 'axios'

const state = {
    points: null,
    point: null
}

const getters = {
    statePoints: state => state.points,
    statePoint: state => state.point
}

const actions = {
    async createPoint({dispatch}, point) {
        await axios.post('points/', point)
        await dispatch('getPoints')
    },

    async getPoints({commit}) {
        let {data} = await axios.get('points')
        commit('setPoints', data)
    },

    async viewPoint({commit}, id) {
        let {data} = await axios.get(`points/${id}`)
        commit('setPoint', data)
    },

    async updatePoint({}, point) {
        await axios.patch(`points/${point.id}`, point.form)
    },

    async deletePoint({}, id) {
        await axios.delete(`points/${id}`)
    }
}

const mutations = {
    setPoints(state, points) {
        state.points = points
    },
    setPoint(state, point) {
        state.point = point
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}