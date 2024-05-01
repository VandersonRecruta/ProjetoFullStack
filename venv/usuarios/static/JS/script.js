// Adiciona um evento ao botão
var combo = document.querySelector('#combo')
    combo.addEventListener('click', VeriCombo)

// Função para verificar se o valor foi adicionado
function VeriCombo(){
    let quantidade = document.querySelector('#Qcombo').value;

    if (quantidade == 0){
        respCombo.innerHTML = 'Você não selecionou a quantidade'
        respCombo.style.color = 'red';
    }else{
        respCombo.innerHTML = 'Combo de Sushi e Sashimi Adicionado ao carrinho!'
        respCombo.style.color = 'green';
        setTimeout(function(){
            let resposta = confirm('Ir para o carrinho de compras?')
            if (resposta){
                window.location.href = '/carrinho/'
            }
        }, 200)
    }
}

// Adiciona um evento ao botão 
var salmao = document.querySelector('#salmao')
    salmao.addEventListener('click', VeriSalmao)

// Função para verificar se o valor foi adicionado
function VeriSalmao(){
    let quantidade = document.querySelector('#Qsalmao').value;

    if (quantidade == 0){
        respSalmao.innerHTML = 'Você não selecionou a quantidade'
        respSalmao.style.color = 'red';
    }else{
        respSalmao.innerHTML = 'Temaki de Salmão com cream cheese Adicionado ao carrinho!'
        respSalmao.style.color = 'green';
        setTimeout(function(){
            let resposta = confirm('Ir para o carrinho de compras?')
            if (resposta){
                window.location.href = '/carrinho/'
            }
        }, 200)
    }
}

// Adiciona um evento ao botão 
var temaki = document.querySelector('#temaki')
    temaki.addEventListener('click', VeriTemaki)

// Função para verificar se o valor foi adiconado
function VeriTemaki(){
    let quantidade = document.querySelector('#Qtemaki').value;

    if (quantidade == 0){
        respTemaki.innerHTML = 'Você não selecionou a quantidade'
        respTemaki.style.color = 'red';
    }else{
        respTemaki.innerHTML = 'Temaki Doce Adicionado ao carrinho!'
        respTemaki.style.color = 'green';
        setTimeout(function(){
            let resposta = confirm('Ir para o carrinho de compras?')
            if (resposta){
                window.location.href = '/carrinho/'
            }
        }, 200)
    }
}


// Adiciona um evento ao botão
var barca = document.querySelector('#barca')
    barca.addEventListener('click', VeriBarca)


// Função para verificar se o valor foi adicionado
function VeriBarca(){
    let quantidade = document.querySelector('#Qbarca').value;

    if (quantidade == 0){
        respBarca.innerHTML = 'Você não selecionou a quantidade'
        respBarca.style.color = 'red';
    }else{
        respBarca.innerHTML = 'Barca de Sushi e Sashimi Adicionado ao carrinho!'
        respBarca.style.color = 'green';
        setTimeout(function(){
            let resposta = confirm('Ir para o carrinho de compras?')
            if (resposta){
                window.location.href = '/carrinho/'
            }
        }, 200)
        
    }
}
