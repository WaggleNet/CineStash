<template lang="pug">
  #app
    b-navbar(variant='dark' type='dark')
      b-navbar-brand CineStash
      b-navbar-nav(style='flex-grow: 1')
        p
      b-navbar-nav.nav
        b-nav-item(to='/projects' exact exact-active-class="active") Projects
        b-nav-item(to='/settings' exact exact-active-class="active") Settings
    router-view.main
</template>

<style lang="scss">
html {
  height: 100%;
}

body {
  height: 100%;
}

#app {
  display: flex;
  flex-direction: column;
  height: 100%;
}

#app > .nav {
  flex-grow: 0;
}

#app > .main {
  flex-grow: 1;
  flex: 1
}

nav.navbar {
  border-bottom: 1px solid rgba(0, 0, 0, 0.125)
}

</style>
