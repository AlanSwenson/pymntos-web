<template>
  <footer class="footer has-cards">
    <div class="container">
      <div class="row row-grid align-items-center my-md"></div>
      <hr />
      <div class="row align-items-center justify-content-md-between">
        <div class="col-md-6">
          <div class="copyright">
            &copy; {{year}}
            <a href="#" target="_blank" rel="noopener">pymntos</a> |
            Theme by:
            <a
              href="https://www.creative-tim.com"
              target="_blank"
              rel="noopener"
            >Creative Tim</a>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>
<script>
export default {
  name: "starter-footer",
  data() {
    return {
      year: new Date().getFullYear()
    };
  }
};
</script>
<style>
</style>
