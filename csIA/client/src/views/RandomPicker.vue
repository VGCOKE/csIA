<script>
import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer } from "@vue-leaflet/vue-leaflet";
import axios from 'axios';

export default {
    components: {
        LMap,
        LTileLayer
    },
    data() {
        return {
            zoom: 2,
            isTrayOpen: false,
            selectedDistance: null,
            selectedPrice: null,
            selectedType: null,
            restaurant:[]
        };
    },
    watch: {
        selectedDistance: function(newVal, oldVal) {
        if (newVal && this.selectedPrice && this.selectedType) {
            this.onSubmit();
        }
        },
        selectedPrice: function(newVal, oldVal) {
        if (this.selectedDistance && newVal && this.selectedType) {
            this.onSubmit();
        }
        },
        selectedType: function(newVal, oldVal) {
        if (this.selectedDistance && this.selectedPrice && newVal) {
            this.onSubmit();
        }
        },
    },
    methods: {
        toggleTray() {
            this.isTrayOpen = !this.isTrayOpen;
        },
        onSubmit() {
            if (!this.selectedDistance || !this.selectedPrice || !this.selectedType) {
                return;
            }
            axios.post('/filters', {
                distance: this.selectedDistance,
                price: this.selectedPrice,
                type: this.selectedType
            })
            .then ((res) => {
                console.log('Filters applied:', res.data);
            })
            .catch((err) => {
                console.log(err)
            });
        },
        getRestaurant(){
            axios.get('http://127.0.0.1:5000/')
            .then ((res) => {
                console.log(res.data)
                this.restaurant = res.data.restaurant;
            })
            .catch((err) => {
                console.log(err)
            });
        }
    },
    created(){
        this.getRestaurant();
    }
}
</script>

<template id="randomdraw">
        <div class="container rows-cols-auto">
            <div class="dropdown row">
                <div class="btn-group col">
                    <span type="button" class="btn">Distance:</span>
                    <select class="form-select" v-model="selectedDistance">
                        <option selected disabled>Choose distance</option>
                        <option value="1">200m</option>
                        <option value="2">300m</option>
                        <option value="2">400m</option>
                        <option value="2">500m</option>
                    </select>
                </div>
                <div class="btn-group col">
                    <span type="button" class="btn">Price:</span>
                    <select class="form-select" v-model="selectedPrice">
                        <option selected disabled>Choose price</option>
                        <option value="1">under $50</option>
                        <option value="2">under $65</option>
                        <option value="2">under $80</option>
                        <option value="2">under $100</option>
                    </select>
                </div>
                <div class="btn-group col">
                    <span type="button" class="btn">Type:</span>
                    <select class="form-select" v-model="selectedType">
                        <option selected disabled>Choose type</option>
                        <option value="1">fast food</option>
                        <option value="2">sushi</option>
                        <option value="2">cha chaan tang</option>
                    </select>
                </div>
            </div>
            <div class="map-list row">
                <div id="map" class="map col-8">
                    <l-map ref="map" :useGlobalLeaflet="false" v-model:zoom="zoom" :center="[47.41322, -1.219482]">
                        <l-tile-layer
                            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                            layer-type="base"
                            name="OpenStreetMap"
                        ></l-tile-layer>
                    </l-map>
                </div>
                <button @click="toggleTray" class="btn toggle-tray-button">
                    <i class="bi" :class="{ 'bi-caret-down-fill': isTrayOpen, 'bi-caret-up-fill': !isTrayOpen }"></i> 
                </button>
                <div class="tray tray-content col" :class="{ 'open': isTrayOpen }">
                    <div class="restaurant-list list-group">
                        <a class="list-group-item list-group-item-action active" aria-current="true">
                            <div class="d-flex w-100 justify-content-between">
                                <h5 class="mb-1">Restaurants:</h5>
                                <small>num</small>
                            </div>
                        </a>
                        <a v-for="restaurant, index in restaurant" :key="index" class="list-group-item item">
                            <div class="d-flex w-100 justify-content-between">
                                <h5 class="mb-1">{{ restaurant.name }}</h5>
                            </div>
                            <p class="mb-1">~X mins walk</p>
                            <small class="text-body-secondary">{{ restaurant.distance }}</small>
                        </a>
                    </div>
                    <a href="/spin" class="btn">Spin</a>
                </div>
            </div>
        </div>
</template>

<style>
.container{
    background-color: #eeeee4;
}
.dropdown{
    display: flex;
    align-items: center;
}
.dropdown .btn-group .form-select{
    box-sizing: border-box;
    border: 1px solid #fbebdd;
    border-radius: 0 5px 5px 0;
    box-shadow: 0px 2px 4px rgba(207, 207, 207, 0.1);
    background-color: #fff;
}

.dropdown .btn-group .btn{
    background-color: #fee3b5;
    color: #343a40;
    box-shadow: 0px 2px 4px rgba(220, 220, 220, 0.1);
    border-radius: 5px;
}
.container .map-list .tray .restaurant-list .active{
    border: none;
    background-color: #dcb081;
    color: #343a40;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
    border-radius: 5px;
}
.container .map-list .tray .btn{
    background-color: #8dabad;
    color: white;
}
.dropdown .btn-group .btn:hover, 
.dropdown .btn-group .btn:focus, 
.container .map-list .tray .restaurant-list .active:hover{
    background-color: #fee3b5;
    color: #212529; 
}
.container .map-list .tray .restaurant-list .item{
    box-sizing: border-box;
    border: 1px solid #fbebdd;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
    background-color: #fff;
}



@media (min-width: 768px){
    .dropdown{
        margin-top: 20px;
    }
    .container{
        height: 80%;
    }
    .container .map-list{
        display: flex;
        margin-top: 30px;
        margin-right: 10px;
    }
    #map{
        aspect-ratio: 4/3;
        height: 80%;
    }
    .dropdown .btn-group .btn{
        padding: 8px 12px;
        font-size: 16px;
    }
    .dropdown .btn-group .form-select{
        font-size: 16px;
        padding: 8px 12px;
    }
    .container .map-list .tray .restaurant-list{
        width: 100%;
        overflow-y: auto;
        margin: 10px;
        max-height: 80%;
    }
    .container .map-list .tray .btn{
        width: 100%;
        margin: 10px;
    }
    .container .map-list .toggle-tray-button{
        display: none;
    }
    .container .map-list .tray .restaurant-list h5{
        font-weight: 350;
        font-size: 17px;
    }
    .container .map-list .tray .restaurant-list .active h5{
        font-weight: 500;
    }
    .container .map-list .tray .restaurant-list .active{
        border-radius: 5px 5px 0 0;
    }
}

@media (max-width: 768px){
    body{
        position: relative;
        overflow: auto;
    }
    .container {
        position: fixed;
        width: 100%; 
        bottom: 0;
        z-index: -1;
    }
    #map{
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: calc(100% - 10px);
        z-index: -1;
        padding: 0;
    }
    .container .dropdown{
        position: fixed;
        z-index: 1001;
        bottom: 0;
        width: 100%;
        background-color: rgba(255, 255, 255, 0.9); 
        padding: 10px;
        display: flex;
        align-items: center;
        justify-content: space-between; 
    }
    .container .dropdown .btn-group{
        width: auto;
        margin-bottom: 10px;
    }
    .container .dropdown .btn-group .btn, .dropdown .btn-group .form-select{
        font-size: 13px;
        padding: 5px 9px;
    }
    .container .map-list .toggle-tray-button{
        position: fixed;
        bottom: 55px;
        right: 0;
        z-index: 1001;
        background-color: rgba(255, 255, 255, 0.9); 
        color: #9898b3;
        border-radius: 5px;
        padding: 3px 12px; 
        width: 100%;
        border: none;
    }
    .container .map-list .tray{
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: rgba(255, 255, 255, 0.9);
        padding: 20px; 
        transform: translateY(100%); 
        transition: transform 0.3s ease-in-out;
        z-index: 1000; 
        border-radius: 10px 10px 0 0;
    }
    .container .map-list .tray.open{ 
        transform: translateY(0); 
    }
    .container .map-list .tray-content{
        display: flex;
        flex-direction: column;
        height: 70%; 
        bottom: 65px;
    }
    .container .map-list .tray .restaurant-list{
        flex: 1;
        overflow-y: auto; 
        padding: 15px 25px;
    }
    .container .map-list .tray .restaurant-list h5{
        font-size: 17px;
    }
    .container .map-list .tray .restaurant-list .item{
        font-size: 13px;
    }
    .container .map-list .tray .restaurant-list .item h5{
        font-size: 15px;
    }
    .container .map-list .tray .btn{
        margin: 0 20px;
        box-shadow: #eeeee4 0px -3px 10px;
        z-index: 1001; 
    }
}
</style>