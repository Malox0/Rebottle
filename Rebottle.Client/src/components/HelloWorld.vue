<script lang="ts" setup>
import {ref} from "vue";
import axios from "axios";
defineProps<{
  msg: string

}>()
const   rules =  [
  (value :any) => !value || value.type == 'text/jpeg' || value.type == 'text/png' || 'Only PNG/JPG files allowed'
]

function apicall(){
  if(file.value != null){
    let formData = new FormData();
    formData.append("file", file.value);
    axios.post("localhost:5000/upload", formData, {
      headers: {
        "Content-Type": "multipart/form-data"
      }
    }).then((resp: any) => {
      console.log(resp);

    });
  }

}

let file = ref(null)
</script>

<template>
  <div class="greetings">
    <div class="headings">
      <div class="heading-wrapper">
      <h1 class="green">{{ msg }}
      </h1>
        <v-img
            :width="250"
            aspect-ratio="16/9"
            cover
            src="src/assets/rebottle_logo.png"
            id="logo"
        ></v-img>
      </div>
      <div class="heading-wrapper">
      <h3>
        Reuse. Recycle.

      </h3>
      <h3 class="green">Rebottle.</h3>
      </div>

      <v-file-input  v-model="file" accept="image/png, image/jpeg" id="file-input" label="Input your file here" small-chips ></v-file-input>
    </div>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 10rem;
}

h3 {
  top: -35px;
  font-size: 3.7rem;
  left: 0;

}

#logo{
  top: 5px;
  left: -17px;
}
.headings {
  position: absolute;
  display: flex;
  flex-direction: column;
  margin-left: 0 !important;
  margin-top: 0 !important;
  top: 0;
}

.heading-wrapper{
  top: -10px;
  left: -6px;
  width: 100%;
  display: inline-flex;
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
