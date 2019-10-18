<template lang="pug">
  #app
    b-navbar
      b-navbar-brand CineStash
      b-navbar-nav.nav
        b-nav-item(to='/projects' exact exact-active-class="active") Projects
        b-nav-item(to='/settings' exact exact-active-class="active") Settings
    router-view.main

</template>

<style lang="scss">
#app {
  display: flex;
  flex-direction: column;
}

#app > .nav {
  flex-grow: 0;
}

#app > .main {
  flex-grow: 1;
}

</style>
