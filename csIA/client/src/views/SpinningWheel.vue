<script>
    import VueWheelSpinner from 'vue-wheel-spinner';
    import { Modal } from 'bootstrap';
    import axios from 'axios';

    // import cursorImage from 'client/src/assets/cursor3.svg';
    // import wonSound from './sounds/won.mp3';
    // import clickSound from './sounds/click.mp3';
    // import hoverSound from './sounds/hover.mp3';
    // import leaveSound from './sounds/leave.mp3';
    // import spinningSound from './sounds/spinning.mp3';

    export default {
        components: {
            VueWheelSpinner
        },
        props: {
            restaurants: {
                type: Array,
                required: true
            }
        },
        data() {
        return {
            winnerResult: null,
            isSpinning: false,
            defaultWinner: 0,
            restaurants: [],
            usedColors: [],
            winnerModal: null,
        //     sounds: {
        //     won: wonSound,
        //     spinButtonClick: clickSound,
        //     spinButtonHover: hoverSound,
        //     spinButtonLeave: leaveSound,
        //     spinning: spinningSound
        //     },
            // cursorImage,
            // cursorAngle: 0,
            // cursorPosition: 'edge',
            // cursorDistance: 0
        };
        },
        computed: {
            restaurantSlices() {
                this.usedColors = [];
                return this.restaurants ? this.restaurants.map(restaurant => ({
                    color: this.getUniqueRandomColor(),
                    text: restaurant.name
                })): [];
            }
        }, 
        methods: {
            handleDirectionAndSave() {
                if (this.winnerResult) {
                    this.saveWinnerToHistory()
                    .then(() => {
                        this.redirectToGoogleMap();
                    })
                    .catch(err => {
                        console.log(err);
                    });
                }
            },
            saveWinnerToHistory() {
                const winnerData = {
                    name: this.winnerResult.text,
                };

                return axios.post('http://127.0.0.1:5000/history', winnerData) 
                    .then(response => {
                    console.log('Winner saved to history:', response.data);
                    });
                },

                redirectToGoogleMap() {
                const restaurantName = encodeURIComponent(this.winnerResult.text);
                const googleMapsUrl = `https://www.google.com/maps/search/?api=1&query=${restaurantName}`;
                window.location.href = googleMapsUrl;
            },
            getRandomColor() {
                const orangeShades = [
                    '#FFA500',
                    '#FF8C00',
                    '#FF7F50',
                    '#FFD700',
                    '#FFE4B5',
                    '#FFFAF0',
                    '#FFFFFF' 
                ];
                const randomIndex = Math.floor(Math.random() * orangeShades.length);
                return orangeShades[randomIndex];
            },
            getUniqueRandomColor() {
                let newColor;
                do {
                    newColor = this.getRandomColor();
                } while (this.usedColors.includes(newColor));

                this.usedColors.push(newColor);
                return newColor;
            },
            playAudio(audio) {
                if (audio) {
                audio.volume = 0.5
                audio.play();
                }
            },
            handleSpinButtonClick() {
                if (this.buttonClickAudio) {
                this.playAudio(this.buttonClickAudio)
                }
                this.$refs.spinner.spinWheel(this.defaultWinner);
            },
            handleSpinButtonHover() {
                if (this.buttonHoverAudio) {
                this.playAudio(this.buttonHoverAudio)
                }
            },
            handleSpinButtonLeave() {
                if (this.buttonLeaveAudio) {
                this.playAudio(this.buttonLeaveAudio)
                }
            },
            spinFor(index) {
                this.defaultWinner = index;
                this.$refs.spinner.spinWheel(index);
            },
            onSpinStart() {
                this.winnerResult = null;
                this.isSpinning = true;
            },
            onSpinEnd(winnerIndex) {
                this.isSpinning = false;
                this.winnerResult = this.restaurantSlices[winnerIndex];
                this.winnerModal = new Modal(document.getElementById('winnerModal'))
                this.winnerModal.show(); 
            },
            pickAgain() {
                this.winnerModal.hide();
                this.handleSpinButtonClick();
            }
            },
            mounted() {
                //this.buttonHoverAudio = new Audio(hoverSound);
                //this.buttonLeaveAudio = new Audio(leaveSound);
                //this.buttonClickAudio = new Audio(clickSound);
                axios.get('http://127.0.0.1:5000/')
                    .then(response => {
                        this.restaurants = response.data.restaurant;
                    })
                    .catch(err => {
                        console.log(err);
                });
        },
    };
</script>

<template>
    <div class="container">
            <VueWheelSpinner
            ref="spinner"
            :slices="restaurantSlices"
            :winner-index="defaultWinner"
            :sounds="sounds"
            :cursor-angle="cursorAngle"
            :cursor-position="cursorPosition"
            :cursor-distance="cursorDistance"
            @spin-start="onSpinStart"
            @spin-end="onSpinEnd">

            <template #cursor>
            <img class="cursor-img" :src="cursorImage" alt="Cursor">
            </template>

            <template #default>
            <button
                class="spin-button"
                :disabled="isSpinning"
                @click="handleSpinButtonClick"
                @mouseover="handleSpinButtonHover"
                @mouseleave="handleSpinButtonLeave">
                Spin
            </button>
            </template>
        </VueWheelSpinner>
    </div>
    <div class="modal fade" id="winnerModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="staticBackdropLabel">The winner restaurant is</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <h2 v-if="winnerResult">{{ winnerResult.text }}</h2>
                <p v-if="winnerResult"></p> 
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-primary" @click="handleDirectionAndSave" data-bs-dismiss="modal">Direction + Save record</button>
                <button type="button" class="btn btn-secondary" @click="pickAgain">Pick again</button>
            </div>
            </div>
        </div>
    </div>
</template>

<style>
.modal .modal-dialog .modal-footer .btn-primary{
    background-color: transparent;
    color: #dcb081;
    border: 2px solid #dcb081;
}
.modal .modal-dialog .modal-footer .btn-secondary{
    background-color: #dcb081;
    color: #343a40;
    border: 2px solid #dcb081;
}
.container{
    height: 80%;
    justify-content: center;
}
canvas{
    max-width: 70% !important;
}
.cursor-img {
    width: 50px;
    aspect-ratio: 1 / 1;
    filter: drop-shadow(3px 3px 2px rgba(169, 169, 169, 0.19));
}
.spin-button {
    width: 100px;
    height: 100px;
    margin: 0 auto;
    aspect-ratio: 1 / 1;
    font-size: 20px;
    cursor: pointer;
    background: #ffb868;
    border-radius: 50%;
    transition: all 150ms;
    border: 5px solid white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    color: white !important;
    box-shadow: inset -3px -3px 2px 2px rgba(0, 0, 0, 0.19), 3px 3px 2px 2px rgba(0, 0, 0, 0.19);
    z-index: 11;
    position: relative;
    user-select: none;
    &:hover {
    box-shadow: inset -5px -5px 2px 2px rgba(0, 0, 0, 0.19), 3px 3px 2px 2px rgba(0, 0, 0, 0.19);
    }
    &:active {
    box-shadow: inset 3px 3px 2px 2px rgba(0, 0, 0, 0.19), 3px 3px 2px 2px rgba(0, 0, 0, 0.19);
    }
    &:disabled {
    background: #ccc;
    cursor: not-allowed;
    pointer-events: none;
    }
}

</style>