import Vue from "vue";
import Router from "vue-router";
import Header from "./layout/starter/StarterHeader";
import Footer from "./layout/starter/StarterFooter";
import Starter from "./views/Starter.vue";
import About from "./views/About.vue";
import Events from "./views/Events.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "starter",
      components: {
        header: Header,
        default: Starter,
        footer: Footer
      }
    },
    {
      path: "/about",
      name: "about",
      components: {
        header: Header,
        default: About,
        footer: Footer
      }
    },
    {
      path: "/events",
      name: "events",
      components: {
        header: Header,
        default: Events,
        footer: Footer
      }
    }
  ]
});
