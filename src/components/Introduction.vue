<template>
  <div id="introduction" style=" text-align: justify;">
    <div style="margin-top:50px;margin-right: auto;
    margin-left: auto;padding: 50px 15px 0px;max-width: 850px;">
      <h1 style="font-size: 50px; text-align: center;color: #3b6b3b;text-transform: uppercase">
        Interactive Swiss sustainability Map</h1><br><br><br>
      Around the world, countries are trying to reduce their CO2 emissions so that we, future generations and our planet can continue to live and exist without a terrible climate catastrophe. We must make efforts to make our lifestyles, our industries and our society sustainable. This starts with ourselves, our communities, our cantons and our country, Switzerland.<br><br>

      This website is serves to display the progress of Switzerland, its cantons and communes in 3 key sustainability metrics:<br>
      <ul>
        <li>Solar potential usage: share of roof area that is economically and technologically exploitable that already has solar pannels installed.</li>
        <li>Renewable heating share: share of building with renewable heat technologies.</li>
        <li>Electric car share: percentage of electric cars vs combustion cars.</li>
      </ul><br>

      So come take a look and see how your region is doing! Can your region do better? Is your region already a pioneer in sustainable development and an example for the rest of Switzerland?<br>

      Maybe you can contibute to the community yourself by switching to an electric car?<br><br>

      <h2>Interactive map</h2><br>

      Just click on any canton (or then commune) to see the metrics for that region.<br><br>

      Note: the 3 bar charts on the per capita ratio between the selected region and Switzerland (log scale).
    </div>
  </div>
</template>
<script>
export default {
  name: 'Introduction',
  props: {
    msg: String
  }
}
</script>
<style scoped>
</style>
