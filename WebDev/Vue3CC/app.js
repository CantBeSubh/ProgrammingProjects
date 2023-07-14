const app = Vue.createApp({
    data: () => ({
        product: 'The Final Empire',
        qty: 10,
    }),
    methods: {
        onClick() {
            if (this.qty > 0) this.qty--
            else alert('Out of stock')
        }
    }
})

app.mount('#app')