<script setup>
import { RouterLink, RouterView, useRoute} from 'vue-router'
import { ref, computed } from 'vue'

const isSidebarOpen = ref(false);
const route = useRoute();

const toggleSidebar = () => {
  isSidebarOpen.value = !isSidebarOpen.value;
};
const showSummaryButton = computed(() => {
  return route.name === 'history';
});
const backButton = computed(() => {
  return route.name === 'summary'|| route.name === 'spin';
});
</script>

<template id="app">
  <header>
      <button @click="toggleSidebar" class="btn mobile-menu-button">
        <i class="bi bi-list"></i> 
      </button>

      <h1>{{ route.meta.title || 'Restaurant random picker' }}</h1>
      <div v-if="showSummaryButton" class="summary-button-container">
        <a class="btn btn-dark" href="/summary">Summary</a>
      </div>
      <div v-if="backButton" class="back-button-container">
        <a class="btn btn-dark" onclick="history.back()">Back</a>
      </div>
  </header>
  
  <body>
    <nav class="d-flex flex-column flex-shrink-0 sidebar-wrap" :class="{ 'open': isSidebarOpen }" id="sb">
      <a href="/" class="text-decoration-none logo-wrap">
        <div class="icon-wrap">
          <i class="bi bi-house-door-fill"></i>
        </div>
        <span>Home</span>
      </a>
      <button @click="toggleSidebar" class="btn btn-dark close-button">
        <i class="bi bi-x-lg"></i>
      </button>
      <hr>
        <ul class="nav nav-pills flex-column mb-auto">
          <li>
            <a href="/randompicker" class="nav-link active" aria-current="page">
              <div class="icon-wrap">
                <i class="bi bi-shuffle"></i>
              </div>
              <span>Random draw</span>
            </a>
          </li>
          <li>
            <a href="/history" class="nav-link active" aria-current="page">
              <div class="icon-wrap">
                <i class="bi bi-clock-history"></i>
              </div>
              <span>History</span>
            </a>
          </li>
        </ul>
    </nav>
  </body>
  <RouterView />
</template>

<style scoped>
header {
  display: flex;
  align-items: center;
  justify-content: 20px;
  width: 100%;
}
h1{
  font-size: 50px;
  color: #676780;
  align-content: center;
}
.summary-button-container, .back-button-container {
  margin-left: auto;
}
.btn{
  background-color: #5c6279;
}
.sidebar-wrap .logo-wrap, .mobile-menu-button{
  font-size: 25px;
  display: flex;
  align-items: center;
  gap: 5px;
}
.sidebar-wrap .logo-wrap span {
  font-weight: 500;
  overflow-x: hidden;
  overflow-y: auto;
  flex-wrap: nowrap;
}
.sidebar-wrap .logo-wrap .icon-wrap{
  display: flex;
  align-items: center;
  justify-content: center;
  height: 40px;
  min-width: 40px;
}
.sidebar-wrap .nav{
  height: 100%;
  overflow-x: hidden;
  overflow-y: auto;
  flex-wrap: nowrap;
}
.sidebar-wrap .nav li { 
  margin-top: 10px;
}
.sidebar-wrap .nav li .nav-link { 
  padding: 0;
  font-size: 25px;
  display: flex;
  align-items: center;
  gap: 5px;
}
.sidebar-wrap .nav li .nav-link .icon-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 40px;
  min-width: 40px;
}
.sidebar-wrap .nav li .nav-link.active{
  max-height: 40px;
}
.sidebar-wrap .nav li .nav-link:hover, .close-button:hover{
  background-color: white;
  color: #f4e6de;
}
hr{
  border: 1px solid ;
  border-radius: 0.5px;
}
.sidebar-wrap, .sidebar-wrap .nav li .nav-link.active, .mobile-menu-button{
  background-color: #ff914c;
}
.close-button, .sidebar-wrap .nav li .nav-link, hr, .sidebar-wrap .logo-wrap, .mobile-menu-button{
  color: #fff4ea;
}

@media (min-width: 768px){
  .sidebar-wrap {
    border-radius: 10px;
    left: 5%;
    top: 10%;
    width: 60px;
    height: 80%;
    color: #fff;
    padding: 10px;
    position: fixed;
    transition: width 1000ms ease;
    z-index: 1000; 
  }
  .sidebar-wrap:hover{
    width: 16%;
  }
  .sidebar-wrap .logo-wrap span, 
  .sidebar-wrap .nav li .nav-link span{
    visibility: hidden;
    transition: visibility 3000ms ease-in-out;
  }
  .sidebar-wrap:hover .logo-wrap span,
  .sidebar-wrap:hover .nav li .nav-link span{
    visibility: visible;
    transition: visibility 3000ms ease-in-out;
  }
  .mobile-menu-button, .close-button{
    display: none; 
    cursor: pointer;
  }
  .sidebar-wrap .nav li .nav-link span, .sidebar-wrap .logo-wrap span{
    font-size: 20px;
    font-weight: 500;
  }
  header{
    padding-right: 60px;
    padding-bottom: 10px;
  }
  .summary-button-container .btn, .back-button-container .btn{
    padding: 10px 20px;
    font-size: 20px;
    margin-right: 20px;
  }
}

@media (max-width: 768px){
  .sidebar-wrap {
    width: 50%; 
    height: auto; 
    position: fixed; 
    top: 5%;
    left: 0;
    z-index: 1000; 
    transform: translateX(-100%);
    transition: transform 0.2s ease-in-out;  
    padding: 15px;
    opacity: 95%;
    justify-content: left;
    border-radius: 0 10px 10px 0;
  }

  .sidebar-wrap.open { 
    transform: translateX(0);
  }

  .sidebar-wrap .nav {
    flex-direction: column; 
    align-items: left;
  }
  .sidebar-wrap .nav li .nav-link span, .sidebar-wrap .logo-wrap span{
    font-size: 15px;
    font-weight: 500;
  }
  .sidebar-wrap .nav li {
    margin-bottom: 10px; 
  }
  .mobile-menu-button {
    display: block; 
  }
  .sidebar-wrap a{
    display: flex;
  }
  .mobile-menu-button{
    display: inline-block;
    border-radius: 0 10px 10px 0;
    border: none;
    padding: 5px 10px
  }
  .close-button {
    position: absolute;
    right: 20px;
    background: none;
    border: none;
    padding: 5px;
    font-size: 20px;
    cursor: pointer;
  }
  h1{
    font-size: 33px;
    margin-left: 30px;
    margin-bottom: 0;
  }
  header{
    padding: 20px 0;
    background-color: #f5f0e1;
    border-radius: 8px;
    z-index: 1000;
  }
}
</style>