<template>
  <div id="form">
    <b-form @submit.prevent="onSubmit">
      <b-form-group
        id="input-group-1"
        label="Number 1:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="number1"
          type="number"
          placeholder="Enter number"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-2"
        label="Number 2:"
        label-for="input-2"
      >
        <b-form-input
          id="input-2"
          v-model="number2"
          type="number"
          placeholder="Enter number"
          required
        ></b-form-input>
      </b-form-group>

      <b-button type="submit" variant="primary">Sum</b-button>

      <b-form-group
        id="input-group-3"
        label="Result:"
        label-for="input-3"
      >
        <b-form-input
          id="input-3"
          v-model="result"
          type="number"
          placeholder="Result"
          disabled
        ></b-form-input>
      </b-form-group>
    </b-form>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        number1: null,
        number2: null,
        result: null,
      }
    },
    methods: {
      onSubmit(event) {
        fetch(
          "http://127.0.0.1:3000/calc",
          {
              method: 'POST',
              headers: {
                  "Content-Type": "application/json"
              },
              body: JSON.stringify(
                  {
                      number1: this.number1,
                      number2: this.number2
                  }
              )
          }
        )
        .catch(e => alert(`Error: ${e}`))
        .then(response => (
          response.ok ?
          response.json().then(data => this.result = data.result)
          : response.text().then(text => alert(`Error: ${JSON.stringify(JSON.parse(text),null,2)}`))
        ))
        // this.$nextTick(null)
      }
    }
  }
</script>


<style>
#form {
  margin: 0;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  width: 100vw;
}
form {
  min-width: 300px;
  max-width: 300px;
  min-height: 200px;
  max-height: 200px;
}
button {
  margin: 5px;
}
</style>



//   <div id="app">
//     <p>Number 1</p>
//     <input type="text" v-on:input="number1 = $event.target.value">
//     <p>Number 2</p>
//     <input type="text" v-on:input="number2 = $event.target.value">
//     <p>Result</p>
//     <input type="text" :value="result" disabled>
//     <div @click="calc">Button</div>
//   </div>
