<script>
import axios from 'axios';
import { LMap, LTileLayer } from "@vue-leaflet/vue-leaflet";
export default{
    name:'_history',
    components: {
        LMap,
        LTileLayer
    },
    data(){
        return {
            zoom: 2,
            history:[],
            details:[]
        };
    },
    methods: {
        getHistory(){
            axios.get('http://127.0.0.1:5000/history')
            .then ((res) => {
                console.log(res.data)
                this.history = res.data.history;
            })
            .catch((err) => {
                console.log(err)
            });
        },
        getDetails(placeid){
            axios.get(`http://127.0.0.1:5000/history/${placeid}`)
            .then ((res) => {
                console.log(res.data)
                this.details = res.data;
            })
            .catch((err) => {
                console.log(err)
            });
        }
    },
    created(){
        this.getHistory();
    }
}
</script>

<template id="history">
    <div class="container rows-cols-auto">
        <div class="table-list row">
            <table class="table table-borderless table-striped table-hover">
                <thead class="table">
                    <tr>
                        <th scope="col">DateTime</th>
                        <th scope="col">Restaurant name</th>
                        <th scope="col">Address</th>
                    </tr>
                </thead>
                <tbody class="table-group-divider">
                    <tr v-for="history, index in history" :key="index" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
                        <td>{{ history.dateT}}</td>
                        <td @click=getDetails(history.placeid)>{{ history.name}}</td> 
                        <td>{{ history.address}}</td>
                    </tr>
                </tbody>
            </table>
            <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="staticBackdropLabel">Details</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <p><strong>Date:</strong> {{ details.dateT }}</p>
                            <p><strong>Name:</strong> {{ details.name }}</p>
                            <p><strong>Address:</strong> {{ details.address }}</p>
                            <div class="map">
                                <l-map ref="map" :useGlobalLeaflet="false" v-model:zoom="zoom" :center="[47.41322, -1.219482]">
                                    <l-tile-layer
                                        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                                        layer-type="base"
                                        name="OpenStreetMap"
                                    ></l-tile-layer>
                                </l-map>
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            </div>
            <div class="page-scroll">
                <nav aria-label="Page navigation example">
                    <ul class="pagination justify-content-center">
                        <li class="page-item" :class="{ disabled: currentPage === 1 }">
                            <a class="page-link" href="#" @click.prevent="goToPage(currentPage - 1)">Previous</a>
                        </li>
                        <li class="page-item" v-for="page in totalPages" :key="page" :class="{ active: currentPage === page }">
                            <a class="page-link" href="#" @click.prevent="goToPage(page)">{{ page }}</a>
                        </li>
                        <li class="page-item" :class="{ disabled: currentPage === totalPages }">
                            <a class="page-link" href="#" @click.prevent="goToPage(currentPage + 1)">Next</a>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
    </div>
</template>

<style scoped>
.container .table-list{
    background-color: #f4e7d2; 
    padding: 40px;
    border-radius: 20px;
}
.container .table-list .table .table th{
    background-color: #e7b99a;
    color: #000000;
    font-weight: 500;
}
tbody:hover{
    background-color: #8dabad;
    color: #ffffff;
}
.container .table-list .table .table-group-divider zootd{
    background-color: #eeeee4;
    color: #454649;
}
.container .table-list .table .table-group-divider button{
    background-color: #8dabad;
    color: white;
}
.container .table-list .table .table-group-divider button:hover{
    background-color: rgb(85, 85, 85);
    color: #fbebdd;
    border: none;
}
.container .table-list .page-scroll{
    margin-top: 20px;
}
.container .table-list .page-scroll a{
    color: #424242;
}

@media (min-width: 768px){
    .container .table-list{
        top: 10%;
        bottom: 10%;
        height: 100%;
    }
}
@media (max-width: 768px){
    *{
        background-color: #fff5ee;
    }
    .container{
        top: 10%;
        bottom: 10%;
        height: 100%;
    }
    .container .table-list{
        margin: 10px;
    }
    .table th:nth-child(3), 
    .table td:nth-child(3){
        display: none; 
    }
}
</style>