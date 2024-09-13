<script>

</script>

<template id="history">
    <body>
        <div class="container rows-cols-auto">
            <div class="table-list row">
                <table class="table table-borderless table-striped table-hover">
                    <thead class="table">
                        <tr>
                            <th scope="col">Date</th>
                            <th scope="col">Time</th>
                            <th scope="col">Restaurant name</th>
                            <th scope="col">Address</th>
                        </tr>
                    </thead>
                    <tbody class="table-group-divider">
                        <tr> 
                            <td>25/1/2024</td>
                            <td>2:51PM</td>
                            <td>Mcdonald's</td> 
                            <td>Choi Ming Shopping CentreShop Nos. 271</td>
                        </tr>
                        <tr v-for="record in historyRecords" :key="record.id" :to="`/history/${record.id}`"> 
                            <td>{{ record.date }}</td>
                            <td>{{ record.time }}</td>
                            <td>{{ record.restaurantName }}</td> 
                            <td>{{ record.address }}</td>
                        </tr>
                    </tbody>
                </table>
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
    </body>
</template>

<style scoped>
.container .table-list{
    background-color: #f4e7d2; 
    color: white; 
    padding: 40px;
    border-radius: 20px;
}
.container .table-list .table .table th{
    background-color: #e7b99a;
    color: #000000;
    font-weight: 500;
}
.container .table-list .table .table-group-divider zootd{
    background-color: #eeeee4;
    color: #454649;
}
.container .table-list .page-scroll{
    margin-top: 20px;
}
.container .table-list .page-scroll a{
    color: #454649;
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
    .table th:nth-child(4), 
    .table td:nth-child(4){
        display: none; 
    }
}
</style>