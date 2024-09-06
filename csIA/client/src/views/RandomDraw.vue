<template id="randomdraw">
    <header>
        <div class="h-wrap container-fluid">
            <h1>Random draw page</h1>
        </div>
    </header>
    <body>
        <div class="dropdown container fluid">
            <div class="row rows-cols-auto">
                <div class="btn-group col">
                    <span type="button" class="btn btn-secondary">Distance:</span>
                    <select class="form-select" aria-label="Default select example">
                        <option selected>Open this select menu</option>
                        <option value="1">200m</option>
                        <option value="2">300m</option>
                    </select>
                </div>
                <div class="btn-group col">
                    <span type="button" class="btn btn-secondary">Price:</span>
                    <select class="form-select" aria-label="Default select example">
                        <option selected>Open this select menu</option>
                        <option value="1">under $50</option>
                        <option value="2">under $60</option>
                    </select>
                </div>
                <div class="btn-group col">
                    <span type="button" class="btn btn-secondary">Type:</span>
                    <select class="form-select" aria-label="Default select example">
                        <option selected>Open this select menu</option>
                        <option value="1">fast food</option>
                        <option value="2">sushi</option>
                    </select>
                </div>
            </div>
        </div>
        <div class="rest-map container text-center">
            <div></div>
        </div>
        <div class = "draw-btn">
                <a type="button" class="btn btn-lg btn-secondary" href="/drawpage">Draw</a>
        </div>
    </body>
</template>

<style>
.h-wrap, .btn-group, .dropdown{
    display: flex;
    align-items: center;
    margin: 10px;
}
.dropdown .btn-group .form-select{
    box-sizing: border-box;
    background-color: #E6E6E6;
    border-radius: 0 5px 5px 0;
}
.draw-btn{
    margin: 20px;

}
</style>