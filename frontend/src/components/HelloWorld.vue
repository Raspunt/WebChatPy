<template>
  <div class="hello">
    <p>
    Меня зовут Кира Йошикаге.
     Мне 33 года.
      Мой дом находится в северо-восточной части Морио,
       где расположены все виллы.
        Я не женат.
         Я работаю в универмаге Kame Yu и прихожу домой не позднее 8 вечера.
          Я не курю, но иногда выпиваю. Я ложусь спать в 11 вечера,
           и убеждаюсь, что я получаю ровно восемь часов сна,
            несмотря ни на что.
             Выпив стакан теплого молока и потянувшись минут двадцать перед сном,
              я обычно без проблем сплю до утра. Словно ребёнок я просыпаюсь утром без всякой усталости и стресса.
               На моём последнем осмотре мне сказали, что у меня нет никаких проблем со здоровьем.
                Я пытаюсь донести,
                 что я обычный человек,
                  который хочет жить спокойной жизнью.
                   Я забочусь о том, чтобы не утруждать себя какими-либо врагами – победами и поражениями,
                    которые могли бы потревожить мой сон.
                     Вот как я отношусь к обществу, и я знаю,
                      что это приносит мне счастье.
                       Хотя, если бы мне пришлось сражаться, я бы никому не проиграл. 

    </p>

    <h1>{{ msg }}</h1>
     <div v-for="d in data" :key="d">
       {{ d }} 
      </div>
  </div>
</template>

<script>

import axios from 'axios'
let Jsondata ;


  axios.get("/jsonData").then((response)=>{
  Jsondata =  response.data
  alert(response.data)

})



export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data(){
    return {
      "data":Jsondata
    }
  },

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
