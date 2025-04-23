import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-juegos',
  templateUrl: './juegos.page.html',
  styleUrls: ['./juegos.page.scss'],
  standalone: false,
})
export class JuegosPage implements OnInit {

  cantidadJuegos = 20;

  constructor() { }

  ngOnInit() {
  }

  aumentarJuegos() {
    this.cantidadJuegos += 5; // Aumentar de 4 en 4
  }
  
  resetearJuegos() {
    this.cantidadJuegos = 8; // Volver al valor inicial
  }
}
