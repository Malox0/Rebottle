<script lang="ts" setup>
defineProps<{
  msg: string
}>()
</script>

<template>
  <div class="greetings">
    <div class="headings">
      <h1 class="green">{{ msg }}</h1>
      <h3>
        Reuse Recycle
        <a href="https://vitejs.dev/" rel="noopener" target="_blank">Rebottle</a>
      </h3>
      <v-file-input id="file-input" label="Input your file here" small-chips></v-file-input>
    </div>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 10rem;
  top: -10px;
  left: -6px;
}

h3 {
  top: -35px;
  font-size: 3.7rem;
  left: 0;

}

.headings {
  position: absolute;
  display: flex;
  flex-direction: column;
  margin-left: 0 !important;
  margin-top: 0 !important;
  top: 0;
}

.greetings {
  top: 0;
  left: 30px;
  margin-top: 0 !important;
  margin-left: 0 !important;
  width: 100vw;
  height: 80vh;
  position: fixed
}

.greetings h1,
.greetings h3 {
  text-align: left;
  margin-left: 2px;
  padding-left: 2px;
}


#file-input {
  margin-left: 0 !important;
  left: 0 !important;
  padding-left: 0 !important;
}
</style>
