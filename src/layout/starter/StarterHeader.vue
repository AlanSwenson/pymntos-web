<template>
  <header class="header-global">
    <div style="position: relative">
      <base-nav class="navbar-main" transparent type effect="light" expand>
        <router-link to="/" class="nav-link text-white">
          <i class="fab fa-python fa-2x" style="vertical-align: middle;"></i>
          <span class="pl-3">pymntos</span>
        </router-link>

        <div class="row" slot="content-header" slot-scope="{closeMenu}">
          <div class="col-6 collapse-brand">
            <a href="https://demos.creative-tim.com/vue-argon-design-system/documentation/">
              <img src="https://demos.creative-tim.com/vue-argon-design-system/img/brand/blue.png" />
            </a>
          </div>
          <div class="col-6 collapse-close">
            <close-button @click="closeMenu"></close-button>
          </div>
        </div>

        <ul class="navbar-nav ml-lg-auto">
          <li class="nav-item nav-link-icon my-auto">
            <router-link to="/events" class="nav-link">Events</router-link>
          </li>
          <li class="nav-item nav-link-icon my-auto">
            <router-link to="/about" class="nav-link">About</router-link>
          </li>
          <li class="nav-item">
            <a
              class="nav-link nav-link-icon"
              href="https://www.meetup.com/PyMNtos-Twin-Cities-Python-User-Group/"
            >
              <i class="fab fa-meetup fa-2x" style="vertical-align: middle;"></i>
            </a>
          </li>
          <li class="nav-item">
            <a
              class="nav-link nav-link-icon"
              href="https://join.slack.com/t/pymntos/shared_invite/zt-f1a5x1mc-Csi9OhofJGM7gaCF5P6BbA"
            >
              <i class="fab fa-slack fa-2x" style="vertical-align: middle;"></i>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link nav-link-icon" href="https://github.com/PyMNtos">
              <i class="fab fa-github fa-2x" style="vertical-align: middle;"></i>
            </a>
          </li>
        </ul>
      </base-nav>
    </div>
  </header>
</template>
<script>
import BaseNav from "@/components/BaseNav";
import CloseButton from "@/components/CloseButton";
import BaseDropdown from "@/components/BaseDropdown";

export default {
  components: {
    BaseNav,
    CloseButton,
    BaseDropdown
  }
};
</script>
<style>
</style>
