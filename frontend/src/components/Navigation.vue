<template>
   <div class="container centralize">
      <div class="navigation">
         <div class="navigation-container">
            <router-link to="/" class="logo-link">
               <logo></logo>
            </router-link>
         </div>
      </div>
   </div>
</template>
<script>
import Logo from "@/components/Logo";
export default {
   components: {
      Logo,
   }   
}
</script>
<style>
</style>