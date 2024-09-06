<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template id="app">
  <header>
    <div class="d-flex flex-column flex-shrink-0 sidebar-wrap" id="sb">
      <a href="/" class="text-decoration-none logo-wrap">
        <div class="icon-wrap">
          <i class="bi bi-list"></i>
        </div>
        <span>List</span>
      </a>
      <hr>
        <ul class="nav nav-pills flex-column mb-auto">
          <li class="nav-item">
            <a href="/" class="nav-link active" aria-current="page">
              <div class="icon-wrap">
                <i class="bi bi-house-door-fill"></i>
              </div>
              <span>Home</span>
            </a>
          </li>
          <li>
            <a href="/randomdraw" class="nav-link active" aria-current="page">
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
    </div>
  </header>
  <RouterView />
</template>

<style scoped>
.sidebar-wrap {
  border-radius: 10px;
  left: 5%;
  top: 10%;
  width: 60px;
  height: 80%;
  background-color: #000;
  color: #fff;
  padding: 10px;
  transition: 0.8s;
  position: fixed;
  transition: all 1000ms ease;
  z-index: 1;
}
.sidebar-wrap:hover{
  width: 20%;
  opacity:75%;
}
.sidebar-wrap:hover .logo-wrap span, .sidebar-wrap:hover .nav li .nav-link span {
  display: flex;
}
.sidebar-wrap .logo-wrap {
  color: #fff;
  font-size: 35px;
  display: flex;
  align-items: center;
  gap: 10px;
}
.sidebar-wrap .logo-wrap span {
  font-size: 18px;
  font-weight: 1000;
}
.sidebar-wrap .logo-wrap .icon-wrap {
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
.sidebar-wrap a span {
  overflow-x: hidden;
  overflow-y: auto;
  flex-wrap: nowrap;
}
.sidebar-wrap .nav li {
  margin-top: 5px;
}
.sidebar-wrap .nav li .nav-link {
  color: #fff;
  padding: 0;
  font-size: 20px;
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
.sidebar-wrap .nav li .nav-link span {
  font-size: 16px;
  font-weight: 500;
}
.sidebar-wrap .nav li .nav-link.active {
  background-color: #000000;
}
.sidebar-wrap .nav li .nav-link:hover {
  background-color: #aefff8;
  color: #000000;
}
hr{
  border: 1px solid white;
  border-radius: 0.5px;
}
</style>

<script>
</script>
