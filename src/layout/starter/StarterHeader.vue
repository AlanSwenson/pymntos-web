<template>
  <header class="header-global">
    <div style="position: relative">
      <base-nav type="primary" effect="dark" expand>
        <a class="navbar-brand" href="#">
          <i class="fab fa-python fa-2x" style=" vertical-align: middle;"></i>
          <span class="pl-3">pymntos</span>
        </a>

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
          <li class="nav-item">
            <a
              class="nav-link nav-link-icon"
              href="https://www.meetup.com/PyMNtos-Twin-Cities-Python-User-Group/"
            >
              <i class="fab fa-meetup fa-2x"></i>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link nav-link-icon" href="https://github.com/PyMNtos">
              <i class="fab fa-github fa-2x"></i>
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

export default {
  components: {
    BaseNav,
    CloseButton
  }
};
</script>
<style>
</style>
