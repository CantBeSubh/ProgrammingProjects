const puzzleBoard=document.querySelector('#puzzle')
const solveButton=document.querySelector('#solve-btn')
const result = document.querySelector('#result')
const submit=[]
const squares=81

for(let i=0;i<squares;i++){
    const elem=document.createElement('input')
    elem.setAttribute('type','number')
    elem.setAttribute('min','0')
    elem.setAttribute('max','9')
    if(
        ((i%9==0 || i%9==1 || i%9==2)&&i<21)||
        ((i%9==6 || i%9==7 || i%9==8)&& i<27)||
        ((i%9==3 || i%9==4 || i%9==5)&& (i>27 && i<53))||
        ((i%9==0 || i%9==1 || i%9==2)&& i>53)||
        ((i%9==6 || i%9==7 || i%9==8)&& i>53)
    ){
        elem.classList.add('grey')
    }
    puzzleBoard.appendChild(elem)
}

const joinValues=()=>{
    const inputs = document.querySelectorAll('input')
    inputs.forEach(i=>{
        if(i.value){submit.push(i.value)}
        else{submit.push('.')}
    })
    console.log(submit)
}

const populate=(solve,arr)=>{
    const inputs = document.querySelectorAll('input')
    if(solve && arr){
        inputs.forEach((input,i)=>{
            input.value=arr[i]
        })
        result.innerHTML='THIS IS ZE ANSWER!'
    }
    else{
        // console.log('NOT SOLVABLE')
        result.innerHTML='THIS IS NOT SOLVABLE :('
    }
}

const solve=()=>{
    joinValues()
    
}


solveButton.addEventListener('click',solve)