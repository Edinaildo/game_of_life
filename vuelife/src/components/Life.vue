<template>
    <div class="body">
        <table>
            <tr v-for="(line, i) in grid" :key="i">
                <td v-for="(cell, j) in line" :key="j" :class="{vivo: cell==1}"></td>
            </tr>
        </table>
    </div>
</template>

<script>


function _count_vizinhos_vivos(i, j, grid){
    const [M, N] = [grid.length, grid[0].length]
    const delta_coord = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 1], 
        [1, -1], [1, 0], [1, 1],
    ]
    let coord_vizinhos = []
    for (let k = 0; k < delta_coord.length; k++ ){
        coord_vizinhos.push([i + delta_coord[k][0], j + delta_coord[k][1]])
    }
    let coord_vizinhos_vivos = coord_vizinhos.filter((e) => e[0] >= 0 && e[0] < M && e[1] >= 0 && e[1] < N && grid[e[0]][e[1]] == 1)
    return coord_vizinhos_vivos.length
}

function _nextState(grid){
    const [M, N] = [grid.length, grid[0].length]
    let newGrid = new Array(M)
    for (let i = 0; i < M; i++){
        newGrid[i] = new Array(N).fill(0)
    }
    for (let i = 0; i < M; i++){
        for (let j = 0; j < N; j++){
            let vizinhosvivos = _count_vizinhos_vivos(i,j,grid)
            if (grid[i][j] == 1){
                if (vizinhosvivos == 2 || vizinhosvivos == 3){
                    newGrid[i][j] = 1
                } else {
                    newGrid[i][j] = 0
                }
            } else {
                if (vizinhosvivos == 3){
                    newGrid[i][j] = 1
                }
                else {
                    newGrid[i][j] = 0
                }
            }
        }
    }

    return newGrid
}

export default {
    name: 'Life',
    data() {
        return {
            grid: [
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,1,0,0,0],
                [0,0,0,0,1,0,1,0,0,0],
                [0,0,0,0,0,0,1,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,1,1,1],
                [0,1,1,0,0,0,1,1,0,0],
                [0,1,0,0,0,0,1,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
            ]
        }
    },
    methods: {
        nextStep(){
            this.grid = _nextState(this.grid)
    },
    },
    mounted(){
        setInterval(() => {
            this.nextStep()
        }, 1000)
    }
  }
</script>

<style>
table, th, td {
    justify-content: center;
    border: 1px solid;
}
td {
    width: 70px;
    height: 70px;
}
.body{
    height: ;
}
.vivo {
    background-color: yellow;
}
</style>
