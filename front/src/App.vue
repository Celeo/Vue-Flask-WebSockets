<template>
<div id="app">
    <h1>{{ msg }}</h1>
    <input v-model="message">
    <button v-on:click="sendMessage()">Send</button>
    <div v-if="logs">
        <hr>
        <p v-for="log in logs">
            {{ log }}
        </p>
    </div>
</div>
</template>

<script>
import Vue from 'vue'
import VueSocketio from 'vue-socket.io'


Vue.use(VueSocketio, 'http://localhost:5000')

export default {
    data () {
        return {
            message: '',
            logs: []
        }
    },
    sockets: {
        connect: function() {
            console.log('Connected to the backend web socket server')
        },
        disconnect: function() {
            console.log('Disconnected from the backend web socket server')
        },
        event: function(data) {
            console.log('Got event: ' + data.message)
        },
        response: function(data) {
            console.log('Got response: ' + data.message)
            this.logs.push(data.message)
        }
    },
    methods: {
        sendMessage: function() {
            this.$socket.emit('event', this.message)
            console.log('Sent "' + this.message + '" to the backend')
            this.message = ''
        }
    }
}
</script>
