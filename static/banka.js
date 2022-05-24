'use strict'

//iskanje igralcev po imenih 
  function isci_igralec() {
    let vrednost = document.getElementById('isci_igralec').value;
    let tabela = document.getElementById('igralci');
    [...tabela.rows].forEach(vrstica => {
      let vsebina=vrstica.cells[0].innerText
      if(vsebina.toLocaleLowerCase().indexOf(vrednost.toLocaleLowerCase()) >= 0) {
        vrstica.style.display = ''
      }
      else {
        vrstica.style.display = 'none'
      }
    })
  }



 


//iskanje igralcev po starosti 
  function isci_starost() {
    let vrednost = document.getElementById('isci_starost').value;
    let tabela = document.getElementById('igralci');
    [...tabela.rows].forEach(vrstica => {
      let vsebina=vrstica.cells[1].innerText
      if(vsebina.toLocaleLowerCase().indexOf(vrednost.toLocaleLowerCase()) >= 0) {
        vrstica.style.display = ''
      }
      else {
        vrstica.style.display = 'none'
      }
    })
  }


  //iskanje igralcev po točkah 
  function isci_tocke() {
    let vrednost = document.getElementById('isci_tocke').value;
    let tabela = document.getElementById('igralci');
    [...tabela.rows].forEach(vrstica => {
      let vsebina=vrstica.cells[4].innerText
      if(vsebina.toLocaleLowerCase().indexOf(vrednost.toLocaleLowerCase()) >= 0) {
        vrstica.style.display = ''
      }
      else {
        vrstica.style.display = 'none'
      }
    })
  }