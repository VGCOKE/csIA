<template id="draw">
    <header>
        <div class="h-wrap">
            <h1>Random draw page</h1>
        </div>
    </header>
    <body>
        <div class="dropdown">
            <div class="btn-group">
                <button type="button" class="btn btn-secondary btn-lg">Distance:</button>
                <button type="button" class="btn btn-lg btn-secondary dropdown-toggle dropdown-toggle-split" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    <span class="sr-only">Dropdown</span>
                </button>
                <div class="dropdown-menu">
                    <h6 class="dropdown-header">Distance</h6>
                    <a class="dropdown-item" href="#">200m</a>
                </div>
            </div>
            <div class="btn-group">
                <button type="button" class="btn btn-secondary btn-lg">Price:</button>
                <button type="button" class="btn btn-lg btn-secondary dropdown-toggle dropdown-toggle-split" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    <span class="sr-only">Dropdown</span>
                </button>
                <div class="dropdown-menu">
                    <a class="dropdown-item" href="#">200m</a>
                </div>
            </div>
            <div class="btn-group">
                <button type="button" class="btn btn-secondary btn-lg">Type::</button>
                <button type="button" class="btn btn-lg btn-secondary dropdown-toggle dropdown-toggle-split" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    <span class="sr-only">Dropdown</span>
                </button>
                <div class="dropdown-menu">
                    <a class="dropdown-item" href="#">200m</a>
                </div>
            </div> 
        </div>
    </body>
</template>

<style>
.h-wrap, .btn-group{
    align-items: center;
    display: flex;
    margin: 10px;
}

</style>