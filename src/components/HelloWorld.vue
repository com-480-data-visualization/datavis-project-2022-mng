<template>
  <div style=" text-align: justify;">
    <div class="col-12" ref="introduction" style="margin-right: auto;
    margin-left: auto;padding: 50px 15px 75px;max-width: 850px;">
      <div style="text-align: center; font-style: italic;font-weight: bold">
        Interactive map of Switzerland</div><br><br>
      This map is supposed to serve as a visualisation of the current suistanability situation in Switzerland<br><br>
      Keep writing eheh

      <!-- As we will show later some there are multiple topics that show a clear polarization between the two political parties
      We have trained a machine learning model to classify these quotes to the corresponding political party. Our model associates a score that varies from 0 to 1 to each quotation representing the probability that the quote is said by a democrat. -->
    </div>
  </div>
</template>
<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
