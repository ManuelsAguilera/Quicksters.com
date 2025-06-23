import { Component, OnInit } from '@angular/core';
import { JuegosService } from '../../service/juegos.service';

@Component({
  selector: 'app-juegos',
  templateUrl: './juegos.page.html',
  styleUrls: ['./juegos.page.scss'],
  standalone: false,
})
export class JuegosPage implements OnInit {
  juegos: any[] = [];
  juegosVisibles: any[] = []; // los que se están mostrando
  nuevoAppid: number = 0;
  cantidadJuegos = 0;
  paginaActual = 0;
  tamanoPagina = 8;
  
  constructor(private juegosService: JuegosService) {}

  ngOnInit() {
    this.cargarJuegos();
  }

  cargarJuegos() {
    this.juegosService.obtenerJuegos().subscribe((resp: any) => {
      this.juegos = resp.data;
      this.cantidadJuegos = this.juegos.length;
      this.mostrarJuegos(); // mostrar los primeros 8
    });
  }

  mostrarJuegos() {
    const inicio = this.paginaActual * this.tamanoPagina;
    const fin = inicio + this.tamanoPagina;
    const nuevosJuegos = this.juegos.slice(inicio, fin);
    this.juegosVisibles = [...this.juegosVisibles, ...nuevosJuegos];
    this.paginaActual++;
  }

  importarJuego() {
    if (this.nuevoAppid > 0) {
      this.juegosService.importarDesdeSteam(this.nuevoAppid).subscribe({
        next: (resp: any) => {
          this.cargarJuegos();
          this.nuevoAppid = 0;
        },
        error: (err: any) => {
          console.error(err);
          alert('Error al importar el juego');
        }
      });
    }
  }

  aumentarJuegos() {
    this.mostrarJuegos();
  }

  resetearJuegos() {
    this.cantidadJuegos = 6; // Volver al valor inicial
  }
}





// export class JuegosPage implements OnInit {
//   juegos: any[] = [];
//   nuevoAppid: number = 0;

//   constructor(private juegosService: JuegosService) {}

//   ngOnInit() {
//     this.cargarJuegos();
//   }

//   cargarJuegos() {
//     this.juegosService.obtenerJuegos().subscribe(resp => {
//       this.juegos = resp.data;
//     });
//   }

//   importarJuego() {
//     if (this.nuevoAppid > 0) {
//       this.juegosService.importarDesdeSteam(this.nuevoAppid).subscribe({
//         next: (resp) => {
//           this.cargarJuegos();
//           this.nuevoAppid = 0;
//         },
//         error: (err) => {
//           console.error(err);
//           alert('Error al importar el juego');
//         }
//       });
//     }
//   }
// }


// export class JuegosPage implements OnInit {

//   cantidadJuegos = 20;

//   constructor() { }

//   ngOnInit() {
//   }

//   aumentarJuegos() {
//     this.cantidadJuegos += 5; // Aumentar de 4 en 4
//   }
  
//   resetearJuegos() {
//     this.cantidadJuegos = 8; // Volver al valor inicial
//   }
// }
